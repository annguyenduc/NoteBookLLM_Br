---
title: "Attention (machine learning) - Wikipedia"
source_url: "https://en.wikipedia.org/wiki/Attention_mechanism"
scraped_at: "88773.703"
engine: "Lightpanda (via Playwright)"
audit:
  score: 1.00
  date: "2026-05-12"
  status: "PASSED"
  auditor: "v1.0"
  verify_result: "SKIPPED"
  verify_gaps: []
---
# Attention (machine learning) - Wikipedia

Source: https://en.wikipedia.org/wiki/Attention_mechanism

## Content

Jump to content
Main menu
Search
Donate
Create account
Log in
Contents hide
(Top)
History
Overview
Toggle Overview subsection
Interpreting attention weights
Variants
Optimizations
Toggle Optimizations subsection
Flash attention
FlexAttention
Applications
Toggle Applications subsection
Attention maps as explanations for vision transformers
Mathematical representation
Toggle Mathematical representation subsection
Standard scaled dot-product attention
Masked attention
Multi-head attention
Bahdanau (additive) attention
Luong attention (general)
Self-attention
Masking
See also
References
External links
Attention (machine learning)
15 languages
Article
Talk
Read
Edit
View history
Tools
Appearance hide
Text
Small
Standard
Large
Width
Standard
Wide
Color
Automatic
Light
Dark
From Wikipedia, the free encyclopedia
(Redirected from Attention mechanism)
Part of a series on
Machine learning
and data mining

show
Paradigms


show
Problems


show
Supervised learning
(classification • regression)


show
Clustering


show
Dimensionality reduction


show
Structured prediction


show
Anomaly detection


show
Neural networks


show
Reinforcement learning


show
Learning with humans


show
Model diagnostics


show
Mathematical foundations


show
Journals and conferences


show
Related articles

vte
Attention mechanism, overview

In machine learning, attention is a method that determines the importance of each component in a sequence relative to the other components in that sequence. In natural language processing, importance is represented by "soft" weights assigned to each word in a sentence. More generally, attention encodes vectors called token embeddings across a fixed-width sequence that can range from tens to millions of tokens in size.

Unlike "hard" weights, which are computed during the backwards training pass, "soft" weights exist only in the forward pass and therefore change with every step of the input. Earlier designs implemented the attention mechanism in a serial recurrent neural network (RNN) language translation system, but a more recent design, namely the transformer, removed the slower sequential RNN and relied more heavily on the faster parallel attention scheme.

Inspired by ideas about attention in humans, the attention mechanism was developed to address the weaknesses of using information from the hidden layers of recurrent neural networks. Recurrent neural networks favor more recent information contained in words at the end of a sentence, while information earlier in the sentence tends to be attenuated. Attention allows a token equal access to any part of a sentence directly, rather than only through the previous state.

History[edit]
See also: Timeline of machine learning
1950s–1960s	Psychology and biology of attention. Cocktail party effect[1] — focusing on content by filtering out background noise. Filter model of attention,[2] partial report paradigm, and saccade control.[3]
1980s	Sigma-pi units,[4] higher-order neural networks.
1990s	Fast weight controllers and dynamic links between neurons, anticipating key-value mechanisms in attention.[5][6][7][8]
1998	The bilateral filter was introduced in image processing. It uses pairwise affinity matrices to propagate relevance across elements.[9]
2005	Non-local means extended affinity-based filtering in image denoising, using Gaussian similarity kernels as fixed attention-like weights.[10]
2014	seq2seq with RNN + Attention.[11] Attention was introduced to enhance RNN encoder-decoder translation, particularly for long sentences. See Overview section.

Attentional Neural Networks introduced a learned feature selection mechanism using top-down cognitive modulation, showing how attention weights can highlight relevant inputs.[12]


2015	Attention was extended to vision for image captioning tasks.[13][14]
2016	Self-attention was integrated into RNN-based models to capture intra-sequence dependencies.[15][16]

