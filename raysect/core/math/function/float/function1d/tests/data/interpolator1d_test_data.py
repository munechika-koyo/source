import numpy as np


class TestInterpolatorLoadValues:
    """
    Base class for loading values for a 1D sin function test.

    Storage for interpolation and extrapolation data to be test against.
    These data are saved to 12 significant figures. self.data is generated by applying the sin function to an
    (NB_X = 10) 1D data set, which is used as the spline knots. The precalc_interpolation
    is setup for cubic, and linear interpolation are compared to functions equivalent functions from scipy
    version 1.6.3. In 1D, all extrapolation values are independent of the interpolator types. For uneven spacing, cubic
    data is tested against the current implementation.
    """
    def __init__(self):
        # Define in setup_cubic or setup_linear.
        self.precalc_interpolation = None

        #: Array holding precalculated nearest neighbour extrapolation data.
        self.precalc_extrapolation_nearest: np.array = None

        #: Array holding precalculated linear extrapolation data.
        self.precalc_extrapolation_linear: np.array = None

        #: Array holding precalculated quadratic extrapolation data.
        self.precalc_extrapolation_quadratic: np.array = None


class TestInterpolatorLoadNormalValues(TestInterpolatorLoadValues):
    """
    Loading values for the original np.sin(x) tests.

    For description of data storage, see TestInterpolatorLoadValues.
    """
    def __init__(self):
        super().__init__()
        #: data array from a function sampled on self.x. dtype should be np.float64.
        self.data: np.array = np.array(
            [0.000000000000E+00, 1.108826285100E-01, 2.203977434561E-01, 3.271946967962E-01, 4.299563635284E-01,
             5.274153857719E-01, 6.183698030697E-01, 7.016978761467E-01, 7.763719213007E-01, 8.414709848079E-01],
            dtype=np.float64
        )

        #: array holding precalculated nearest neighbour extrapolation data.
        self.precalc_extrapolation_nearest: np.array = np.array(
            [0.000000000000E+00, 0.000000000000E+00, 0.000000000000E+00, 8.414709848079E-01,
             8.414709848079E-01, 8.414709848079E-01], dtype=np.float64
        )

        #: array holding precalculated linear extrapolation data.
        self.precalc_extrapolation_linear: np.array = np.array(
            [-1.995887313179E+00, -1.330591542119E+00, -6.652957710597E-01, 1.232065365851E+00,
             1.622659746895E+00, 2.013254127938E+00], dtype=np.float64
        )
        #: array holding precalculated quadratic extrapolation data.
        self.precalc_extrapolation_quadratic: np.array = np.array(
            [-2.106655911846E+00, -1.379822030416E+00, -6.776033931338E-01, 1.145890531031E+00,
             1.277960407614E+00, 1.237680614556E+00], dtype=np.float64
        )

    def setup_cubic(self):
        self.precalc_interpolation = np.array(
            [0.000000000000E+00, 3.445726766897E-02, 6.892361882629E-02, 1.032764263792E-01,
             1.374723672762E-01, 1.715660220877E-01, 2.054427374305E-01, 2.390211362762E-01,
             2.723736467104E-01, 3.054074932289E-01, 3.380184236890E-01, 3.702697865700E-01,
             4.021030314403E-01, 4.334059817503E-01, 4.642087324270E-01, 4.944967727547E-01,
             5.241623210482E-01, 5.531868543036E-01, 5.816021511759E-01, 6.093090034050E-01,
             6.362532436612E-01, 6.624890560875E-01, 6.879357356812E-01, 7.125198048495E-01,
             7.362936780787E-01, 7.592034615909E-01, 7.811477131101E-01, 8.017642725164E-01,
             8.215858285263E-01, 8.414709848079E-01], dtype=np.float64
        )

    def setup_linear(self):
        self.precalc_interpolation = np.array(
            [0.000000000000E+00, 3.441185022723E-02, 6.882370045445E-02, 1.032355506817E-01,
             1.373173114280E-01, 1.713047608940E-01, 2.052922103601E-01, 2.388110112734E-01,
             2.719548933444E-01, 3.050987754155E-01, 3.378252140443E-01, 3.697167657888E-01,
             4.016083175333E-01, 4.333170194678E-01, 4.635629229227E-01, 4.938088263776E-01,
             5.240547298324E-01, 5.525062595092E-01, 5.807334924637E-01, 6.089607254182E-01,
             6.356100940512E-01, 6.614705305234E-01, 6.873309669955E-01, 7.119977444438E-01,
             7.351724481123E-01, 7.583471517807E-01, 7.808615118874E-01, 8.010646695275E-01,
             8.212678271677E-01, 8.414709848079E-01], dtype=np.float64
        )


