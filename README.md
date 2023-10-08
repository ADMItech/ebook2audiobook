# General description of the project

This is python script that uses Google
Text-to-Speech for creating audiobooks.
Actual preset is suitable for ebooks written 
in the Slovak language. 

gTTS is also set for Slovak language.
Please see code note to setup different language.



## Install Python 3.9

Please install [Python 3.9](www.python.org)


## Install all required packages


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
python3 -m pip install -r requirements.txt
```




## Run Script

### RawData and Output
RawData folder is place where to place your .mobi ebook.

OutPut folder is place where you will find recorder audiobook in mp3 format.

 ```bash
python3 main.py
```
Existing Sample file of the .mobi ebook is included. This file will generate approx. 18 minutes of audiobook.





## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](LICENSE.md)
