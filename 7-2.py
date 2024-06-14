# 7장 통계분석

# 7-2 상관분석 + 히트맵

# 타이타닉호 생존율 분석하기

# 3. 데이터 수집

import seaborn as sns
import pandas as pd
titanic = sns.load_dataset("titanic")
titanic.to_csv('./7장_data/titanic.csv', index = False)

# 4. 데이터 준비

# - 결측값 있는지 확인하기

titanic.isnull().sum()

# - age 열의 결측값을 중앙값으로 치환하기

titanic['age'] = titanic['age'].fillna(titanic['age'].median())

# - embarked 열의 결측값을 최빈값으로 치환하기

titanic['embarked'].value_counts()
titanic['embarked'] = titanic['embarked'].fillna('S')

# - embark_town 열의 결측값을 최빈값으로 치환하기

titanic['embark_town'].value_counts()
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')

# - deck 열의 결측값을 최빈값으로 치환하기

titanic['deck'].value_counts()
titanic['deck'] = titanic['deck'].fillna('C')

# - 결측치가 다 채워졌는지 확인하기

titanic.isnull().sum()

# 5. 데이터 탐색

# 5.1 데이터의 기본 정보 탐색하기

titanic.info()
titanic.survived.value_counts()

# 5.2 차트를 그려 데이터를 시각적으로 탐색하기

import matplotlib.pyplot as plt
f,ax = plt.subplots(1, 2, figsize = (10, 5))

titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
ax[0].set_title('Survived (Male)')
ax[1].set_title('Survived (Female)')

plt.show()

# 5.3 등급별 생존자 수를 차트로 나타내기

sns.countplot('pclass', hue = 'survived', data = titanic)
plt.title('Pclass vs Survived')
plt.show()

# 6. 데이터 모델링

# 6.1 상관분석을 위한 상관계수를 구하고 저장하기

titanic_corr = titanic.corr(method = 'pearson')
titanic_corr
titanic_corr.to_csv('./7장_data/titanic_corr.csv', index = False)

# 6.2 상관계수 확인하기 

# - 저장한 titanic_corr.csv 파일을 열어본다

# 6.3 특정 변수 사이의 상관계수 구하기 

titanic['survived'].corr(titanic['adult_male'])
titanic['survived'].corr(titanic['fare'])

# 7. 결과 시각화

# 7.1 산점도로 상관 분석 시각화하기 

sns.pairplot(titanic, hue = 'survived')

plt.show()

# 7.2 두 변수의 상관관계 시각화하기

# - 객실 등급과 생존의 상관관계를 seaborn 패키지의 catplot으로 시각화해보자

sns.catplot(x = 'pclass', y = 'survived', hue = 'sex', data = titanic, kind = 'point')

plt.show()

# 7.3 변수 사이의 상관 계수를 히트맵으로 시각화하기

def category_age(x):
    if x < 10:
        return 0
    elif x < 20:
        return 1
    elif x < 30:
        return 2
    elif x < 40:
        return 3
    elif x < 50:
        return 4
    elif x < 60:
        return 5
    elif x < 70:
        return 6
    else:
        return 7
titanic['age2'] = titanic['age'].apply(category_age)
titanic['sex'] = titanic['sex'].map({'male':1, 'female':0})
titanic['family'] = titanic['sibsp'] + titanic['parch'] + 1
titanic.to_csv('./7장_data/titanic3.csv', index = False)
heatmap_data = titanic[['survived', 'sex', 'age2', 'family', 'pclass', 'fare']]
colormap = plt.cm.RdBu

sns.heatmap(heatmap_data.astype(float).corr(), linewidths = 0.1, vmax = 1.0, square = True, cmap = colormap, linecolor = 'white', annot = True,
annot_kws = {"size": 10})

plt.show()