class TestInterpolatorLoadBigValues(TestInterpolatorLoadValues):
    """
    Loading big values (10^20 times the original) instead of the original np.sin(x).

    For description of data storage, see TestInterpolatorLoadValues.
    """
    def __init__(self):
        super().__init__()
        #: data array from a function sampled on self.x. dtype should be np.float64.
        # self.data: np.array = np.sin(self.x).
        self.data: np.array = np.array(
            [0.000000000000E+00, 1.108826285100E+19, 2.203977434561E+19, 3.271946967962E+19,
             4.299563635284E+19, 5.274153857719E+19, 6.183698030697E+19, 7.016978761467E+19,
             7.763719213007E+19, 8.414709848079E+19], dtype=np.float64
        )
        #: precalculated result of the function used to calculate self.data on self.xsamples.
        #: array holding precalculated nearest neighbour extrapolation data.
        self.precalc_extrapolation_nearest: np.array = np.array(
            [0.000000000000E+00, 0.000000000000E+00, 0.000000000000E+00, 8.414709848079E+19,
             8.414709848079E+19, 8.414709848079E+19], dtype=np.float64
        )

        #: array holding precalculated linear extrapolation data.
        self.precalc_extrapolation_linear: np.array = np.array(
            [-1.995887313179E+20, -1.330591542119E+20, -6.652957710597E+19, 1.232065365851E+20,
             1.622659746895E+20, 2.013254127938E+20], dtype=np.float64
        )

        #: array holding precalculated quadratic extrapolation data.
        self.precalc_extrapolation_quadratic: np.array = np.array(
            [-2.106655911846E+20, -1.379822030416E+20, -6.776033931338E+19, 1.145890531031E+20,
             1.277960407614E+20, 1.237680614556E+20], dtype=np.float64
        )

    def setup_cubic(self):
        self.precalc_interpolation = np.array(
            [0.000000000000e+00, 3.445726766897e+18, 6.892361882629e+18, 1.032764263792e+19,
             1.374723672762e+19, 1.715660220877e+19, 2.054427374305e+19, 2.390211362762e+19,
             2.723736467104e+19, 3.054074932289e+19, 3.380184236890e+19, 3.702697865700e+19,
             4.021030314403e+19, 4.334059817503e+19, 4.642087324270e+19, 4.944967727547e+19,
             5.241623210482e+19, 5.531868543036e+19, 5.816021511759e+19, 6.093090034050e+19,
             6.362532436612e+19, 6.624890560875e+19, 6.879357356812e+19, 7.125198048495e+19,
             7.362936780787e+19, 7.592034615909e+19, 7.811477131101e+19, 8.017642725164e+19,
             8.215858285263e+19, 8.414709848079e+19], dtype=np.float64)

    def setup_linear(self):
        self.precalc_interpolation = np.array(
            [0.000000000000e+00, 3.441185022723e+18, 6.882370045445e+18, 1.032355506817e+19,
             1.373173114280e+19, 1.713047608940e+19, 2.052922103601e+19, 2.388110112734e+19,
             2.719548933444e+19, 3.050987754155e+19, 3.378252140443e+19, 3.697167657888e+19,
             4.016083175333e+19, 4.333170194678e+19, 4.635629229227e+19, 4.938088263776e+19,
             5.240547298324e+19, 5.525062595092e+19, 5.807334924637e+19, 6.089607254182e+19,
             6.356100940512e+19, 6.614705305234e+19, 6.873309669955e+19, 7.119977444438e+19,
             7.351724481123e+19, 7.583471517807e+19, 7.808615118874e+19, 8.010646695275e+19,
             8.212678271677e+19, 8.414709848079e+19], dtype=np.float64)


