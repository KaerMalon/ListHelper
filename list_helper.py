"""
    列表助手模块
"""
class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            查找满足条件的所有元素的方法
        :param list_target: 目标列表
        :param func_condition: 查找条件，函数类型
                        函数名（参数）--->bool
        :return:需要查找的元素 生成器类型
        """
        for i in list_target:
            if func_condition(i):
                yield i

    @staticmethod
    def find_single(list_target, func_condition):
        """
            查找满足条件的单个元素的方法
        :param list_target: 目标列表
        :param func_condition: 查找条件，函数类型
                        函数名（参数）--->bool
        :return:需要查找的元素 生成器类型
        """
        for i in list_target:
            if func_condition(i):
                return i

    @staticmethod
    def sum(list_target, func_handle):
        """
            通用的求和方法
        :param list_target: 需要求和的列表
        :param func_handle:求和的处理逻辑，函数类型，函数名（参数）
        :return:求和的结果
        """
        result = 0
        for item in list_target:
            result += func_handle(item)   #handle函数执行的结果累加，括号和参数不能丢，这里参数是item，也就是列表中的对象
        return result

    @staticmethod
    def select(list_target, func_condition):
        lis_result = []
        for item in list_target:
            lis_result.append(func_condition(item))
        return lis_result

    @staticmethod
    def get_max(list_target, func_handle):
        """
            通用获取最大值的方法
        :param list_target: 目标列表
        :param func_handle: 最大值条件，函数类型，方法（参数）
        :return: 最大值对应的对象
        """
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_handle(max_value) < func_handle(list_target[i]):
                max_value = list_target[i]
        return max_value.name

    @staticmethod
    def get_min(list_target, func_handle):
        """
            通用获取最小值的方法
        :param list_target: 目标列表
        :param func_handle: 最小值条件，函数类型，方法（参数）
        :return: 最小值对应的对象的属性
        """
        min_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_handle(min_value) > func_handle(list_target[i]):
                min_value = list_target[i]
        return min_value.name

    @staticmethod
    def order_by_up(list_target, func_handle):
        """
            通用的升序排序方法
        :param list_target: 需要排序的列表
        :param func_handle: 需要排序的条件，函数类型，方法（参数）
        """
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_handle(list_target[i]) > func_handle(list_target[j]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def order_by_down(list_target, func_handle):
        """
            通用的降序排序方法
        :param list_target: 需要排序的列表
        :param func_handle: 需要排序的条件，函数类型，方法（参数）
        """
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_handle(list_target[i]) < func_handle(list_target[j]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def delete_all(list_target,func_condition):
        """
            通用的删除方法
        :param list_target: 需要删除的列表
        :param func_condition: 删除条件
        """
        for i in range(len(list_target) - 1, -1, -1):
            if func_condition(list_target[i]):
                del list_target[i]