from flask import Blueprint, render_template, request, json, jsonify
import requests

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def home():
    return render_template('index.html')

@routes.route('/prediction')
def prediction():
    return render_template("prediction.html")

@routes.route('/predict', methods=['GET', 'POST'])
def predict():
    LotShape = request.form.get('LotShape')
    LotConfig = request.form.get('LotConfig')
    Neighborhood = request.form.get('Neighborhood')
    HouseStyle = request.form.get('HouseStyle')
    ExterQual = request.form.get('ExterQual')
    BsmtQual = request.form.get('BsmtQual')
    HeatingQC = request.form.get('HeatingQC')
    CentralAir = request.form.get('CentralAir')
    KitchenQual = request.form.get('KitchenQual')
    GarageFinish = request.form.get('GarageFinish')
    LotFrontage = request.form.get('LotFrontage')
    LotArea = request.form.get('LotArea')
    OverallQual = request.form.get('OverallQual')
    YearBuilt = request.form.get('YearBuilt')
    YearRemodAdd = request.form.get('YearRemodAdd')
    MasVnrArea = request.form.get('MasVnrArea')
    BsmtFinSF1 = request.form.get('BsmtFinSF1')
    TotalBsmtSF = request.form.get('TotalBsmtSF')
    FirstFlrSF = request.form.get('1stFlrSF')
    SecondFlrSF = request.form.get('2ndFlrSF')
    GrLivArea = request.form.get('GrLivArea')
    FullBath = request.form.get('FullBath')
    TotRmsAbvGrd = request.form.get('TotRmsAbvGrd')
    Fireplaces = request.form.get('Fireplaces')
    GarageYrBlt = request.form.get('GarageYrBlt')
    GarageCars = request.form.get('GarageCars')
    GarageArea = request.form.get('GarageArea')

    inputData = json.dumps({'LotFrontage': LotFrontage, 'LotArea': LotArea, 'LotShape': LotShape, 'LotConfig': LotConfig,
                            'Neighborhood': Neighborhood, 'HouseStyle': HouseStyle, 'OverallQual': OverallQual, 'YearBuilt': YearBuilt, 'YearRemodAdd': YearRemodAdd,
                            'MasVnrArea': MasVnrArea, 'ExterQual': ExterQual, 'BsmtQual': BsmtQual, 'BsmtFinSF1': BsmtFinSF1, 'TotalBsmtSF': TotalBsmtSF,
                            'HeatingQC': HeatingQC, 'CentralAir': CentralAir, '1stFlrSF': FirstFlrSF, '2ndFlrSF': SecondFlrSF, 'GrLivArea': GrLivArea,
                            'FullBath': FullBath, 'KitchenQual': KitchenQual, 'TotRmsAbvGrd': TotRmsAbvGrd, 'Fireplaces': Fireplaces,
                            'GarageYrBlt': GarageYrBlt, 'GarageFinish': GarageFinish, 'GarageCars': GarageCars, 'GarageArea': GarageArea})

    # URL for prediction model
    url = "http://127.0.0.0:5000"

    #post data to url
    results =  requests.post(url, inputData)

    return render_template("prediction.html", LotFrontage = LotFrontage, LotArea = LotArea, LotShape = LotShape, LotConfig = LotConfig,
                            Neighborhood = Neighborhood, HouseStyle = HouseStyle, OverallQual = OverallQual, YearBuilt = YearBuilt, YearRemodAdd = YearRemodAdd,
                            MasVnrArea = MasVnrArea, ExterQual = ExterQual, BsmtQual = BsmtQual, BsmtFinSF1 = BsmtFinSF1, TotalBsmtSF = TotalBsmtSF,
                            HeatingQC = HeatingQC, CentralAir = CentralAir, firstFlrSF = FirstFlrSF, SecondFlrSF = SecondFlrSF, GrLivArea = GrLivArea,
                            FullBath = FullBath, KitchenQual = KitchenQual, TotRmsAbvGrd = TotRmsAbvGrd, Fireplaces = Fireplaces,
                            GarageYrBlt = GarageYrBlt, GarageFinish = GarageFinish, GarageCars = GarageCars, GarageArea = GarageArea,
                            results=results.content.decode('UTF-8'))