class TestInterpolatorLoadSmallValues(TestInterpolatorLoadValues):
    """
    Loading small values (10^-20 times the original) instead of the original np.sin(x)

    For description of data storage, see TestInterpolatorLoadValues.
    """
    def __init__(self):
        super().__init__()
        #: data array from a function sampled on self.x. dtype should be np.float64.
        # self.data: np.array = np.sin(self.x).
        self.data: np.array = np.array(
            [0.000000000000E+00, 1.108826285100E-21, 2.203977434561E-21, 3.271946967962E-21,
             4.299563635284E-21, 5.274153857719E-21, 6.183698030697E-21, 7.016978761467E-21,
             7.763719213007E-21, 8.414709848079E-21], dtype=np.float64
        )

        #: precalculated result of the function used to calculate self.data on self.xsamples.
        #: array holding precalculated nearest neighbour extrapolation data.
        self.precalc_extrapolation_nearest: np.array = np.array(
            [0.000000000000E+00, 0.000000000000E+00, 0.000000000000E+00, 8.414709848079E-21,
             8.414709848079E-21, 8.414709848079E-21], dtype=np.float64
        )

        #: array holding precalculated linear extrapolation data.
        self.precalc_extrapolation_linear: np.array = np.array(
            [-1.995887313179E-20, -1.330591542119E-20, -6.652957710597E-21, 1.232065365851E-20,
             1.622659746895E-20, 2.013254127938E-20], dtype=np.float64
        )

        #: array holding precalculated quadratic extrapolation data.
        self.precalc_extrapolation_quadratic: np.array = np.array(
            [-2.106655911846E-20, -1.379822030416E-20, -6.776033931338E-21, 1.145890531031E-20,
             1.277960407614E-20, 1.237680614556E-20], dtype=np.float64
        )

    def setup_cubic(self):
        self.precalc_interpolation = np.array(
            [0.000000000000e+00, 3.445726766897e-22, 6.892361882629e-22, 1.032764263792e-21,
             1.374723672762e-21, 1.715660220877e-21, 2.054427374305e-21, 2.390211362762e-21,
             2.723736467104e-21, 3.054074932289e-21, 3.380184236890e-21, 3.702697865700e-21,
             4.021030314403e-21, 4.334059817503e-21, 4.642087324270e-21, 4.944967727547e-21,
             5.241623210482e-21, 5.531868543036e-21, 5.816021511759e-21, 6.093090034050e-21,
             6.362532436612e-21, 6.624890560875e-21, 6.879357356812e-21, 7.125198048495e-21,
             7.362936780787e-21, 7.592034615909e-21, 7.811477131101e-21, 8.017642725164e-21,
             8.215858285263e-21, 8.414709848079e-21], dtype=np.float64
        )

    def setup_linear(self):
        self.precalc_interpolation = np.array(
            [0.000000000000e+00, 3.441185022723e-22, 6.882370045445e-22, 1.032355506817e-21,
             1.373173114280e-21, 1.713047608940e-21, 2.052922103601e-21, 2.388110112734e-21,
             2.719548933444e-21, 3.050987754155e-21, 3.378252140443e-21, 3.697167657888e-21,
             4.016083175333e-21, 4.333170194678e-21, 4.635629229227e-21, 4.938088263776e-21,
             5.240547298324e-21, 5.525062595092e-21, 5.807334924637e-21, 6.089607254182e-21,
             6.356100940512e-21, 6.614705305234e-21, 6.873309669955e-21, 7.119977444438e-21,
             7.351724481123e-21, 7.583471517807e-21, 7.808615118874e-21, 8.010646695275e-21,
             8.212678271677e-21, 8.414709848079e-21], dtype=np.float64
        )


