import sys
#import sql_rc
#import pyforeignkey
# import pyrelation
# import pyforeignkey
# import pymainwork
import numpy as np

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QPixmap
from pymainwork import Ui_MainDlg
from pyrelation import Ui_ProDlg
from pyforeignkey import Ui_ForDlg
from data import SQLTable, PrvProperty, ForProperty

#This is foreign key edit GUI
class FrkDlg(QDialog):

    #This is function called when you click ACCEPT button in Window
    def frk_accept(self):
        self.fk_name = self.ui.lineEdit.text()
        self.trg_tb = self.ui.lineEdit_2.text()
        self.trg_pro = self.ui.lineEdit_3.text()
        self.ref_tb = self.ui.lineEdit_4.text()
        self.ref_pro = self.ui.lineEdit_5.text()

    #This is Class initialize function
    def __init__(self):
        super(FrkDlg, self).__init__()
        self.ui = Ui_ForDlg()
        self.ui.setupUi(self)
        self.ui.btn_accept.clicked.connect(self.frk_accept)
        self.fk_name = ""
        self.trg_tb = ""
        self.trg_pro = ""
        self.ref_tb = ""
        self.ref_pro = ""

#
class RelDlg(QDialog):
    def rel_accept(self):
        self.rel_tbname = self.ui.lineEdit.text()
        self.rel_name = self.ui.lineEdit_2.text()
        self.rel_type = self.ui.lineEdit_3.text()

    def __init__(self):
        super(RelDlg, self).__init__()
        self.ui = Ui_ProDlg()
        self.ui.setupUi(self)
        self.ui.btn_accept.clicked.connect(self.rel_accept)
        self.rel_tbname = ""
        self.rel_name = ""
        self.rel_type = ""


