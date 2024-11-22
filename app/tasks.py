import os
from typing import Any, Dict

import docker
from celery_app import app
from docker.errors import ContainerError, DockerException, ImageNotFound


@app.task
def read_file() -> Dict[str, Any]:
    """
    Read files from a Docker container and return the results.

    This function performs the following steps:
    1. Creates a Docker client and runs a container with the 'read_file' image.
    2. Mounts a local directory to the container.
    3. Waits for the container to finish execution and captures its logs.
    4. Returns the container's exit status and logs.

    Returns:
        Dict[str, Any]: A dictionary containing the container's exit status and logs.
        The dictionary has two keys:
        - 'status': An integer representing the container's exit status.
        - 'logs': A string containing the container's logs.

    Raises:
        Exception: If any error occurs during the execution of the function.
        In this case, the function returns a dictionary with status -1 and the error message.
    """
    try:
        client = docker.from_env()

        container = client.containers.run(
            image="read_file",
            name=f"read_file_container_{os.getpid()}",
            detach=True,
            remove=False,
            volumes={
                os.environ.get("SOURCE_PATH", ""): {
                    "bind": "/files_to_read",
                    "mode": "ro",
                }
            },
        )

        try:
            result = container.wait()
            logs = container.logs().decode("utf-8")
            print(f"Container logs: {logs}")
            return {"status": result["StatusCode"], "logs": logs}
        finally:
            container.remove(force=True)

    except Exception as e:
        print(f"Error: {str(e)}")
        return {"status": -1, "logs": f"Error: {str(e)}"}
    finally:
        if "client" in locals():
            client.close()