class TestInterpolatorLoadNormalValuesUneven(TestInterpolatorLoadValues):
    """
    Loading values for the original np.sin(x) tests.

    For description of data storage, see TestInterpolatorLoadValues.
    """
    def __init__(self):
        super().__init__()
        #: data array from a function sampled on self.x. dtype should be np.float64.
        self.data: np.array = np.array(
            [0.000000000000E+00, 3.702857007388E-02, 1.108826285100E-01, 1.476068197303E-01,
             2.203977434561E-01, 2.563646369997E-01, 3.271946967962E-01, 3.619607135792E-01,
             4.299563635284E-01, 4.630927348596E-01, 5.274153857719E-01, 5.585134413496E-01,
             6.183698030697E-01, 6.470460111056E-01, 7.016978761467E-01, 7.275985734567E-01,
             7.763719213007E-01, 7.991776750271E-01, 8.414709848079E-01],
            dtype=np.float64
        )

        #: array holding precalculated nearest neighbour extrapolation data.
        self.precalc_extrapolation_nearest: np.array = np.array(
            [0.000000000000E+00, 0.000000000000E+00, 0.000000000000E+00, 8.414709848079E-01,
             8.414709848079E-01, 8.414709848079E-01], dtype=np.float64
        )

        #: array holding precalculated linear extrapolation data.
        self.precalc_extrapolation_linear: np.array = np.array(
            [-1.999542783989E+00, -1.333028522660E+00, -6.665142613298E-01, 1.222110772835E+00,
             1.602750560862E+00, 1.983390348889E+00], dtype=np.float64
        )
        #: array holding precalculated quadratic extrapolation data.
        self.precalc_extrapolation_quadratic: np.array = np.array(
            [-2.048891639918E+00, -1.354961347517E+00, -6.719974675441E-01, 1.132519435691E+00,
             1.244385212286E+00, 1.177068314593E+00], dtype=np.float64
        )

    def setup_cubic(self):
        self.precalc_interpolation = np.array(
            [0.000000000000E+00, 3.447689899231E-02, 6.890969626029E-02, 1.032663410549E-01,
             1.374955851006E-01, 1.715582751249E-01, 2.054267982438E-01, 2.390422887771E-01,
             2.723733478015E-01, 3.053895619332E-01, 3.380330919885E-01, 3.702773755625E-01,
             4.020863664159E-01, 4.334112596336E-01, 4.642238088320E-01, 4.944838580069E-01,
             5.241575897512E-01, 5.532064755044E-01, 5.815945917048E-01, 6.092983549301E-01,
             6.362718694451E-01, 6.624875407098E-01, 6.879231756786E-01, 7.125336157113E-01,
             7.362980081875E-01, 7.591920171466E-01, 7.811777090800E-01, 8.022266985700E-01,
             8.220389418037E-01, 8.414709848079E-01], dtype=np.float64
        )

    def setup_linear(self):
        self.precalc_interpolation = np.array(
            [0.000000000000E+00, 3.447487558602E-02, 6.886221595150E-02, 1.032425534993E-01,
             1.374760083591E-01, 1.714521223301E-01, 2.053375523404E-01, 2.390013090821E-01,
             2.722403400575E-01, 3.052129541007E-01, 3.379841502805E-01, 3.701670851248E-01,
             4.018202325149E-01, 4.333842640109E-01, 4.642017460822E-01, 4.941450490931E-01,
             5.240883521040E-01, 5.531517076293E-01, 5.812175785538E-01, 6.090817469407E-01,
             6.361688287471E-01, 6.621223876686E-01, 6.875637731188E-01, 7.124154060681E-01,
             7.360077713608E-01, 7.587126057020E-01, 7.810903531061E-01, 8.020944550120E-01,
             8.217827199100E-01, 8.414709848079E-01], dtype=np.float64
        )


