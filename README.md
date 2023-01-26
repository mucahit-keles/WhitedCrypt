# WhitedCrypt

An encryption algorithm made by me from the ground up. This goes without saying, but I do **NOT** advise using this algorithm for encrypting any important data as the algorithm can't be considered secure enough. ***Just because it hasn't been cracked yet doesn't mean it won't be.***
I refuse to take any responsibility if any data you encrypt using this algorithm gets cracked.

Pull requests are welcome.

## How does it work?
There are mainly 4 functions:

**encode(*PlainText: string*):**
- Goes through each character in [PlainText].
- Gets the character's equivalent Unicode Number.
- Creates a [Unicode Order] (basically all the unicodes in one string) with separators (Example: "unicode1\unicode2\unicode3").
- Then, it goes through all the Unicode Numbers in the [Unicode Order].
- Replaces the characters with different whitespace characters, making the [Unicode Order] practically invisible.

**decode(*EncodedText: string*):**
- Does the opposite of encode.

**encrypt(*PlainText: string*, *Key: string*):**
- Hashes the key with SHA512.
- Creates a [Unicode Order] from the Hashed Key and maps each Unicode to different numbers. (Example: "123\123\123" would now be "78407840784". With the separator being a number (0) as well.)
- Creates a [Unicode Order] from the [PlainText] and maps each Unicode to different numbers. (Example: "123\123\123" would now be "78407840784". With the separator being a number (0) as well.)
* *Now that both the HashedKey and the PlainText are practically numbers now, we can do mathematical operations on them.*
- Adds the HashedKey to the PlainText (doesnt append it as a string, it literally adds it as a mathematical operation), which means you will need to subtract the Key to get the text itself. Which requires you to have the key.
- Maps the result with whitespaces using Unicode Order's and returns it

**decrypt(*EncryptedText: string*, *Key: string*):**
- Does the opposite of encrypt
