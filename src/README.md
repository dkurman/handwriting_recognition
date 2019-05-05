# Requirements

Guys, let's keep our repository clean!

In order to do that get acquanted with the general pipeline of the system below. 

Since each of us has his own task, contribute only to the corresponding directories. 

You are allowed to work in notebooks, but in the end you have to collect and properly strucutre all valuable code.  

Please, also start thinking of the integration!!! It is important!

## Pipeline:

1. **preprocessing** (horizontal alignment):
   * input:
        * raw image of an envelope
   * output:
        * horizontally aligned image
2. **text region detection**
   * input: 
        * pre-processed image
   * output: 
        * bbox of the sender
        * bbox of the receiver
3. **text segmentation**
   * input:
        * image of the text region
   * output:
        * list of words
4. **word recognition**
   * input:
        * image of a word
   * output:
        * class of the word