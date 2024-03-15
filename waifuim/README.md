## Developer Notes
 - The artist name is only callable for SFW images, as such NSFW images don't have the option to display the artist name. For this reason I have commited the artist name out of the embeds. If you wish to enable them yourself simply fork this repo and use your own personal fork with your instance.

 - Here are some examples of the current json structure for the waifu.im api:

### **NSFW Structure**

```js
{
  "images": [
    {
      "signature": "",
      "extension": "",
      "image_id": 0000,
      "favorites": 0,
      "dominant_color": "#000000",
      "source": "",
      "artist": null,
      "uploaded_at": "",
      "liked_at": null,
      "is_nsfw": true,
      "width": ,
      "height": 1080,
      "byte_size": 0000000,
      "url": "",
      "preview_url": "",
      "tags": [
        {
          "tag_id": 0,
          "name": "",
          "description": "",
          "is_nsfw": true
        },
        {
          "tag_id": 0,
          "name": "",
          "description": "",
          "is_nsfw": true
        },
        {
          "tag_id": 0,
          "name": "",
          "description": "",
          "is_nsfw": false
        },
        {
          "tag_id": 0,
          "name": "",
          "description": "",
          "is_nsfw": false
        }
      ]
    }
  ]
}
```

### **SFW Structure**

```js
{
  "images": [
    {
      "signature": "",
      "extension": "",
      "image_id": 0000,
      "favorites": 0,
      "dominant_color": "#000000",
      "source": "",
      "artist": {
        "artist_id": 00,
        "name": "",
        "patreon": null,
        "pixiv": "",
        "twitter": "",
        "deviant_art": null
      },
      "uploaded_at": "",
      "liked_at": null,
      "is_nsfw": false,
      "width": 1273,
      "height": 1800,
      "byte_size": 0000000,
      "url": "",
      "preview_url": "",
      "tags": [
        {
          "tag_id": 0,
          "name": "",
          "description": "",
          "is_nsfw": false
        }
      ]
    }
  ]
}
```