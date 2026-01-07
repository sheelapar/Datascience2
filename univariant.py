# Class univariant to separate qualitative and quantitative columns

class univariant():
    @staticmethod
    def qualquan(dataset):
        qual = []
        quan = []

        for column in dataset.columns:
            if dataset[column].dtype == 'object':
                qual.append(column)
            else:
                quan.append(column)
        return qual, quan