class TestInterpolatorLoadBigValuesUneven(TestInterpolatorLoadValues):
    """
    Loading big values (10^20 times the original) instead of the original np.sin(x).

    For description of data storage, see TestInterpolatorLoadValues.
    """
    def __init__(self):
        super().__init__()
        #: data array from a function sampled on self.x. dtype should be np.float64.
        # self.data: np.array = np.sin(self.x).
        self.data: np.array = np.array(
            [0.000000000000E+00, 3.702857007388E+18, 1.108826285100E+19, 1.476068197303E+19,
             2.203977434561E+19, 2.563646369997E+19, 3.271946967962E+19, 3.619607135792E+19,
             4.299563635284E+19, 4.630927348596E+19, 5.274153857719E+19, 5.585134413496E+19,
             6.183698030697E+19, 6.470460111056E+19, 7.016978761467E+19, 7.275985734567E+19,
             7.763719213007E+19, 7.991776750271E+19, 8.414709848079E+19], dtype=np.float64
        )
        #: precalculated result of the function used to calculate self.data on self.xsamples.
        #: array holding precalculated nearest neighbour extrapolation data.
        self.precalc_extrapolation_nearest: np.array = np.array(
            [0.000000000000E+00, 0.000000000000E+00, 0.000000000000E+00, 8.414709848079E+19,
             8.414709848079E+19, 8.414709848079E+19], dtype=np.float64
        )

        #: array holding precalculated linear extrapolation data.
        self.precalc_extrapolation_linear: np.array = np.array(
            [-1.999542783990E+20, -1.333028522660E+20, -6.665142613298E+19, 1.222110772835E+20,
             1.602750560862E+20, 1.983390348889E+20], dtype=np.float64
        )

        #: array holding precalculated quadratic extrapolation data.
        self.precalc_extrapolation_quadratic: np.array = np.array(
            [-2.048891639918E+20, -1.354961347517E+20, -6.719974675441E+19, 1.132519435691E+20,
             1.244385212286E+20, 1.177068314593E+20], dtype=np.float64
        )

    def setup_cubic(self):
        self.precalc_interpolation = np.array(
            [0.000000000000E+00, 3.447689899231E+18, 6.890969626029E+18, 1.032663410549E+19,
             1.374955851006E+19, 1.715582751249E+19, 2.054267982438E+19, 2.390422887771E+19,
             2.723733478015E+19, 3.053895619332E+19, 3.380330919885E+19, 3.702773755625E+19,
             4.020863664159E+19, 4.334112596336E+19, 4.642238088320E+19, 4.944838580069E+19,
             5.241575897512E+19, 5.532064755044E+19, 5.815945917048E+19, 6.092983549301E+19,
             6.362718694451E+19, 6.624875407098E+19, 6.879231756786E+19, 7.125336157113E+19,
             7.362980081875E+19, 7.591920171466E+19, 7.811777090800E+19, 8.022266985700E+19,
             8.220389418037E+19, 8.414709848079E+19], dtype=np.float64)

    def setup_linear(self):
        self.precalc_interpolation = np.array(
            [0.000000000000E+00, 3.447487558603E+18, 6.886221595152E+18, 1.032425534994E+19,
             1.374760083592E+19, 1.714521223301E+19, 2.053375523404E+19, 2.390013090821E+19,
             2.722403400575E+19, 3.052129541007E+19, 3.379841502806E+19, 3.701670851248E+19,
             4.018202325149E+19, 4.333842640109E+19, 4.642017460822E+19, 4.941450490931E+19,
             5.240883521040E+19, 5.531517076293E+19, 5.812175785538E+19, 6.090817469407E+19,
             6.361688287472E+19, 6.621223876687E+19, 6.875637731188E+19, 7.124154060681E+19,
             7.360077713608E+19, 7.587126057020E+19, 7.810903531062E+19, 8.020944550120E+19,
             8.217827199099E+19, 8.414709848079E+19], dtype=np.float64)