#This is main program window
class MainWork(QDialog):

    # define pro
    def errormsg(self,str):
        mbox = QMessageBox()
        mbox.setText(str)
        mbox.setStandardButtons(QMessageBox.Ok)
        mbox.exec_()

    # define foreign property add click
    # This function is called when you click ADD button.
    def slot_property_add(self):
        fkdlg = RelDlg();
        ret = fkdlg.exec_();
        if ret == QDialog.Accepted:
            rel_tbname = fkdlg.rel_tbname
            rel_name = fkdlg.rel_name
            rel_type = fkdlg.rel_type

            totalrow = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(totalrow + 1)
            item1 = QTableWidgetItem(rel_tbname)
            item2 = QTableWidgetItem(rel_name)
            item3 = QTableWidgetItem(rel_type)

            self.ui.tableWidget.setItem(totalrow, 0, item1)
            self.ui.tableWidget.setItem(totalrow, 1, item2)
            self.ui.tableWidget.setItem(totalrow, 2, item3)

            mbox = QMessageBox()
            mbox.setText("You created new property key successfully!!!")
            mbox.setStandardButtons(QMessageBox.Ok)
            mbox.exec_()
        return

    # define foreign property del click
    # This function is called when you clicked del button
    def slot_property_del(self):
        currow = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(currow)
        return


    # define foreign property add click
    #This function is called when you click ADD button.
    def slot_frproperty_add(self):
        fkdlg = FrkDlg();
        ret = fkdlg.exec_();
        if ret == QDialog.Accepted:
            fk_name = fkdlg.fk_name
            trg_tb = fkdlg.trg_tb
            trg_pro = fkdlg.trg_pro
            ref_tb = fkdlg.ref_tb
            ref_pro = fkdlg.ref_pro

            totalrow = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.setRowCount(totalrow + 1)
            item1 = QTableWidgetItem(fk_name)
            item2 = QTableWidgetItem(trg_tb)
            item3 = QTableWidgetItem(trg_pro)
            item4 = QTableWidgetItem(ref_tb)
            item5 = QTableWidgetItem(ref_pro)

            self.ui.tableWidget_2.setItem(totalrow, 0, item1)
            self.ui.tableWidget_2.setItem(totalrow, 1, item2)
            self.ui.tableWidget_2.setItem(totalrow, 2, item3)
            self.ui.tableWidget_2.setItem(totalrow, 3, item4)
            self.ui.tableWidget_2.setItem(totalrow, 4, item5)

            mbox = QMessageBox()
            mbox.setText("You created new foreign key successfully!!!")
            mbox.setStandardButtons(QMessageBox.Ok)
            mbox.exec_()
        return

    # define foreign property del click
    #This function is called when you clicked del button
    def slot_frproperty_del(self):
        currow = self.ui.tableWidget_2.currentRow()
        self.ui.tableWidget_2.removeRow(currow)
        return

    def initTable(self):
        if self.samplemode < 3:
            return
        tablenames = []
        for i in range(self.ui.tableWidget.rowCount()):
            isexist = 0
            for j in tablenames:
                if j == self.ui.tableWidget.item(i, 0).text():
                    isexist = 1
                    break
            if isexist == 0:
                tablenames.append(self.ui.tableWidget.item(i, 0).text())
        self.tables[2] = np.empty(len(tablenames), dtype=object)
        # print(tablenames)
        tablenames.clear()
        g = 0
        for i in range(self.ui.tableWidget.rowCount()):
            t_name = self.ui.tableWidget.item(i, 0).text()
            if tablenames.count(t_name) == 0:
                tablenames.append(t_name)
                tb = SQLTable(t_name)
                pr = PrvProperty(self.ui.tableWidget.item(i, 1).text(), self.ui.tableWidget.item(i, 2).text())
                tb.prvkey_list.append(pr)
                self.tables[2][g] = tb
                g = g + 1
            else:
                pr = PrvProperty(self.ui.tableWidget.item(i, 1).text(), self.ui.tableWidget.item(i, 2).text())
                tb = SQLTable("a")
                k = 0
                for j in tablenames:
                    if j == t_name:
                        self.tables[2][k].prvkey_list.append(pr)
                        break
                    k = k + 1
        # print(tablenames)
        # print(self.tables[2][:])

        g = 0
        for i in range(self.ui.tableWidget_2.rowCount()):
            t_name = self.ui.tableWidget_2.item(i, 1).text()
            if tablenames.count(t_name) == 0:
                self.errormsg("Error! This foreign key is invalid!!! Let's check")
                return
            else:
                fk = ForProperty(self.ui.tableWidget_2.item(i, 0).text(), t_name, self.ui.tableWidget_2.item(i, 2).text(),
                                 self.ui.tableWidget_2.item(i, 3).text(), self.ui.tableWidget_2.item(i, 4).text())
                tb = SQLTable("a")
                k = 0
                for j in tablenames:
                    if j == t_name:
                        self.tables[2][k].forkey_list.append(fk)
                        break
                    k = k + 1
        print(tablenames)
        print(self.tables[2][:])
    #define get fk from field
    #you can get fk array from fl that is one field of target view using this function.
    def getFKfromField(self, fl):
        arr = []
        for i in self.FKC:
            if i.rfr_id == fl:
                arr.append(i)
        return arr

    #define GroupValueCorresponding
    #you can get class variable GVC(result for step1) using this function.
    #This is recursive function
    def func_GVC(self, i, cur):
        if self.samplemode < 4:
            return
        tcnt = len(self.fields) - 1
        if i == tcnt:
            self.GVC.append(cur)
            #print(cur)
            return
        else:
            tmp_arr = self.getFKfromField(self.fields[i])
            for j in tmp_arr:
                cur.append(j)
                self.func_GVC(i+1, cur)

    #check all contains fk
    #this function is checked if cur is involved in all
    def func_allchk(self, cur, all):
        ttmp = []
        isSuc = 0
        for i in cur:
            for j in i:
                if ttmp.count(j) == 0:
                    ttmp.append(j)
        for i in all:
            if ttmp.count(i) == 0:
                isSuc = 1
        if isSuc == 0:
            return 1
        else:
            return 0

    #get missing fk
    #this funcion get array that one of (all - cur)
    def func_missing(self, cur, all):
        ttmp = []
        # isSuc = 0
        ttrt = []
        for i in cur:
            for j in i:
                if ttmp.count(j) == 0:
                    ttmp.append(j)
        for i in all:
            if ttmp.count(i) == 0:
                # isSuc = 1
                ttrt.append(i)
        return ttrt
        # if isSuc == 0:
        #     return 1
        # else:
        #     return 0


    #define Candidate Set
    #this function calculate candidate set from group value corresponding
    def func_CS(self, i, cur):
        if self.samplemode < 4:
            return
        mearr = self.GVC[i]
        tcnt = len(self.GVC) - 1
        isSuc = 0
        if tcnt == i:
            isSuc = self.func_allchk(cur, self.FKC)
            if isSuc == 1:
                self.CS.append(cur)
            return
        else:
            missing_fk = self.func_missing(cur, self.FKC)
            for k in missing_fk:
                #parr = self.GVC[]
                #print("dsffdsf")
                ia = []
                ia.append(k)

                for j in range(tcnt+1):
                    if j > i:
                        isSuc = self.func_allchk(ia, self.GVC[j])
                        if isSuc == 1:
                            cur.append(self.GVC[j])
                            self.func_CS(j, cur)

    #this function calculate top candidate from Candidates with using rank generator algorithm
    def getTopRankCS(self):
        self.CS.sort()
        #toprank = self.CS[0]

    #generate query
    def getQuery(self):
        if self.samplemode < 3:
            return self.outputstr[self.samplemode - 1]
        else:
            totalstr = ""
            for i in self.tables[2]:
                str = 'CREATE TABLE ' + "'" + i.name + "' ( "
                for j in i.prvkey_list:
                    str = str + "'" + j.name + "' " + j.type + " NOT NULL , "
                for j in i.forkey_list:
                    str = str + "CONSTRAINT `" + j.name + "` FOREIGN KEY (`" + j.trg_id + "`) REFERENCES " \
                    "`" + j.rfr_tb + "` (`" + j.rfr_id + "`) ON DELETE CASCADE ON UPDATE CASCADE ,"
                str = str[0:-3] + " ) "
                totalstr = totalstr + str
            return totalstr

    # define generate query
    #core feature
    def slot_gen_query(self):
        # self.loadData()
        self.initTable()
        #step1
        totalrows =  self.ui.tableWidget_2.rowCount()
        for i in range(totalrows):
            fk_name = self.ui.tableWidget_2.item(i, 0)
            src_t = self.ui.tableWidget_2.item(i, 1)
            src_f = self.ui.tableWidget_2.item(i, 2)
            trg_f = self.ui.tableWidget_2.item(i, 4)
            #foreign key initial
            tmp_frg = ForProperty(fk_name, src_t, src_f, "Target", trg_f)
            self.FKC.append(tmp_frg)
            #target view field initial
            self.isExist = 0
            for j in self.fields:
                if j == trg_f:
                    self.isExist = 1
                    break
            if self.isExist == 0:
                self.fields.append(trg_f)
        #group value corresponding
        cur = []
        self.func_GVC(0, cur)
        # for i in self.FKC:
        #     self.GVC.append(i)
        #success GVC is result in step 1

        #step2
        #generate candidate sets
        cur.clear()
        self.func_CS(0, cur)
        #CS is result in step 2

        #step3
        self.getTopRankCS()

        #step4
        str = self.getQuery()
        self.ui.plainTextEdit.setPlainText(str)

        self.fields = []
        # all Group Value Correspondences for step1
        self.GVC = []
        # all Foreign key
        self.FKC = []
        # all Candidates Sets
        self.CS = []
        # state variable
        self.isExist = 0

        return

    def func_rd(self):
        i = 1
        if self.ui.rdbtn1.isChecked() == True:
            i = 1
        if self.ui.rdbtn2.isChecked() == True:
            i = 2
        if self.ui.rdbtn3.isChecked() == True:
            i = 3
        self.samplemode = i
        self.loadData()
        if i == 3:
            self.ui.tableWidget_2.setEnabled(True)
            self.ui.tableWidget.setEnabled(True)
            self.ui.btn_pr_add.setEnabled(True)
            self.ui.btn_pr_del.setEnabled(True)
            self.ui.btn_fk_add.setEnabled(True)
            self.ui.btn_fk_del.setEnabled(True)
        else:
            self.ui.tableWidget_2.setEnabled(True)
            self.ui.tableWidget.setEnabled(True)
            self.ui.btn_pr_add.setEnabled(False)
            self.ui.btn_pr_del.setEnabled(False)
            self.ui.btn_fk_add.setEnabled(False)
            self.ui.btn_fk_del.setEnabled(False)
            picstr = './ui/ER_' + str(i) + '.png'
            self.ui.label.setPixmap(QPixmap(picstr))
        #print(i)

    def loadData(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget.setHorizontalHeaderLabels(["T_Name", "P_Name", "P_Type"])
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["Fk", "SRC_T", "SRC_P", "TRG_T", "TRG_P"])
        self.fields = []
        self.GVC = []
        self.FKC = []
        self.CS = []
        self.isExist = 0
        if self.samplemode == 1:
            self.ui.tableWidget.setRowCount(20)
            self.ui.tableWidget_2.setRowCount(6)
            # print(self.tables)
            k = 0
            l = 0
            for i in self.tables[0]:
                # print(i.name)
                # print(len(i.prvkey_list))
                for j in i.prvkey_list:
                    self.ui.tableWidget.setItem(k, 0, QTableWidgetItem(i.name))
                    self.ui.tableWidget.setItem(k, 1, QTableWidgetItem(j.name))
                    self.ui.tableWidget.setItem(k, 2, QTableWidgetItem(j.type))
                    k = k + 1
                #print(len(i.forkey_list))
                for j in i.forkey_list:
                    self.ui.tableWidget_2.setItem(l, 0, QTableWidgetItem(j.name))
                    self.ui.tableWidget_2.setItem(l, 1, QTableWidgetItem(j.trg_tb))
                    self.ui.tableWidget_2.setItem(l, 2, QTableWidgetItem(j.trg_id))
                    self.ui.tableWidget_2.setItem(l, 3, QTableWidgetItem(j.rfr_tb))
                    self.ui.tableWidget_2.setItem(l, 4, QTableWidgetItem(j.rfr_id))
                    l = l + 1
        elif self.samplemode == 2:
            self.ui.tableWidget.setRowCount(11)
            self.ui.tableWidget_2.setRowCount(3)
            k = 0
            l = 0
            for i in self.tables[1]:
                # print(i.name)
                # print(len(i.prvkey_list))
                for j in i.prvkey_list:
                    self.ui.tableWidget.setItem(k, 0, QTableWidgetItem(i.name))
                    self.ui.tableWidget.setItem(k, 1, QTableWidgetItem(j.name))
                    self.ui.tableWidget.setItem(k, 2, QTableWidgetItem(j.type))
                    k = k + 1
                #print(len(i.forkey_list))
                for j in i.forkey_list:
                    self.ui.tableWidget_2.setItem(l, 0, QTableWidgetItem(j.name))
                    self.ui.tableWidget_2.setItem(l, 1, QTableWidgetItem(j.trg_tb))
                    self.ui.tableWidget_2.setItem(l, 2, QTableWidgetItem(j.trg_id))
                    self.ui.tableWidget_2.setItem(l, 3, QTableWidgetItem(j.rfr_tb))
                    self.ui.tableWidget_2.setItem(l, 4, QTableWidgetItem(j.rfr_id))
                    l = l + 1
        else:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget_2.setRowCount(0)

    #this funciton is main class initialize function
    def __init__(self):
        super(MainWork, self).__init__()
        self.ui = Ui_MainDlg()
        self.ui.setupUi(self)
        # self.ui.btn_rl_add.clicked.connect(self.slot_property_add)
        # self.ui.btn_rl_del.clicked.connect(self.slot_property_del)
        self.ui.btn_fk_add.clicked.connect(self.slot_frproperty_add)
        self.ui.btn_fk_del.clicked.connect(self.slot_frproperty_del)
        self.ui.btn_pr_add.clicked.connect(self.slot_property_add)
        self.ui.btn_pr_del.clicked.connect(self.slot_property_del)
        self.ui.btn_gen_query.clicked.connect(self.slot_gen_query)
        self.ui.tableWidget_2.setEnabled(False)
        self.ui.btn_fk_add.setEnabled(False)
        self.ui.btn_fk_del.setEnabled(False)
        self.ui.btn_pr_add.setEnabled(False)
        self.ui.btn_pr_del.setEnabled(False)
        self.ui.rdbtn1.clicked.connect(self.func_rd)
        self.ui.rdbtn2.clicked.connect(self.func_rd)
        self.ui.rdbtn3.clicked.connect(self.func_rd)
        self.ui.btn_gen_query.setDefault(True)
        self.samplemode = 1
        self.tables = np.empty(3, dtype=object)
        # self.ui.rdbtn3.setEnabled(False)

        pr = np.empty(2, dtype=object)
        tb = np.empty(6, dtype=object)
        pr[0] = PrvProperty("ID", "int")
        pr[1] = PrvProperty("City_name", "varchar")
        tb[0] = SQLTable("city_tb")
        tb[0].prvkey_list = pr
        # print(pr)
        # print(tb[0].prvkey_list[1].type)
        pr = np.empty(2, dtype=object)
        pr[0] = PrvProperty("ID", "int")
        pr[1] = PrvProperty("Email_addr", "varchar")
        tb[1] = SQLTable("email_tb")
        tb[1].prvkey_list = pr
        # print(pr)
        # print(tb[1].prvkey_list[1].type)
        pr = np.empty(2, dtype=object)
        pr[0] = PrvProperty("ID", "int")
        pr[1] = PrvProperty("Job_type", "varchar")
        tb[2] = SQLTable("joby_tb")
        tb[2].prvkey_list = pr

        pr = np.empty(2, dtype=object)
        pr[0] = PrvProperty("Id", "int")
        pr[1] = PrvProperty("country_name", "varchar")
        tb[3] = SQLTable("country_tb")
        tb[3].prvkey_list = pr

        pr = np.empty(3, dtype=object)
        pr[0] = PrvProperty("Id", "int")
        pr[1] = PrvProperty("university_name", "varchar")
        pr[2] = PrvProperty("country", "int")
        tb[4] = SQLTable("university_tb")
        tb[4].prvkey_list = pr
        fk = np.empty(1, dtype=object)
        fk[0] = ForProperty("f6", "university_tb", "country", "country_tb", "Id")
        tb[4].forkey_list = fk

        pr = np.empty(9, dtype=object)
        pr[0] = PrvProperty("ID", "int")
        pr[1] = PrvProperty("Name", "varchar")
        pr[2] = PrvProperty("University", "int")
        pr[3] = PrvProperty("Sex", "varchar")
        pr[4] = PrvProperty("Age", "int")
        pr[5] = PrvProperty("Country", "int")
        pr[6] = PrvProperty("City", "int")
        pr[7] = PrvProperty("Email", "int")
        pr[8] = PrvProperty("job", "int")
        tb[5] = SQLTable("user_tb")
        tb[5].prvkey_list = pr
        fk = np.empty(5, dtype=object)
        fk[0] = ForProperty("f1", "user_tb", "University", "university_tb", "Id")
        fk[1] = ForProperty("f2", "user_tb", "Country", "country_tb", "Id")
        fk[2] = ForProperty("f3", "user_tb", "Email", "email_tb", "ID")
        fk[3] = ForProperty("f4", "user_tb", "Job", "job_tb", "ID")
        fk[4] = ForProperty("f5", "user_tb", "City", "city_tb", "ID")
        tb[5].forkey_list = fk

        self.tables[0] = tb
        pr = np.empty(6, dtype=object)
        tb = np.empty(3, dtype=object)
        tb[0] = SQLTable("user_tb")
        pr[0] = PrvProperty("ID", "int")
        pr[1] = PrvProperty("Name", "varchar")
        pr[2] = PrvProperty("University", "int")
        pr[3] = PrvProperty("Sex", "varchar")
        pr[4] = PrvProperty("Age", "int")
        pr[5] = PrvProperty("Country", "int")
        tb[0].prvkey_list = pr
        fk = np.empty(2, dtype=object)
        fk[0] = ForProperty("f1", "user_tb", "Country", "country_tb", "Id")
        fk[1] = ForProperty("f2", "user_tb", "University", "university_tb", "Id")
        tb[0].forkey_list = fk

        pr = np.empty(3, dtype=object)
        tb[1] = SQLTable("university_tb")
        pr[0] = PrvProperty("Id", "int")
        pr[1] = PrvProperty("university_name", "varchar")
        pr[2] = PrvProperty("country", "int")
        tb[1].prvkey_list = pr
        fk = np.empty(1, dtype=object)
        fk[0] = ForProperty("f3", "university_tb", "country", "country_tb", "Id")
        tb[1].forkey_list = fk

        pr = np.empty(2, dtype=object)
        tb[2] = SQLTable("country_tb")
        pr[0] = PrvProperty("Id", "int")
        pr[1] = PrvProperty("country", "varchar")
        tb[2].prvkey_list = pr
        self.tables[1] = tb
        #print(self.tables)

        self.smData1 = [["F1", "S2", "A", "Z"], ["F2", "S2", "B", "Y"], ["F3", "S1", "A", "O"], ["F4", "S1", "A", "P"],
                       ["F5", "S4", "A", "W"], ["F6", "S4", "B", "X"], ["F7", "S6", "B", "W"], ["F8", "S6", "A", "O"],
                       ["F9", "S5", "A", "Z"], ["F10", "S5", "B", "O"], ["F11", "S5", "C", "X"]]
        #
        # self.smData4 = [["F1", "S1", "A", "C"], ["F2", "S2", "A", "D"], ["F3", "S2", "B", "C"]]
        # self.str = ['aaa', 'CREATE VIEW T(Z, Y, O, P, W, X) AS SELECT F9(S5.A), NULL ,F10(S5,.B), F4(S3.A), F5(S4.A),' \
        #             ' F11(S5.C) FROM S5, S3, S4 WHRER S3.K=S4.FK AND F4.K = S5.FK UNION SELECT F1(S2.A) , F2(S2.B),' \
        #             ' F7(S6.A), NULL, F8(S6.B), F6(S4.B) FROM S2, S4, S6 WHERE S2.K = S4.FK AND S4.K = S6.FK' \
        #             ' UNION SELECT NULL, NULL, F3(S1.A), NULL, NULL, NULL FROM S1',
        #             'dsf',
        #             'a',
        #             'CREATE VIEW T(C,D) AS SELECT F1(S1.A), F2(S2.A) FROM S1,S2 WHERE S1.K = S2.FK UNION SELECT' \
        #             ' NULL, F3(S2.B) FROM S2']
        #all tables
        self.outputstr = ["""CREATE TABLE `city_tb`  (
                          `ID` int(11) NOT NULL,
                          `City_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          PRIMARY KEY (`ID`) USING BTREE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
                        
                        
                        CREATE TABLE `country_tb`  (
                          `Id` int(11) NOT NULL,
                          `country_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          PRIMARY KEY (`Id`) USING BTREE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
                        
                        CREATE TABLE `email_tb`  (
                          `ID` int(11) NOT NULL,
                          `Email_addr` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          PRIMARY KEY (`ID`) USING BTREE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
                        
                        CREATE TABLE `job_tb`  (
                          `ID` int(11) NOT NULL,
                          `Job_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          PRIMARY KEY (`ID`) USING BTREE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

                        CREATE TABLE `university_tb`  (
                          `Id` int(11) NOT NULL,
                          `university_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          `country` int(255) NULL DEFAULT NULL,
                          PRIMARY KEY (`Id`) USING BTREE,
                          INDEX `fk_3`(`country`) USING BTREE,
                          CONSTRAINT `fk_3` FOREIGN KEY (`country`) REFERENCES `country_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
                        
                        CREATE TABLE `user_tb`  (
                          `ID` int(11) NOT NULL,
                          `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          `University` int(11) NULL DEFAULT NULL,
                          `Sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
                          `Age` int(11) NULL DEFAULT NULL,
                          `Country` int(11) NULL DEFAULT NULL,
                          `City` int(11) NULL DEFAULT NULL,
                          `Email` int(255) NULL DEFAULT NULL,
                          `Job` int(11) NULL DEFAULT NULL,
                          PRIMARY KEY (`ID`) USING BTREE,
                          INDEX `fk_1`(`University`) USING BTREE,
                          INDEX `fk_2`(`Country`) USING BTREE,
                          INDEX `fk4`(`City`) USING BTREE,
                          INDEX `fk5`(`Email`) USING BTREE,
                          INDEX `fk6`(`Job`) USING BTREE,
                          CONSTRAINT `fk_1` FOREIGN KEY (`University`) REFERENCES `university_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
                          CONSTRAINT `fk_2` FOREIGN KEY (`Country`) REFERENCES `country_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
                          CONSTRAINT `fk4` FOREIGN KEY (`City`) REFERENCES `city_tb` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
                          CONSTRAINT `fk5` FOREIGN KEY (`Email`) REFERENCES `email_tb` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
                          CONSTRAINT `fk6` FOREIGN KEY (`Job`) REFERENCES `job_tb` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;""" ,
                          """CREATE TABLE `country_tb`  (
                          `Id` int(11) NOT NULL,
                          `country_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          PRIMARY KEY (`Id`) USING BTREE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
                        
                        CREATE TABLE `university_tb`  (
                          `Id` int(11) NOT NULL,
                          `university_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          `country` int(255) NULL DEFAULT NULL,
                          PRIMARY KEY (`Id`) USING BTREE,
                          INDEX `fk_3`(`country`) USING BTREE,
                          CONSTRAINT `fk_3` FOREIGN KEY (`country`) REFERENCES `country_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
                                                
                        CREATE TABLE `user_tb`  (
                          `ID` int(11) NOT NULL,
                          `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                          `University` int(11) NULL DEFAULT NULL,
                          `Sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
                          `Age` int(11) NULL DEFAULT NULL,
                          `Country` int(11) NULL DEFAULT NULL,
                          PRIMARY KEY (`ID`) USING BTREE,
                          INDEX `fk_1`(`University`) USING BTREE,
                          INDEX `fk_2`(`Country`) USING BTREE,
                          CONSTRAINT `fk_1` FOREIGN KEY (`University`) REFERENCES `university_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
                          CONSTRAINT `fk_2` FOREIGN KEY (`Country`) REFERENCES `country_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
                        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;"""]
        self.fields = []
        #all Group Value Correspondences for step1
        self.GVC = []
        #all Foreign key
        self.FKC = []
        #all Candidates Sets
        self.CS = []
        #state variable
        self.isExist = 0

def main():
    app = QApplication(sys.argv)
    mbox = QMessageBox()
    mbox.setText("As shown picture, this is good sample dataset,Don't change ,only use!!!")
    mbox.setStandardButtons(QMessageBox.Ok)
    mbox.exec_()
    w = MainWork()
    w.exec_()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
