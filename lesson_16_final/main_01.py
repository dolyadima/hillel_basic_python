# class MyContextManager:
#     """
#     Протокол Контекстного Менеджера.
#     """
#
#     def __init__(self, data: dict):
#         self.data = data
#
#     def __enter__(self):
#         print(f'Enter {self.data=}')
#         return self.data
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'Exit {self.data}')
#
#
# with MyContextManager({'bread': 1}) as my_cont_manager:
#     my_cont_manager['milk'] = '3l'
#     print(f'inside my manager {my_cont_manager}')


# from contextlib import contextmanager
#
#
# @contextmanager
# def my_cont_manager():
#     print(f'Enter')
#     yield
#     print(f'Exit')
#
#
# with my_cont_manager():
#     print(f'inside manager, contextmanager')
