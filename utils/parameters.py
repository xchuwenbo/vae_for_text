class Parameters():
    # general parameters
    latent_size = 13  # std=13, inputless_dec(dec_keep_rate=0.0)=111
    num_epochs = 100
    learning_rate = 0.001
    batch_size = 50
    # for decoding
    temperature = 1.0
    gen_length = 40
    # beam search
    beam_search = False
    beam_size = 2
    # encoder
    rnn_layers = 1
    encoder_hidden = 350  # std=191, inputless_dec=350
    encode = 'hw' # 'hw' or 'mlp'
    # highway networks
    keep_rate = 1.0
    highway_lc = 2
    highway_ls = 600
    # decoder
    decoder_hidden = 350
    decoder_rnn_layers = 1
    dec_keep_rate = 0.62
    decode = 'hw' # can use 'hw', 'concat', 'mlp'
    # data
    datasets = ['GOT', 'PTB']
    embed_size = 353 # std=353, inputless_dec=499
    sent_max_size = 100
    input = datasets[1]
    debug = False
    vocab_drop = 3 # drop less than n times occured
    # use pretrained w2vec embeddings
    pre_trained_embed = True
    fine_tune_embed = True
    # technical parameters
    is_training = True
    LOG_DIR = './model_logs/'
    visualise = False
    # gru base cell partially implemented
    base_cell = 'lstm' # or GRU
    def parse_args(self):
        import argparse
        import os
        parser = argparse.ArgumentParser(
            description="Specify some parameters, all parameters "
            "also can be directly specified in Parameters class")
        parser.add_argument('--dataset', default=self.input,
                            help='training dataset (GOT or PTB)', dest='data')
        parser.add_argument('--lr', default=self.learning_rate,
                            help='learning rate', dest='lr')
        parser.add_argument('--embed_dim', default=self.embed_size,
                            help='embedding size', dest='embed')
        parser.add_argument('--lst_state_dim_enc', default=self.encoder_hidden,
                            help='encoder state size', dest='enc_hid')
        parser.add_argument('--lst_state_dim_dec', default=self.decoder_hidden,
                            help='decoder state size', dest='dec_hid')
        parser.add_argument('--latent', default=self.latent_size,
                            help='latent space size', dest='latent')
        parser.add_argument('--dec_dropout', default=self.dec_keep_rate,
                            help='decoder dropout keep rate', dest='dec_drop')
        parser.add_argument('--beam_search', default=self.beam_search,
                            action="store_true")
        parser.add_argument('--beam_size', default=self.beam_size)
        parser.add_argument('--decode', default=self.decode,
                            help='define mapping from z->lstm. mlp, concat, hw')
        parser.add_argument('--encode', default=self.encode,
                            help='define mapping from lstm->z. mlp, hw')
        parser.add_argument('--vocab_drop', default=self.vocab_drop,
                            help='drop less than')
        parser.add_argument('--gpu', help="specify GPU number")

        args = parser.parse_args()
        self.input = args.data
        self.learning_rate = float(args.lr)
        self.embed_size = int(args.embed)
        self.encoder_hidden = int(args.enc_hid)
        self.decoder_hidden = int(args.dec_hid)
        self.latent_size = int(args.latent)
        self.dec_keep_rate = float(args.dec_drop)
        self.beam_search = args.beam_search
        self.beam_size = int(args.beam_size)
        self.decode = args.decode
        self.encode = args.encode
        self.vocab_drop = int(args.vocab_drop)
        os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"]=args.gpu
