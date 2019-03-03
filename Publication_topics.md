# Potential publication topics

1. Survey on Text Recognition

2. Survey on Text Detection

3. Text Recognition based on pure CNN
	- Experiments with printed text 
		- it allows us to check the hypothesis of CNN on a simpler problem
		- it gives an optimal image size and the required number of training samples
	- Experiments with handwritten text
		- the starting point is the printed text estimates
		
4. Collection of Representative Training Dataset for Handwritten Address (HWA)
	- Main questions: 
		- how to reduce the number of respondents and still collect a representative dataset?
		- what is a representative training dataset for the HWA problem?
	- Idea:
		- collect both the entire target HW words and the HW letters
		- augment the HW letters (geometrical transformations)
		- combine the HW letters into target words
		- augment all
	- This includes: 
		- Analysis of HWT variations
		- Data collection
			- HW characters (letter variations)
			- HW words (char connection variations)
		- Data synthesis (augmentation)
			- augment the HW character dataset
			- combine the words from the set of HW letters
			- augment the entire words

5. Text Recognition based on RCNN (CNN+ BRNN+CTC decoder)
 