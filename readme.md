# README

## What's this?

A simple m3u8 downloader based on scrapy.

## How to use it.

The project is based on scrapy, so you need python3 and scrapy.

Open the project in the terminal and type the command like:

```shell
scrapy m3u8 https://example.com/xxxx.m3u8
```

The m3u8 , ts and key files will be downloaded into path `movie/xxxx`.

This project will __never__ provide the services like `decrypt ts file`, `merge ts files`, or `transfer video from m3u8 into mp4`.

But you can use `vlc` (the most powerful video player I have ever seen) to open the xxxx.m3u8 file and play it.

## How can I help improve it

I wrote this small project just for myself, so...

If this project not work for your case, feel free to let me know, or fix it yourself, we will make it better!

## TODO

- [ ] make the project more general.
- [ ] friendly command line interface and documents.
- [ ] try to build a single binary file.