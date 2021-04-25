from dao import BaseDao


class StudentDao(BaseDao):


    def find_all(self):
        return super().find_all('tb_student')


if __name__ == '__main__':
    dao = StudentDao()
    print(dao.find_all())