class TestInterpolatorLoadSmallValuesUneven(TestInterpolatorLoadValues):
    """
    Loading small values (10^-20 times the original) instead of the original np.sin(x)

    For description of data storage, see TestInterpolatorLoadValues.
    """
    def __init__(self):
        super().__init__()
        #: data array from a function sampled on self.x. dtype should be np.float64.
        # self.data: np.array = np.sin(self.x).
        self.data: np.array = np.array(
            [0.000000000000E+00, 3.702857007388E-22, 1.108826285100E-21, 1.476068197303E-21,
             2.203977434561E-21, 2.563646369997E-21, 3.271946967962E-21, 3.619607135792E-21,
             4.299563635284E-21, 4.630927348596E-21, 5.274153857719E-21, 5.585134413496E-21,
             6.183698030697E-21, 6.470460111056E-21, 7.016978761467E-21, 7.275985734567E-21,
             7.763719213007E-21, 7.991776750271E-21, 8.414709848079E-21], dtype=np.float64
        )

        #: precalculated result of the function used to calculate self.data on self.xsamples.
        #: array holding precalculated nearest neighbour extrapolation data.
        self.precalc_extrapolation_nearest: np.array = np.array(
            [0.000000000000E+00, 0.000000000000E+00, 0.000000000000E+00, 8.414709848079E-21,
             8.414709848079E-21, 8.414709848079E-21], dtype=np.float64
        )

        #: array holding precalculated linear extrapolation data.
        self.precalc_extrapolation_linear: np.array = np.array(
            [-1.999542783990E-20, -1.333028522660E-20, -6.665142613298E-21, 1.222110772835E-20,
             1.602750560862E-20, 1.983390348889E-20], dtype=np.float64
        )

        #: array holding precalculated quadratic extrapolation data.
        self.precalc_extrapolation_quadratic: np.array = np.array(
            [-2.048891639918E-20, -1.354961347517E-20, -6.719974675441E-21, 1.132519435691E-20,
             1.244385212286E-20, 1.177068314593E-20], dtype=np.float64
        )

    def setup_cubic(self):
        self.precalc_interpolation = np.array(
            [0.000000000000E+00, 3.447689899231E-22, 6.890969626029E-22, 1.032663410549E-21,
             1.374955851006E-21, 1.715582751249E-21, 2.054267982438E-21, 2.390422887771E-21,
             2.723733478015E-21, 3.053895619332E-21, 3.380330919885E-21, 3.702773755625E-21,
             4.020863664159E-21, 4.334112596336E-21, 4.642238088320E-21, 4.944838580069E-21,
             5.241575897512E-21, 5.532064755044E-21, 5.815945917048E-21, 6.092983549301E-21,
             6.362718694451E-21, 6.624875407098E-21, 6.879231756786E-21, 7.125336157113E-21,
             7.362980081875E-21, 7.591920171466E-21, 7.811777090800E-21, 8.022266985700E-21,
             8.220389418037E-21, 8.414709848079E-21], dtype=np.float64
        )

    def setup_linear(self):
        self.precalc_interpolation = np.array(
            [0.000000000000E+00, 3.447487558603E-22, 6.886221595152E-22, 1.032425534994E-21,
             1.374760083592E-21, 1.714521223301E-21, 2.053375523404E-21, 2.390013090821E-21,
             2.722403400575E-21, 3.052129541007E-21, 3.379841502806E-21, 3.701670851248E-21,
             4.018202325149E-21, 4.333842640109E-21, 4.642017460822E-21, 4.941450490931E-21,
             5.240883521040E-21, 5.531517076293E-21, 5.812175785538E-21, 6.090817469407E-21,
             6.361688287472E-21, 6.621223876687E-21, 6.875637731188E-21, 7.124154060681E-21,
             7.360077713608E-21, 7.587126057020E-21, 7.810903531062E-21, 8.020944550120E-21,
             8.217827199099E-21, 8.414709848079E-21], dtype=np.float64
        )
