class Calculator:

    @staticmethod
    def subtract_with_zero_if_negative(minuend: int, subtrahend: int) -> int:
        """
        引数minuendから引数subtrahendを引き算し、結果がマイナスの場合はゼロに変換する。

        :param minuend: 引かれる数字 (int)
        :param subtrahend: 引く数字 (int)
        :return: 引き算結果。結果がマイナスの場合はゼロ (int)
        """
        result = max(minuend - subtrahend, 0)
        return result