Self-attention was explored in decomposable attention models for natural language inference[17] and structured self-attentive sentence embeddings.[18]


2017	The Transformer architecture introduced in the research paper Attention is All You Need[19] formalized scaled dot-product self-attention:
𝐴
=
softmax
(
𝑄
𝐾
𝑇
𝑑
𝑘
)
𝑉

Relation networks[20] and set Transformers[21] applied attention to unordered sets and relational reasoning, generalizing pairwise interaction models.


2018	Non-local neural networks[22] extended attention to computer vision by capturing long-range dependencies in space and time. Graph attention networks[23] applied attention mechanisms to graph-structured data.
2019–2020	Efficient Transformers, including Reformer,[24] Linformer,[25] and Performer,[26] introduced scalable approximations of attention for long sequences.
2019+	Hopfield networks were reinterpreted as associative memory-based attention systems,[27] and vision transformers (ViTs) achieved competitive results in image classification.[28]

Transformers were adopted across scientific domains, including AlphaFold for protein folding,[29] CLIP for vision-language pretraining,[30] and attention-based dense segmentation models like CCNet[31] and DANet.[32]

Additional surveys of the attention mechanism in deep learning are provided by Niu et al.[33] and Soydaner.[34]

The major breakthrough came with self-attention, where each element in the input sequence attends to all others, enabling the model to capture global dependencies. This idea was central to the Transformer architecture, which replaced recurrence with attention mechanisms. As a result, Transformers became the foundation for models like BERT, T5 and generative pre-trained transformers (GPT).[19]

Overview[edit]
	
This article may contain original research. Please improve it by verifying the claims made and adding inline citations. Statements consisting only of original research should be removed. (June 2025) (Learn how and when to remove this message)

The modern era of machine attention was revitalized by grafting an attention mechanism (Fig 1. orange) to an Encoder-Decoder.[citation needed]

Animated sequence of language translation
	
Fig 1. Encoder-decoder with attention.[35] Numerical subscripts (100, 300, 500, 9k, 10k) indicate vector sizes while lettered subscripts i and i − 1 indicate time steps. Pinkish regions in H matrix and w vector are zero values. See Legend for details.
Legend show

Figure 2 shows the internal step-by-step operation of the attention block (A) in Fig 1.

Figure 2. The diagram shows the attention forward pass calculating correlations of the word "that" with other words in "See that girl run." Given the right weights from training, the network should be able to identify "girl" as a highly correlated word. Some things to note:
This example focuses on the attention of a single word "that". In practice, the attention of each word is calculated in parallel to speed up calculations. Simply changing the lowercase "x" vector to the uppercase "X" matrix will yield the formula for this.
Softmax scaling qWkT / √100 prevents a high variance in qWkT that would allow a single word to excessively dominate the softmax resulting in attention to only one word, as a discrete hard max would do.
Notation: the commonly written row-wise softmax formula above assumes that vectors are rows, which runs contrary to the standard math notation of column vectors. More correctly, we should take the transpose of the context vector and use the column-wise softmax, resulting in the more correct form
(
𝑋
𝑊
𝑣
)
𝑇
∗
[
(
𝑊
𝑘
𝑋
𝑇
)
∗
(
𝑥
_
𝑊
𝑞
)
𝑇
]
𝑠
𝑚
.
Interpreting attention weights[edit]

In translating between languages, alignment is the process of matching words from the source sentence to words of the translated sentence. Networks that perform verbatim translation without regard to word order would show the highest scores along the (dominant) diagonal of the matrix. The off-diagonal dominance shows that the attention mechanism is more nuanced.

Consider an example of translating I love you to French. On the first pass through the decoder, 94% of the attention weight is on the first English word I, so the network offers the word je. On the second pass of the decoder, 88% of the attention weight is on the third English word you, so it offers t'. On the last pass, 95% of the attention weight is on the second English word love, so it offers aime.

