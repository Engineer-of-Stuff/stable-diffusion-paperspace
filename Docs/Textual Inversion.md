#->`--RETARD'S GUIDE TO TEXTUAL INVERSION--`<-#
->*Quitters never win, and winners never quit.*<-

Textual inversion allows you to train data sets of specific styles or things, which will then be tied to a specific word. It does this without affecting how the model file works as a whole, allowing you to inject keyword shortcuts. If that doesn't excite you, let me put it another way - 
This lets you tie a keyword to specific people, things, places, or art styles in Stable Diffusion that you otherwise would be unable to directly reference. It's a game changer.

==**If you'd prefer to run the trainer locally:**==
You can do so using [**this repo**](https://github.com/huggingface/diffusers/tree/main/examples/textual_inversion)
However this guide is for training on Colab, so you may have to figure out some things yourself.
(Also local Textual Inversion requires at least 12gb of vram at a minimum)

!!!note In the beginning...
**NOTE: You will need Stable Diffusion installed before proceeding, follow the recommended setup guide [**HERE**](https://rentry.org/voldy)

**STEP 1:**  In file explorer, navigate to your root stable diffusion directory (`/stable-diffusion-webui`). 
Create a new folder in this location called `embeddings` (If there isn't one already)

**STEP 2:** Visit the [Stable Diffusion Concept Library](https://huggingface.co/sd-concepts-library) and pick any model.
After selecting the one you wish to install, open a git bash in your `/embeddings` folder and type `git clone` followed by the model URL
eg. `git clone https://huggingface.co/sd-concepts-library/bonzi-monkey`

**STEP 3:** Enter the directory for the model you just downloaded. 
Open `token-identifier.txt` and copy the contents, ignoring the < > (you need to enter them when you put the token into your prompt, but the file name is irrelevant to that).

**STEP 4:** Right click on learned_embeds.bin, click rename, paste what you copied out of token-identifier.txt, and hit enter

**STEP 5:** Move this newly renamed `.bin` file to the `/embeddings` directory. Feel free to delete the directory you cloned for the model once you have moved the `.bin` file out of it.

**Step 6:** Launch Voldy's SD and make sure your newly added model works.
 Pay attention to the name of the `.bin`, That's the keyword which tells Stable Diffusion to use it. 
Use the name within `<  >` brackets, alongside normal prompts:
Example prompt: `<bonzi-monkey>, photorealistic, oil painting, vintage`
==Enjoy!==
!!!note But I want to make my own!

**Step 1:** Once you've figured out what you want to integrate, pick 3-5 photos of your selection, and crop them down into square images, preferably **512x512**

**Step 2:** Upload your photos to a publicly accessible database. 
[Imgur](https://imgur.com) allows for hidden photos with a publicly accessible link

**Step 3:** Go to the [Textual Inversion Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_textual_inversion_training.ipynb#scrollTo=Yl3r7A_3ASxm) and follow the step by step instructions to run the model training, clicking the play button to the left at each new portion.
For your image files, make sure whatever you're inputting is the **direct link** ending in `.jpg`, .`png`, or something of the like. 
!!! info Make sure you have a [Huggingface](https://huggingface.co/join) account. The Colab will give you a link to generate your token code, when you follow it, generate a **write code**

**Step 4:** Once the training has fully run, click the folder on the left side of the screen. 
Click `sd-concept-output`, click the three dots to the right of `learned_embeds.bin`, click download. 
Once the file has downloaded, rename it to whatever you provided as your placeholder token.

**Step 5:** Move this newly renamed `.bin` file to the `/embeddings` directory.

**Step 6:** Launch Voldy's SD and make sure your newly added model works.
==Have fun!==
