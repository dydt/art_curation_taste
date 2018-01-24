# Art Curation and Taste Prediction

I really enjoy looking at art.  When I heard about [artistic style transfer](https://arxiv.org/abs/1508.06576), I thought about how I could further understand art by applying deep learning.

I downloaded about 5000 images total from @womensart1 and @artpicschannel.  I labeled 1000 images from the former account with whether or not I liked it.  In this project, I try to 
1) predict which account an artwork comes from (and thus, which person or group curated it)
2) predict whether or not an artwork is to my personal taste

An example artwork from @womensart1 ("Comforter", Catherine Murphy):

<img src="https://pbs.twimg.com/media/DUDTButWsAE9LKw.jpg" width="300">

An example artwork from @artpicschannel ("The Red Tree House", Vincent Van Gogh):

<img src="https://pbs.twimg.com/media/DUQ4a5IXcAAuPXI.jpg" width="300">

Using fastai and what I learned in the [Practical Deep Learning](http://course.fast.ai/about.html) class, I trained CNNs using both ResNet-34 and VGG19 architectures to accomplish the aforementioned tasks.  With predicting curators, the CNNs reached 80% accuracy.  To put this into perspective, I, as a human who can tell that embroidered art was most likely done by a woman and that the prominent Impressionist painters were men, only achieved 85% accuracy.  This amazed me.

With predicting whether I'd like an artwork, the CNNs reached 81% accuracy. Again, this was very impressive to me.  I can't describe very well at all what commonalities the artworks I like have. 

For more details, please look at the jupyter notebook.  The labels folder are dinky adhoc scripts I used to help me label data very quickly and avoid any labeling cross-contamination.  (I labeled 1000 images from @womensart1 first, which means I knew they were posted from that account and thus could not include them in my curation benchmark.)

# Next Steps

Since I can't put my finger on what makes artworks I like so appealing, I'd love to learn what I can about my own taste from the CNNs I trained.  I read [Zeiler and Fergus](https://cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf) and I'd like to similarly visualize what causes high activations.

Also the unfrozen NNs overfit.  I know about tweaking drop-out as a solution, and I'd like to try that and learn other methods to prevent overfitting.