In the I love you example, the second word love is aligned with the third word aime. Stacking soft row vectors together for je, t', and aime yields an alignment matrix:

	I	love	you
je	0.94	0.02	0.04
t'	0.11	0.01	0.88
aime	0.03	0.95	0.02

Sometimes, alignment can be multiple-to-multiple. For example, the English phrase look it up corresponds to cherchez-le. Thus, "soft" attention weights work better than "hard" attention weights (setting one attention weight to 1, and the others to 0), as we would like the model to make a context vector consisting of a weighted sum of the hidden vectors, rather than "the best one", as there may not be a best hidden vector.

Variants[edit]
Comparison of the data flow in CNN, RNN, and self-attention

Many variants of attention implement soft weights, such as

fast weight programmers, or fast weight controllers (1992).[5] A "slow" neural network outputs the "fast" weights of another neural network through outer products. The slow network learns by gradient descent. It was later renamed as "linearized self-attention".[37]
Bahdanau-style attention,[11] also referred to as additive attention,
Luong-style attention,[38] which is known as multiplicative attention,
Early attention mechanisms similar to modern self-attention were proposed using recurrent neural networks. However, the highly parallelizable self-attention was introduced in 2017 and successfully used in the Transformer model,
positional attention and factorized positional attention.[39]

For convolutional neural networks, attention mechanisms can be distinguished by the dimension on which they operate, namely: spatial attention,[40] channel attention,[41] or combinations.[42][43]

These variants recombine the encoder-side inputs to redistribute those effects to each target output. Often, a correlation-style matrix of dot products provides the re-weighting coefficients. In the figures below, W is the matrix of context attention weights, similar to the formula in Overview section above.

1. encoder-decoder dot product	2. encoder-decoder QKV	3. encoder-only dot product	4. encoder-only QKV	5. Pytorch tutorial

Both encoder & decoder are needed to calculate attention.[38]
	
Both encoder & decoder are needed to calculate attention.[44]
	
Decoder is not used to calculate attention. With only 1 input into corr, W is an auto-correlation of dot products. wij = xi xj.[45]
	
Decoder is not used to calculate attention.[46]
	
A fully-connected layer is used to calculate attention instead of dot product correlation.[47]
Legend show
Optimizations[edit]
Flash attention[edit]

The size of the attention matrix is proportional to the square of the number of input tokens. Therefore, when the input is long, calculating the attention matrix requires a lot of GPU memory. Flash attention is an implementation that reduces the memory needs and increases efficiency without sacrificing accuracy. It achieves this by partitioning the attention computation into smaller blocks that fit into the GPU's faster on-chip memory, reducing the need to store large intermediate matrices and thus lowering memory usage while increasing computational efficiency.[48]

FlexAttention[edit]

FlexAttention[49] is an attention kernel developed by Meta that allows users to modify attention scores prior to softmax and dynamically chooses the optimal attention algorithm.

Applications[edit]

Attention is widely used in natural language processing, computer vision, and speech recognition. In NLP, it improves context understanding in tasks like question answering and summarization. In vision, visual attention helps models focus on relevant image regions, enhancing object detection and image captioning.

Attention maps as explanations for vision transformers[edit]
See also: Saliency map and Mechanistic interpretability

From the original paper on vision transformers (ViT), visualizing attention scores as a heat map (called saliency maps or attention maps) has become an important and routine way to inspect the decision making process of ViT models.[50] One can compute the attention maps with respect to any attention head at any layer, while the deeper layers tend to show more semantically meaningful visualization. Attention rollout is a recursive algorithm to combine attention scores across all layers, by computing the dot product of successive attention maps.[51]

Because vision transformers are typically trained in a self-supervised manner, attention maps are generally not class-sensitive. When a classification head is attached to the ViT backbone, class-discriminative attention maps (CDAM) combines attention maps and gradients with respect to the class [CLS] token.[52] Some class-sensitive interpretability methods originally developed for convolutional neural networks can be also applied to ViT, such as GradCAM, which back-propagates the gradients to the outputs of the final attention layer.[53]

