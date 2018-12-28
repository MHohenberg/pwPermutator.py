# pwPermutator

creates a list of lowercase/uppercase permutations on strings in an input file

For instance, "test" results in 

* test
* tesT
* teSt
* teST
* tEst
* tEsT
* tESt
* tEST
* Test
* TesT
* TeSt
* TeST
* TEst
* TEsT
* TEST

the script ignores non-alphabetic characters. 

As of now, diacrytic characters (like Umlauts) are ignored. 

## But why?

Well, mostly to help facilitate a brute-force attack against files for cases
in which a set of probable passwords is known, but the exact spelling is not.

Created after I forgot the PW to a secret key of mine. Helped a lot, too. 

If you want to use it for something else, be my guest. 

## This code is not very good.

Yes. it was created as a quick hack between two 
lectures during the 35C3. Improvements are welcome.


# To Do

- parametrize the script
- disable verbose move

# License 

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2018 Martin Hohenberg <me@martinhohenberg.de>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
