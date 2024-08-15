from fastapi import FastAPI
from pydantic import BaseModel, Field
from generator import image_generator

app = FastAPI()


class ImageGenerateModel(BaseModel):
    base_filename: str
    amount: int
    prompt: str
    prompt_size: int
    negative_prompt: str
    style: str
    resolution: str
    guidance_scale: int


@app.get('/')
async def root():
    return "Hello Thong"


@app.post('/imagegenerate')
async def image_generate(image_generate_model: ImageGenerateModel):
    generator = image_generator(
        base_filename=image_generate_model.base_filename,
        amount=image_generate_model.amount,
        prompt=image_generate_model.prompt,
        prompt_size=image_generate_model.prompt_size,
        negative_prompt=image_generate_model.negative_prompt.replace(' ', ', '),
        style=image_generate_model.style,
        resolution=image_generate_model.resolution,
        guidance_scale=image_generate_model.guidance_scale
    )

    return {"generator": generator}