Using attention as basis of explanation for the transformers in language and vision is not without debate. While some pioneering papers analyzed and framed attention scores as explanations,[54][55] higher attention scores do not always correlate with greater impact on model performances.[56]

Mathematical representation[edit]
Standard scaled dot-product attention[edit]

For matrices: 
𝑄
∈
𝑅
𝑚
×
𝑑
𝑘
,
𝐾
∈
𝑅
𝑛
×
𝑑
𝑘
 and 
𝑉
∈
𝑅
𝑛
×
𝑑
𝑣
, the scaled dot-product, or QKV attention, is defined as:
Attention
(
𝑄
,
𝐾
,
𝑉
)
=
softmax
(
𝑄
𝐾
𝑇
𝑑
𝑘
)
𝑉
∈
𝑅
𝑚
×
𝑑
𝑣
where 
𝑇
 denotes transpose and the softmax function is applied independently to every row of its argument. The matrix 
𝑄
 contains 
𝑚
 queries, while matrices 
𝐾
,
𝑉
 jointly contain an unordered set of 
𝑛
 key-value pairs. Value vectors in matrix 
𝑉
 are weighted using the weights resulting from the softmax operation, so that the rows of the 
𝑚
-by-
𝑑
𝑣
 output matrix are confined to the convex hull of the points in 
𝑅
𝑑
𝑣
 given by the rows of 
𝑉
.

To understand the permutation invariance and permutation equivariance properties of QKV attention,[57] let 
𝐴
∈
𝑅
𝑚
×
𝑚
 and 
𝐵
∈
𝑅
𝑛
×
𝑛
 be permutation matrices; and 
𝐷
∈
𝑅
𝑚
×
𝑛
 an arbitrary matrix. The softmax function is permutation equivariant in the sense that:
softmax
(
𝐴
𝐷
𝐵
)
=
𝐴
softmax
(
𝐷
)
𝐵
By noting that the transpose of a permutation matrix is also its inverse, it follows that:
Attention
(
𝐴
𝑄
,
𝐵
𝐾
,
𝐵
𝑉
)
=
𝐴
Attention
(
𝑄
,
𝐾
,
𝑉
)
which shows that QKV attention is equivariant with respect to re-ordering the queries (rows of 
𝑄
); and invariant to re-ordering of the key-value pairs in 
𝐾
,
𝑉
. These properties are inherited when applying linear transforms to the inputs and outputs of QKV attention blocks. For example, a simple self-attention function defined as:
𝑋
↦
Attention
(
𝑋
𝑇
𝑞
,
𝑋
𝑇
𝑘
,
𝑋
𝑇
𝑣
)
is permutation equivariant with respect to re-ordering the rows of the input matrix 
𝑋
 in a non-trivial way, because every row of the output is a function of all the rows of the input. Similar properties hold for multi-head attention, which is defined below.

Masked attention[edit]

When QKV attention is used as a building block for an autoregressive decoder, and when at training time all input and output matrices have 
𝑛
 rows, a masked attention variant is used:
Attention
(
𝑄
,
𝐾
,
𝑉
)
=
softmax
(
𝑄
𝐾
𝑇
𝑑
𝑘
+
𝑀
)
𝑉
where the mask, 
𝑀
∈
𝑅
𝑛
×
𝑛
 is a strictly upper triangular matrix, with zeros on and below the diagonal and 
−
∞
 in every element above the diagonal. The softmax output, also in 
𝑅
𝑛
×
𝑛
 is then lower triangular, with zeros in all elements above the diagonal. The masking ensures that for all 
1
≤
𝑖
<
𝑗
≤
𝑛
, row 
𝑖
 of the attention output is independent of row 
