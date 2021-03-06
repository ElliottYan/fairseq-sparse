from entmax import Sparsemax

# code from https://github.com/deep-spin/S7/blob/main/joeynmt/better_sparsemax.py

class BetterSparsemax(Sparsemax):
    # This exists because of a bug in the entmax implementation of sparsemax
    def forward(self, x, *args, **kwargs):
        assert self.dim == -1
        bottled_x = x.view(-1, x.size(-1))
        return super().forward(bottled_x, *args, **kwargs).view_as(x)
