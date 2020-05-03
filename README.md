# StoreQ
StoreQ is a futuristic storage system that works by encoding classical data into quantum circuits.

# How it works
StoreQ can upload and retrieve information from a quantum computer using quantum circuits. This entire process is done by simulation of qbits and quantum processes on my personal computer(which is obviously not quantum). 

# Why it's special
I think this project has huge extensability beyond what I was able to do in a day. Here's a few:
* Because the storage media is via quantum circuits, we can use *entanglement* and *superposition* to represent all the data we accumulate into a single qbit superposition. [sorry for the jargon :(!] What it means is that we can represent a big chunk of information in a single quantum bit, and get the information we want from it by "measuring" it in certain ways.
* Because of the API I created to link the backend to the frontend, it can actually be triggered from your google home! Say: *Ok Google, ask StoreQ to launch demonstration*
* Because it's not all theory and jargon, with nothing to show. I'm proud to have implemented a working concept!


# What Inspired me
Art! I initially was thinking of a way to link quantum computing principles with art. Art led to images, and quantum computing led to quantum circuitry. And bam, the idea was born. 

# How I built it
The frontend is linked with the core backend via a python RESTful API using flask.
* The `Upload` button uploads the image (in greyscale, and resized to not overload my computer) to the quantum computer simulation.
* The `Download` button downloads the image by reconstructing the data from the probability distributions stored in the qbits.
![homepage](https://user-images.githubusercontent.com/17317792/80913338-79f55500-8d76-11ea-9208-25a3d7605f7c.png)

 This is how the backend core works. I'll go in steps:
* **Storage:**
* The data used here is an image. Each row's values are firstly one-hot encoded using a LabelBinarizer(a concept borrowed from machine learning), so that the vector amplitude sum is 1. This is a quantum constraint we have to follow.
* Each binarized vector is stored in a qbit array via initialization of the values, which is the basis of out quantum circuit.
![qbits](https://user-images.githubusercontent.com/17317792/80913326-68ac4880-8d76-11ea-8450-d10e35846671.png)
* **Recovery**
* the array of quantum circuits and the `LabelBinarizer` objects are used to recover each vector.
* The vectors are converted to numbers. 
* The numbers  form the matrix, which Is the resultant image.




# What I learnt
This was really, really, really fun. I learnt so much about how quantum computers work and was able to actually apply it to an idea that interested me. What gives me even more excitement is the possibilities this holds, that I haven't implemented yet due to time constraints.
I learnt about the current quantum computing ecosystem and what tools researchers in the field use. I also got to whip up a quick web frontend for it, which I was also proud to learn and implement.
Also, shoutout to my roommate for explaining to me fundamentals of quantum computing when my brain hurt from trying to understand too much at once. Like, a lot. He's got a bright future.



# References:
* Fixing weird LabelBinarizer with [a custom class](https://stackoverflow.com/questions/31947140/sklearn-labelbinarizer-returns-vector-when-there-are-2-classes)
* [Quantum Circuits!](https://towardsdatascience.com/building-your-own-quantum-circuits-in-python-e9031b548fa7)
* [Quantum physics and art](https://artdesign.unsw.edu.au/whats-on/news/quantum-physicists-take-art-class-rethink-their-view-reality)
* [Representing qbit states](https://qiskit.org/textbook/ch-states/representing-qubit-states.html)
* [css font generator](https://html-css-js.com/css/generator/font/)
# References:
* Fixing weird LabelBinarizer with [a custom class](https://stackoverflow.com/questions/31947140/sklearn-labelbinarizer-returns-vector-when-there-are-2-classes)
* [Quantum Circuits!](https://towardsdatascience.com/building-your-own-quantum-circuits-in-python-e9031b548fa7)
* [Quantum physics and art](https://artdesign.unsw.edu.au/whats-on/news/quantum-physicists-take-art-class-rethink-their-view-reality)
* [Representing qbit states](https://qiskit.org/textbook/ch-states/representing-qubit-states.html)
* [css font generator](https://html-css-js.com/css/generator/font/)