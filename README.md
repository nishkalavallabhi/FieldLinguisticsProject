# Field Linguistics Project

I am attending a Field Linguistics class taught by Dr Sinem Sonsaat at Iowa State University. In the first week of classes, we ran into this issue of different people transcribing  the same sound into different IPA transcriptions. I wondered if we can come up with a simple way to look for a closest match in IPA alphabet automatically. I thought OpenSmile is a good starting point - and thus, this project began.

Here are the steps I followed for now: 

Step 1: Get all mp3 files from [an IPA sounds repo](http://web.uvic.ca/ling/resources/ipa/charts/IPAlab/IPAsounds/) (wget)

Step 2: Convert them all to wav (mpg123)

Step 3: Extract audio features for all these wav files (OpenSmile)

Step 4: For a given wav file, return the most similar sounds from IPA based on distance between audio feature vectors (Python)

TODO:
- Take one sound, and possible IPA sounds (3 or 4 of them) which are related to this, and rank only those.
- Having a small GUI with drop-down for IPA sounds, so that non-Technically minded people can quickly use this. 
