"""Annotated example: using the Responses API with file inputs.

This example shows two common patterns:
1. Analyze a remote PDF by passing a public file URL.
2. Upload a local file first, then reference it by file ID.

Before running:
- Install the OpenAI SDK: `pip install openai`
- Set `OPENAI_API_KEY` in your shell
"""

try:
    from openai import OpenAI
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Missing dependency: install the OpenAI SDK with `pip install openai`, "
        "then rerun this script."
    ) from exc


# The SDK reads OPENAI_API_KEY from the environment.
client = OpenAI()


def analyze_remote_file():
    """Send a public file URL directly to the model."""
    response = client.responses.create(
        model="gpt-5.2",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Analyze this file and provide a summary of the key points.",
                    },
                    {
                        # Use a public URL when the file is already hosted somewhere.
                        "type": "input_file",
                        "file_url": "https://arxiv.org/pdf/1409.3215",
                    },
                ],
            }
        ],
    )

    print("Remote file summary:")
    print(response.output_text)


def upload_local_file(local_path):
    """Upload a local file and return its file ID."""
    with open(local_path, "rb") as file_handle:
        uploaded_file = client.files.create(
            file=file_handle,
            purpose="user_data",
        )

    print(f"Uploaded file ID: {uploaded_file.id}")
    return uploaded_file.id


def analyze_uploaded_file(file_id):
    """Reference a previously uploaded file in a new Responses API request."""
    response = client.responses.create(
        model="gpt-5.2",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Summarize this uploaded file and list the main takeaways.",
                    },
                    {
                        # Use file_id after uploading a file from your own machine.
                        "type": "input_file",
                        "file_id": file_id,
                    },
                ],
            }
        ],
    )

    print("Uploaded file summary:")
    print(response.output_text)


if __name__ == "__main__":
    # Example 1: analyze a remote file URL.
    analyze_remote_file()

    # Example 2: upload a local file, then analyze it.
    # Replace this path with a real file on your machine before uncommenting.
    # file_id = upload_local_file("/absolute/path/to/language_understanding_paper.pdf")
    # analyze_uploaded_file(file_id)
