from denoising_diffusion_pytorch import Unet, GaussianDiffusion
import os.path
from torchvision import transforms
import torch

if __name__ == "__main__":
    model = Unet(
        dim=16,
        dim_mults=(1, 2, 4)
    )

    diffusion = GaussianDiffusion(
        model,
        image_size=32,
        timesteps=1000,  # number of steps
        loss_type='l1'  # L1 or L2
    )

    data = torch.load("models/cat_mini.pt",map_location=torch.device('cpu'))
    diffusion.load_state_dict(data['model'])
    diffusion.eval()
    images_tensor = diffusion.sample(1)

    if(not os.path.exists("results")):
        os.mkdir("results")

    for i,image_tensor in enumerate(images_tensor):
        image = transforms.ToPILImage(mode='RGB')(image_tensor)
        image.save(f"results/sample_{i}.png")
