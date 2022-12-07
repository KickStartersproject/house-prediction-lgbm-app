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

    print('request got in here...')

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
    MasVnrArea = request.form.get('MasVnrArea')
    MasVnrAreaCatg = request.form.get('MasVnrAreaCatg')
    LotFrontage = request.form.get('LotFrontage')
    LotArea = request.form.get('LotArea')
    OverallQual = request.form.get('OverallQual')
    YearBuilt = request.form.get('YearBuilt')
    YearRemodAdd = request.form.get('YearRemodAdd')
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
                            'MasVnrArea': MasVnrArea, 'MasVnrAreaCatg': MasVnrAreaCatg, 'ExterQual': ExterQual, 'BsmtQual': BsmtQual, 'BsmtFinSF1': BsmtFinSF1, 'TotalBsmtSF': TotalBsmtSF,
                            'HeatingQC': HeatingQC, 'CentralAir': CentralAir, '1stFlrSF': FirstFlrSF, '2ndFlrSF': SecondFlrSF, 'GrLivArea': GrLivArea,
                            'FullBath': FullBath, 'KitchenQual': KitchenQual, 'TotRmsAbvGrd': TotRmsAbvGrd, 'Fireplaces': Fireplaces,
                            'GarageYrBlt': GarageYrBlt, 'GarageFinish': GarageFinish, 'GarageCars': GarageCars, 'GarageArea': GarageArea})

    print(inputData)
    # URL for prediction model
    url = "http://127.0.0.1:5000/api"
    # url for heroku

    #post data to url
    results =  requests.post(url, inputData)

    # returned data
    result = results.content.decode('UTF-8')
    final_result = float(result)

    return render_template("prediction.html", LotFrontage = LotFrontage, LotArea = LotArea, LotShape = LotShape, LotConfig = LotConfig,
                            Neighborhood = Neighborhood, HouseStyle = validate_transform_data(HouseStyle), OverallQual = OverallQual, YearBuilt = YearBuilt, YearRemodAdd = YearRemodAdd,
                            MasVnrArea = MasVnrArea, MasVnrAreaCatg = validate_transform_data(MasVnrAreaCatg), ExterQual = validate_transform_data(ExterQual), BsmtQual = validate_transform_data(BsmtQual),
                            BsmtFinSF1 = BsmtFinSF1, TotalBsmtSF = TotalBsmtSF, HeatingQC = validate_transform_data(HeatingQC), CentralAir = validate_transform_data(CentralAir),
                            FirstFlrSF = FirstFlrSF, SecondFlrSF = SecondFlrSF, GrLivArea = GrLivArea, FullBath = FullBath, KitchenQual = validate_transform_data(KitchenQual),
                            TotRmsAbvGrd = TotRmsAbvGrd, Fireplaces = Fireplaces, GarageYrBlt = GarageYrBlt, GarageFinish = validate_transform_data(GarageFinish), 
                            GarageCars = GarageCars, GarageArea = GarageArea, results = '$' + ' ' + convert_to_dollars(final_result))


def convert_to_dollars(digits):
    if (digits != None):
        if(type(digits) == float):
            return '{:,.2f}'.format(digits)
        else:
            return digits
    else:
        return 0

def validate_transform_data(data):
    if(data != None):
        if(type(data) == str):
            return transform_data(data)
        else:
            return data
    else:
        return 'N/A'

def transform_data(data):
    if (data == 'Gd'):
        return 'Good'
    elif (data == 'Fa'):
        return 'Fair'
    elif (data == 'Ex'):
        return 'Excellent'
    elif (data == 'Po'):
        return 'Poor'
    elif (data == 'Y'):
        return 'YES'
    elif (data == 'N'):
        return 'NO'
    elif (data == 'Fin'):
        return 'Finished'
    elif (data == 'Unf'):
        return 'Unfinished'
    elif (data == 'RFn'):
        return 'Rearly Finished'
    elif (data == 'NO'):
        return 'Not Good'
    else:
        return data