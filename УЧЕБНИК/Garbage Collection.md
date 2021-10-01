## <center>Garbage Collection</center>

* [reference counting](#Все-является-объектом)

> <span style='font-size:20px;color:lawngreen;'> 📝Примечание:</span> 
> 
> Если вы создадите несколько объектов и потеряете связь с этими объектами, это не означает, что память будет освобождена

```python
def memory_profile():
    import psutil, os 
    print("Процесс потребляет %.2f Мегабайт\n" % 
    (psutil.Process(os.getpid()).memory_info().rss / float(1000 * 1000), ))

class BIG(object):
    def __init__(self):
        self.val = [[999999999999999999999999999.0 for _ in range(99999999)] for x in range(2)]
        self.left = None
        self.right = None
        
>>> memory_profile() # Примерно 23.83M
>>> x = BIG()
>>> memory_profile() # Примерно 1627.08M
>>> x = None
>>> memory_profile() # Примерно 24.25M, количество ссылок на объект экземпляра равно 0
>>> x = BIG()
>>> y = BIG()
>>> x.right = y
>>> y.left = x
>>> memory_profile() # Примерно 3228.97M
>>> x, y = None, None # Теперь я потерял связь с этими двумя экземплярами
>>> # Но эти два экземпляра связаны друг с другом, каждый из них имеет ссылку на другой
>>> # Таким образом, количество ссылок никогда не стремится к нулю, gc не может освободить память
>>> memory_profile() # Примерно 3228.97M
```