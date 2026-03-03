"""Annotated example: generate an image and save it to disk.

Before running:
- Install the OpenAI SDK: `pip install openai`
- Set `OPENAI_API_KEY` in your shell
"""

import base64

try:
    from openai import OpenAI
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Missing dependency: install the OpenAI SDK with `pip install openai`, "
        "then rerun this script."
    ) from exc


# The SDK reads OPENAI_API_KEY from the environment.
client = OpenAI()


def generate_image(prompt, output_path="cat_and_otter.png"):
    """Generate one image from a text prompt and save it locally."""
    response = client.responses.create(
        model="gpt-5.2",
        input=prompt,
        tools=[{"type": "image_generation"}],
    )

    # Image results are returned in the response output items. For image
    # generation calls, `result` contains a base64-encoded image payload.
    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]

    if not image_data:
        raise RuntimeError("No image data was returned by the API.")

    with open(output_path, "wb") as file_handle:
        file_handle.write(base64.b64decode(image_data[0]))

    print(f"Saved image to: {output_path}")


if __name__ == "__main__":
    generate_image(
        "Generate an image of a gray tabby cat hugging an otter with an orange scarf"
    )
