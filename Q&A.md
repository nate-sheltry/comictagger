# Why modify/fork ComicTagger
**Q: Isn't it still getting updated from time to time?**
<br>
> A: While there have been pre-release versions in development since 2022, whenever I attempted to use said releases I found I was lucky if I could get the app to not crash when accessing settings, making it impossible to scrape any data.

**Q: Why go back to 1.5.5?**
<br>
> A: This ties into the above statement, 1.5.5 was the last full release in 2022, and has been my primary tool.

**Q: Whats with the new image formats?**
<br>
> A: In my own personal use I've been experimenting with using other more modern formats, while some are more proprietary, such as *JPEG XL*, formats like *AVIF* have become increasingly well supported in both browsers and reading devices.

**Q: Do you hope to change the standard image formats of cbz and cbr by adding support?**
<br>
> A: No.
> 
> While I would love to see image formats evolve beyond *JPEG*, I do realize *JPEG* provides a wide color chroma, universal support, and is extremely quick to compress images into. *WEBP* is similar in compression time but is restricted to a smaller color chroma resulting in loss color data.
>
> However formats like *AVIF* provide the same color chroma while being half the size.

**Q: What if I use an older device, is there any point in moving away from JPEG?**
> A: Potentially, if you use a local server for hosting images, *AVIF* files can save storage, preserve detail, and are easily converted to other image types for devices that cannot read them directly. If your local server solution supports reading them, it most likely supports converting them to a compatible image type for the reader.

**Q: What even are these formats, JPEG XL, AVIF, HEIC?**
<br>
> A: Similar to how new compression formats lead to the development of the Blu-Ray, 4k, and HD streaming, these new image formats make storing, working with, preserving images easier.
> 
> *AVIF* is based off the *AV1* video compression, *HEIC* is based off the *HEVC* or *x265* video compression, and *HEIF* is a more broadly compatible version of that. *JPEG XL* is an especially neat format for comic goers as it allows a way to shrink existing *JPEG* files without adding any additional quality loss, while also providing its own form of compression which is comparable to the aforementioned formats.

**Q: Anything else you're adding to a more or less already great program?**
<br>
> A: Not really. I have a few things I'd like to test and check based off some rare bugs I encountered, but really I only did this because it met my own use case.

[Back](https://github.com/nate-sheltry/comictagger)