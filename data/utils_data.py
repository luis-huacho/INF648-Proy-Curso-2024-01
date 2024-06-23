import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.linear_model import Lasso
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor


class DataFeaturesImportances:
    def __init__(self, x: pd.DataFrame, y: pd.Series, seed: int = 42):
        self.x = x
        self.y = y
        self.seed = seed
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            x, y, test_size=0.2, random_state=seed
        )

    def get_matrix_corr(self) -> pd.DataFrame:
        df = self.x.copy()
        df['target'] = self.y
        corr_matrix = df.corr()
        return corr_matrix['target']

    # RandomForestRegressor
    def get_random_forest_regressor_feature_importance(self) -> pd.DataFrame:
        X = self.x.copy()
        X_train = self.X_train.copy()
        y_train = self.y_train.copy()
        seed = self.seed
        # Entrenar el modelo
        reg = RandomForestRegressor(random_state=seed)
        reg.fit(X_train, y_train)
        # Calcular la importancia de las características
        importances = reg.feature_importances_
        feature_names = X.columns

        # Crear un DataFrame de la importancia de las características
        feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
        return feature_importance_df

    # RandomForestRegressor with Permutation
    def get_random_forest_regressor_permutation_feature_importance(self) -> pd.DataFrame:
        X = self.x.copy()
        X_train = self.X_train.copy()
        X_test = self.X_test.copy()
        y_train = self.y_train.copy()
        y_test = self.y_test.copy()
        seed = self.seed
        reg = RandomForestRegressor(random_state=seed)
        reg.fit(X_train, y_train)
        # Calcular la importancia de las características basada en permutación
        result = permutation_importance(reg, X_test, y_test, n_repeats=10, random_state=seed, n_jobs=-1)

        # Crear un DataFrame de la importancia de las características
        importances = result.importances_mean
        feature_names = X.columns
        feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
        return feature_importance_df

    def get_lasso_linear_regression_feature_importance(self) -> pd.DataFrame:
        # Normalizar los datos
        X = self.x.copy()
        y = self.y.copy()
        seed = self.seed
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

        # Crear el modelo Lasso con validación cruzada
        lasso_cv = LassoCV(alphas=np.logspace(-4, 4, 100), cv=5)
        # Ajustar el modelo
        lasso_cv.fit(X_train, y_train)

        # Entrenar el modelo Lasso
        lasso = Lasso(alpha=lasso_cv.alpha_)
        lasso.fit(X_train, y_train)

        # Obtener los coeficientes del modelo
        importances = lasso.coef_
        feature_names = X.columns

        # Crear un DataFrame de la importancia de las características
        feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
        return feature_importance_df

    def get_xgboost_feature_importance(self):
        X = self.x.copy()
        X_train = self.X_train.copy()
        y_train = self.y_train.copy()
        seed = self.seed
        # Entrenar el modelo XGBoost
        xgb = XGBRegressor(random_state=seed)
        xgb.fit(X_train, y_train)

        # Obtener la importancia de las características
        importances = xgb.feature_importances_
        feature_names = X.columns

        # Crear un DataFrame de la importancia de las características
        feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
        return feature_importance_df

    def get_feature_importance_matrix(self) -> pd.DataFrame:
        rf_importance = self.get_random_forest_regressor_feature_importance()
        rf_permutation_importance = self.get_random_forest_regressor_permutation_feature_importance()
        lasso_importance = self.get_lasso_linear_regression_feature_importance()
        xgboost_importance = self.get_xgboost_feature_importance()

        importance_matrix = pd.DataFrame({
            'Feature': self.x.columns,
            'Random Forest': rf_importance.set_index('Feature').reindex(self.x.columns)['Importance'].values,
            'RF Permutation': rf_permutation_importance.set_index('Feature').reindex(self.x.columns)['Importance'].values,
            'Lasso': lasso_importance.set_index('Feature').reindex(self.x.columns)['Importance'].values,
            'XGBoost': xgboost_importance.set_index('Feature').reindex(self.x.columns)['Importance'].values,
        })
        return importance_matrix