𝑗
 of any of the three input matrices. The permutation invariance and equivariance properties of standard QKV attention do not hold for the masked variant.

Multi-head attention[edit]
Decoder multiheaded cross-attention

Multi-head attention
MultiHead
(
𝑄
,
𝐾
,
𝑉
)
=
Concat
(
head
1
,
.
.
.
,
head
ℎ
)
𝑊
𝑂
where each head is computed with QKV attention as:
head
𝑖
=
Attention
(
𝑄
𝑊
𝑖
𝑄
,
𝐾
𝑊
𝑖
𝐾
,
𝑉
𝑊
𝑖
𝑉
)
and 
𝑊
𝑖
𝑄
,
𝑊
𝑖
𝐾
,
𝑊
𝑖
𝑉
, and 
𝑊
𝑂
 are parameter matrices.

The permutation properties of (standard, unmasked) QKV attention apply here also. For permutation matrices, 
𝐴
,
𝐵
:
MultiHead
(
𝐴
𝑄
,
𝐵
𝐾
,
𝐵
𝑉
)
=
𝐴
MultiHead
(
𝑄
,
𝐾
,
𝑉
)
from which we also see that multi-head self-attention:
𝑋
↦
MultiHead
(
𝑋
𝑇
𝑞
,
𝑋
𝑇
𝑘
,
𝑋
𝑇
𝑣
)
is equivariant with respect to re-ordering of the rows of input matrix 
𝑋
.

Bahdanau (additive) attention[edit]

Attention
(
𝑄
,
𝐾
,
𝑉
)
=
softmax
(
tanh
⁡
(
𝑊
𝑄
𝑄
+
𝑊
𝐾
𝐾
)
)
𝑉
where 
𝑊
𝑄
 and 
𝑊
𝐾
 are learnable weight matrices.[11]

Luong attention (general)[edit]

Attention
(
𝑄
,
𝐾
,
𝑉
)
=
softmax
(
𝑄
𝑊
𝐾
𝑇
)
𝑉
where 
𝑊
 is a learnable weight matrix.[38]

Self-attention[edit]

Self-attention is essentially the same as cross-attention, except that query, key, and value vectors all come from the same model. Both encoder and decoder can use self-attention, but with subtle differences.

For encoder self-attention, we can start with a simple encoder without self-attention, such as an "embedding layer", which simply converts each input word into a vector by a fixed lookup table. This gives a sequence of hidden vectors 
ℎ
0
,
ℎ
1
,
…
. These can then be applied to a dot-product attention mechanism, to obtain
ℎ
0
′
	
=
A
t
t
e
n
t
i
o
n
(
ℎ
0
𝑊
𝑄
,
𝐻
𝑊
𝐾
,
𝐻
𝑊
𝑉
)


ℎ
1
′
	
=
A
t
t
e
n
t
i
o
n
(
ℎ
1
𝑊
𝑄
,
𝐻
𝑊
𝐾
,
𝐻
𝑊
𝑉
)

	
⋮
or more succinctly, 
𝐻
′
=
A
t
t
e
n
t
i
o
n
(
𝐻
𝑊
𝑄
,
𝐻
𝑊
𝐾
,
𝐻
𝑊
𝑉
)
. This can be applied repeatedly, to obtain a multilayered encoder. This is the "encoder self-attention", sometimes called the "all-to-all attention", as the vector at every position can attend to every other.

Masking[edit]
Decoder self-attention with causal masking, detailed diagram

For decoder self-attention, all-to-all attention is inappropriate, because during the autoregressive decoding process, the decoder cannot attend to future outputs that has yet to be decoded. This can be solved by forcing the attention weights 
𝑤
𝑖
𝑗
=
0
 for all 
𝑖
<
𝑗
, called "causal masking". This attention mechanism is the "causally masked self-attention".

