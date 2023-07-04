## `pd.melt()` Cheat Sheet

### `pd.melt()` Nedir?
`pd.melt()` fonksiyonu, pandas kütüphanesindeki bir fonksiyondur ve veri setlerini yeniden düzenlemek için kullanılır. Bu fonksiyon, belirli sütunları korurken diğer sütunları yeni bir yapıda birleştirir.

### Kullanımı
```python
pd.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)
```

### Parametreler
- `frame`: Yeniden düzenlemek istediğiniz DataFrame.
- `id_vars`: Yeni yapıda korunacak sütunlar veya sütunlar listesi. Bunlar, veri setinde sabit kalacak sütunlar olacaktır.
- `value_vars`: Yeniden düzenlenen sütunların adları veya sütunlar listesi. Bu sütunlar, diğer sütunların birleştirildiği sütunlar olacaktır.
- `var_name`: Yeni sütunların adlarının atanacağı sütun adı.
- `value_name`: Değerlerin atanacağı sütun adı.
- `col_level`: Eğer çoklu sütun indeksleri varsa, bu parametre sütun seviyesini belirtir.

### Örnek Kullanım
```python
import pandas as pd

# Veri seti
data = {
    'Name': ['John', 'Jane', 'Mike'],
    'Math': [90, 85, 92],
    'Science': [95, 88, 91],
    'History': [87, 82, 89]
}

df = pd.DataFrame(data)

# Veri setini yeniden düzenleme
df_melted = pd.melt(df, id_vars='Name', value_vars=['Math', 'Science', 'History'], var_name='Subject', value_name='Grade')

print(df_melted)
```

Bu örnekte, `pd.melt()` fonksiyonu kullanılarak veri seti yeniden düzenlenir. `Name` sütunu korunurken, `Math`, `Science` ve `History` sütunları yeni bir yapıda birleştirilir. Yeni sütun adları `Subject` ve `Grade` olarak atanır.