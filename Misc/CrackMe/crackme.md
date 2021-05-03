# Crack Me
_I follow all the security rules, for example, I have ensured that my password is in lowercase, long enough, no spaces and with the format mydogbreed, myluckycolor, mytelephonecountrycode and underscores in between. See how cautious I am. Oh wait, did I leak something that I should not?_

_Password Hash:_
` 1bf575335ff6a3bad86bfa2c83a884fa018253483c7e5630629761a23523e963`

_Add shaktictf{} to the password obtained._

## Solution

First of all we checked the hash type thanks to `hash-identifier` (https://tools.kali.org/password-attacks/hash-identifier). We found out it was a `sha256` hash.
In order to crack the Hash we used `hashcat` (https://github.com/hashcat/hashcat) in a custom bash script ([`crack.sh`](https://github.com/TryKatChup/ShaktiCTF2021-writeup/blob/main/Misc/CrackMe/crack.sh)). Before executing it, we downloaded the colors (https://www.scrapmaker.com/data/wordlists/colors/colors.txt) and dog breeds (https://github.com/the911s/dog_breeds/blob/master/breed_list) dictionaries. 

Firstly, we removed the spaces and converted all the letters to lowercase for both dictionaries.

```sh
tr -d ' '      < dogs.txt     > dogs_tmp.txt
tr 'A-Z' 'a-z' < dogs_tmp.txt > dogs2.txt
tr -d ' '      < colors.txt     > colors_tmp.txt
tr 'A-Z' 'a-z' < colors_tmp.txt > colors2.txt
```

With the modified version of the dictionaries, we append two words from two dictionaries with `_` between them and at the end of the extracted words:

```sh
hashcat -a 1 -j '$_' -k '$_' dogs2.txt colors2.txt --stdout | grep _ > dogscolors.txt
```

`-a 1` specifies the attack mode, which is the `Combination` mode in this case.
`-j` specifies the single rule applied to each word from left wordlist(`dogs2,txt`), in this case to append the `_` to a dog breed.
`-k` specifies the single rule applied to each word from right wordlist (`colors2.txt`), in this case to append `_` to a color.

Every combination is saved in a temporary dictionary, called `dogscolors.txt`.

In order to obtain the telephone country code number we generated every number from 000 to 999 in mask mode with `?d?d?d`.

```sh
hashcat -a 6 dogscolors.txt '?d?d?d'     --stdout | grep _ >> dogscolorsnumber.txt
```
`-a 6` is the `Hybrid Wordlist + Mask` attack mode.

We cracked `sha2-256`:
```sh
hashcat -a 0 -m 1400   test dogscolorsnumber.txt`
```
`-m` specifies the hash type (`1400` is `sha-256`).

Finally, we have the cracked hash:

`shaktictf{dachshund_aquamarine_974}`