See also[edit]
Recurrent neural network
seq2seq
Transformer (deep learning architecture)
Attention
Dynamic neural network
References[edit]
^ Cherry, E. Colin (1953). "Some Experiments on the Recognition of Speech, with One and with Two Ears". The Journal of the Acoustical Society of America. 25 (5): 975–979. Bibcode:1953ASAJ...25..975C. doi:10.1121/1.1907229. hdl:11858/00-001M-0000-002A-F750-3.
^ Broadbent, Donald E. (1958). Perception and Communication. Pergamon Press.
^ Kowler, Eileen (1995). "The control of saccadic eye movements". Reviews of Oculomotor Research. 5: 1–70.
^ Rumelhart, David E.; Hinton, G. E.; Mcclelland, James L. (1987-07-29). "A General Framework for Parallel Distributed Processing" (PDF). In Rumelhart, David E.; Hinton, G. E.; PDP Research Group (eds.). Parallel Distributed Processing, Volume 1: Explorations in the Microstructure of Cognition: Foundations. Cambridge, Massachusetts: MIT Press. ISBN 978-0-262-68053-0.
^ 
Jump up to:
a b Schmidhuber, Jürgen (1992). "Learning to control fast-weight memories: an alternative to recurrent nets". Neural Computation. 4 (1): 131–139. doi:10.1162/neco.1992.4.1.131. S2CID 16683347.
^ von der Malsburg, Christoph (1981). "The correlation theory of brain function". Internal Report 81–2, Max-Planck-Institute for Biophysical Chemistry.
^ Feldman, Jerome A. (1982). "Dynamic connections in neural networks". Biological Cybernetics. 46 (1): 27–39. doi:10.1007/BF00335349. PMID 6307398.
^ Hinton, Geoffrey E. (1989). "Connectionist learning procedures". Artificial Intelligence. 40 (1–3): 185–234. doi:10.1016/0004-3702(89)90049-0.
^ Tomasi, Carlo (1998). Bilateral filtering for gray and color images. ICCV.
^ Buades, Antoni (2005). A non-local algorithm for image denoising. CVPR.
^ 
Jump up to:
a b c Bahdanau, Dzmitry; Cho, Kyunghyun; Bengio, Yoshua (2014). "Neural Machine Translation by Jointly Learning to Align and Translate". arXiv:1409.0473 [cs.CL].
^ Wang, Qian (2014). Attentional Neural Network: Feature Selection Using Cognitive Feedback. NeurIPS.
^ Xu, Kelvin; Ba, Jimmy; Kiros, Ryan (2015). Show, Attend and Tell: Neural Image Caption Generation with Visual Attention. arXiv:1502.03044.
^ Vinyals, Oriol; Toshev, Alexander; Bengio, Samy; Erhan, Dumitru (2015). "Show and Tell: A Neural Image Caption Generator". 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). pp. 3156–3164. doi:10.1109/CVPR.2015.7298935. ISBN 978-1-4673-6964-0.
^ Cheng, Jianpeng (2016). "Long Short-Term Memory-Networks for Machine Reading". arXiv:1601.06733 [cs.CL].
^ Paulus, Romain (2017). "A Deep Reinforced Model for Abstractive Summarization". arXiv:1705.04304 [cs.CL].
^ Parikh, Anees (2016). Decomposable Attention Model for Natural Language Inference. EMNLP. arXiv:1606.01933.
^ Lin, Zichao (2017). A Structured Self-Attentive Sentence Embedding. ICLR. arXiv:1703.03130.
^ 
Jump up to:
a b Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; Uszkoreit, Jakob; Jones, Llion; Gomez, Aidan N.; Kaiser, Lukasz; Polosukhin, Illia (2017). "Attention is All You Need". arXiv:1706.03762 [cs.CL].
^ Santoro, Adam (2017). Relation Networks for Relational Reasoning. ICLR. arXiv:1706.01427.
^ Lee, Juho (2019). Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks. ICML. arXiv:1810.00825.
^ Wang, Xiaolong (2018). Non-Local Neural Networks. CVPR.
^ Veličković, Petar (2018). Graph Attention Networks. ICLR.
^ Kitaev, Nikita (2020). Reformer: The Efficient Transformer. ICLR. arXiv:2001.04451.
^ Wang, Salah (2020). Linformer: Self-Attention with Linear Complexity. ICLR. arXiv:2006.04768.
^ Choromanski, Krzysztof (2020). Rethinking Attention with Performers. ICLR. arXiv:2009.14794.
^ Ramsauer, Johannes (2021). Hopfield Networks is All You Need. NeurIPS. arXiv:2008.02217.
^ Dosovitskiy, Aleksander (2021). An Image is Worth 16×16 Words: Transformers for Image Recognition at Scale. ICLR. arXiv:2010.11929.
^ Jumper, John (2021). "Highly accurate protein structure prediction with AlphaFold". Nature. 596 (7873): 583–589. Bibcode:2021Natur.596..583J. doi:10.1038/s41586-021-03819-2. PMC 8371605. PMID 34265844.
^ Radford, Alec (2021). Learning Transferable Visual Models from Natural Language Supervision. ICML.
^ Huang, Xiangyu (2019). CCNet: Criss-Cross Attention for Semantic Segmentation. ICCV. arXiv:1811.11721.
^ Fu, Jing (2019). Dual Attention Network for Scene Segmentation. CVPR. arXiv:1809.02983.
^ Niu, Zhaoyang; Zhong, Guoqiang; Yu, Hui (2021-09-10). "A review on the attention mechanism of deep learning". Neurocomputing. 452: 48–62. doi:10.1016/j.neucom.2021.03.091. ISSN 0925-2312.
^ Soydaner, Derya (August 2022). "Attention mechanism in neural networks: where it comes and where it goes". Neural Computing and Applications. 34 (16): 13371–13385. arXiv:2204.13154. doi:10.1007/s00521-022-07366-3. ISSN 0941-0643.
^ Britz, Denny; Goldie, Anna; Luong, Minh-Thanh; Le, Quoc (2017-03-21). "Massive Exploration of Neural Machine Translation Architectures". arXiv:1703.03906 [cs.CV].
^ "Pytorch.org seq2seq tutorial". Retrieved December 2, 2021.
^ Schlag, Imanol; Irie, Kazuki; Schmidhuber, Jürgen (2021). "Linear Transformers Are Secretly Fast Weight Programmers". ICML 2021. Springer. pp. 9355–9366.
^ 
Jump up to:
a b c Luong, Minh-Thang (2015-09-20). "Effective Approaches to Attention-Based Neural Machine Translation". arXiv:1508.04025v5 [cs.CL].
^ Luo, Fan; Zhang, Juan; Xu, Shenghui (3 July 2024). "Learning Positional Attention for Sequential Recommendation". catalyzex.com.
^ Zhu, Xizhou; Cheng, Dazhi; Zhang, Zheng; Lin, Stephen; Dai, Jifeng (2019). "An Empirical Study of Spatial Attention Mechanisms in Deep Networks". 2019 IEEE/CVF International Conference on Computer Vision (ICCV). pp. 6687–6696. arXiv:1904.05873. doi:10.1109/ICCV.2019.00679. ISBN 978-1-7281-4803-8. S2CID 118673006.
^ Hu, Jie; Shen, Li; Sun, Gang (2018). "Squeeze-and-Excitation Networks". 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 7132–7141. arXiv:1709.01507. doi:10.1109/CVPR.2018.00745. ISBN 978-1-5386-6420-9. S2CID 206597034.
^ Woo, Sanghyun; Park, Jongchan; Lee, Joon-Young; Kweon, In So (2018-07-18). "CBAM: Convolutional Block Attention Module". arXiv:1807.06521 [cs.CV].
^ Georgescu, Mariana-Iuliana; Ionescu, Radu Tudor; Miron, Andreea-Iuliana; Savencu, Olivian; Ristea, Nicolae-Catalin; Verga, Nicolae; Khan, Fahad Shahbaz (2022-10-12). "Multimodal Multi-Head Convolutional Attention with Various Kernel Sizes for Medical Image Super-Resolution". arXiv:2204.04218 [eess.IV].
^ Neil Rhodes (2021). CS 152 NN—27: Attention: Keys, Queries, & Values. Event occurs at 06:30. Retrieved 2021-12-22.
^ Alfredo Canziani & Yann Lecun (2021). NYU Deep Learning course, Spring 2020. Event occurs at 05:30. Retrieved 2021-12-22.
^ Alfredo Canziani & Yann Lecun (2021). NYU Deep Learning course, Spring 2020. Event occurs at 20:15. Retrieved 2021-12-22.
^ Robertson, Sean. "NLP From Scratch: Translation With a Sequence To Sequence Network and Attention". pytorch.org. Retrieved 2021-12-22.
^ Mittal, Aayush (2024-07-17). "Flash Attention: Revolutionizing Transformer Efficiency". Unite.AI. Retrieved 2024-11-16.
^ "FlexAttention: The Flexibility of PyTorch with the Performance of FlashAttention – PyTorch".
^ Dosovitskiy, Alexey; Beyer, Lucas; Kolesnikov, Alexander; Weissenborn, Dirk; Zhai, Xiaohua; Unterthiner, Thomas; Dehghani, Mostafa; Minderer, Matthias; Heigold, Georg (2021-06-03), An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale, arXiv:2010.11929
^ Abnar, Samira; Zuidema, Willem (2020-05-31), Quantifying Attention Flow in Transformers, arXiv:2005.00928
^ Brocki, Lennart; Binda, Jakub; Chung, Neo Christopher (2024-10-25), Class-Discriminative Attention Maps for Vision Transformers, arXiv:2312.02364
^ Gildenblat, Jacob (2025-07-21), jacobgil/pytorch-grad-cam, retrieved 2025-07-21
^ Mullenbach, James; Wiegreffe, Sarah; Duke, Jon; Sun, Jimeng; Eisenstein, Jacob (2018-04-16), Explainable Prediction of Medical Codes from Clinical Text, arXiv:1802.05695
^ Bahdanau, Dzmitry; Cho, Kyunghyun; Bengio, Yoshua (2016-05-19), Neural Machine Translation by Jointly Learning to Align and Translate, arXiv:1409.0473
^ Serrano, Sofia; Smith, Noah A. (2019-06-09), Is Attention Interpretable?, arXiv:1906.03731
^ Lee, Juho; Lee, Yoonho; Kim, Jungtaek; Kosiorek, Adam R; Choi, Seungjin; Teh, Yee Whye (2018). "Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks". arXiv:1810.00825 [cs.LG].
External links[edit]
Olah, Chris; Carter, Shan (September 8, 2016). "Attention and Augmented Recurrent Neural Networks". Distill. 1 (9). Distill Working Group. doi:10.23915/distill.00001.
Dan Jurafsky and James H. Martin (2022). Speech and Language Processing (3rd ed. draft, January 2022) — Chapter 10.4 (Attention) and Chapter 9.7 (Self-Attention Networks: Transformers)
Alex Graves (2020). Attention and Memory in Deep Learning — video lecture from DeepMind / UCL
show
vte
Artificial intelligence (AI)


Category: Machine learning
This page was last edited on 6 April 2026, at 05:21 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policy
About Wikipedia
Disclaimers
Contact Wikipedia
Legal & safety contacts
Code of Conduct
Developers
Statistics
Cookie statement
Mobile view

---
## Raw Source Metadata
- URL: https://en.wikipedia.org/wiki/Attention_mechanism
- Title: Attention (machine learning) - Wikipedia
