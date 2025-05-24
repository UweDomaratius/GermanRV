# GermanRV

The German Road Vehicle Set is (as the name implies) a vehicle set for Open Transport Tycoon.
It includes a variety of busses, trams and trucks from the early 20th century to the present.

## Usage

To use the set in your game, head over to [Releases](https://github.com/UweDomaratius/GermanRV/releases) and download the latest version.
Unzip the archive and copy the grf file into the corresponding location of your OpenTTD installation (typically `C:\Users\<you>\Documents\OpenTTD\newgrf\`).
Start the game and the set should show up in the list of the NewGRF settings.

## Contributing

If you think you found a bug or the set is missing something, check the [Issues](https://github.com/UweDomaratius/GermanRV/issues) section and create a new issue if necessary.

In case you feel like contributing to the set development, feel free to fork the repository and provide your input as a new [pull request](https://github.com/UweDomaratius/GermanRV/pulls).

## Compiling from source

The source code and all graphics are contained in this repository.
To compile, you will need a working NML compiler installation.
Follow the instructions at [NML](https://github.com/OpenTTD/nml) to set it up, but I found that `python -m pip install --upgrade pip setuptools wheel nml` might be enough, as long as you have a working python installation on your system.

The set itself comes with a build file written in python, you only need to run `python build.py` to compile the sources.
A new grf will be created in a subfolder named `build`.

## License

The set is licensed under the [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/4.0/) CC-BY-NC-SA license.

Graphics by Daniel Böhme, Uwe Domaratius, Roland Kahlert, Stephan Krause, Hansel Kruzer.
Code by Uwe Domaratius.

## Acknowledgements

Special thanks to Michael Blunck for various cargo sprites and general help with the development.
