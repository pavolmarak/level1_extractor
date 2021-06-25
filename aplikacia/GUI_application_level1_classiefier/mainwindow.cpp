#include <Python.h>
#define PY_SSIZE_T_CLEAN

#include "mainwindow.h"
#include "ui_mainwindow.h"
// Python headers
#include <abstract.h>

// NumPy C/API headers
#include <numpy/ndarrayobject.h>

#include <vector>

#include <QDir>
#include <string>
#include <iostream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    level1.loadScript("trainedScript");
    QDir dir("/home/editav/Plocha/LeftLoop/");
    QFileInfoList lst = dir.entryInfoList(QStringList() << "*.tif");
    foreach (const QFileInfo& i, lst) {
        ui->list->addItem(i.fileName());
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_2_clicked()
{
    QPixmap imagePixmap =QPixmap("/home/editav/Plocha/LeftLoop/"+ui->filename->text());
    int result = -1;

    result = level1.classify(imagePixmap);

    if(result == 0){
        ui->label->setText("ARCH");

    }
    if(result == 1){
        ui->label->setText("LEFT LOOP");
    }
    if(result == 2){
        ui->label->setText("RIGHT LOOP");
    }
    if(result == 3){
        ui->label->setText("TENDED ARCH");
    }
    if(result == 4){
        ui->label->setText("WHORL");
    }
}

void MainWindow::on_list_itemClicked(QListWidgetItem *item)
{
    ui->filename->setText(item->text());
    QPixmap imagePixmap =QPixmap("/home/editav/Plocha/LeftLoop/"+item->text());
    ui->img_2->setPixmap(imagePixmap);
    ui->label->setText("");
}
