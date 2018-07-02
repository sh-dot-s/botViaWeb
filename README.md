# botViaWeb

Simple Bot using DNN (Tensorflow) and served using Django

### Installing Requirements
> Run the command in root directory (where manage.py lives)

`pip install -r requirements.pip --no-index --find-links file:///tmp/packages`

##Training

Expected responses to speech requests can be configured in **Intents.json** file present in the same root folder

##### Example
```json
{
  "intents": [{
      "tag": "greeting",
      "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
      "responses": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"],
      "context_set": ""
    },
    {
      "tag": "goodbye",
      "patterns": ["Bye", "See you later", "Goodbye"],
      "responses": ["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."]
    }
  ]
}
```
## Firing the Server and Requests
Start the server on desired port in localhost/any ip and port. Localhost and 8000 are the defaults
```bash
python manage.py runserver
python manage.py runserver 10.1.1.1:2130
```
The server only accepts GET request (can be configured otherwise also) with **Speech** as query text

`http://localhost:8000/?speech="Hi there, I am a sample text"`

The Expected response will be
```json
{
	result: {
		"tag":"response"
	}
}
```