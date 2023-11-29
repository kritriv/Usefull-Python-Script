import os
from PIL import Image

def convert_jpg_to_webp(input_image_path, output_image_path):
  input_image = Image.open(input_image_path)
  input_image.save(output_image_path, format='WEBP')

def convert_all_images_in_folder_to_webp(input_folder_path, output_folder_path):
  if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

  for filename in os.listdir(input_folder_path):

    if filename.endswith('.png'):
      input_image_path = os.path.join(input_folder_path, filename)
      output_image_path = os.path.join(output_folder_path, filename[:-4] + '.webp')

      convert_jpg_to_webp(input_image_path, output_image_path)

if __name__ == '__main__':
  input_folder_path = 'tar_other_more_old' 
  output_folder_path = 'tar_other_more_new'

  convert_all_images_in_folder_to_webp(input_folder_path, output_folder_path)
