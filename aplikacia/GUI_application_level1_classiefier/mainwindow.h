#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <Python.h>
#include <memory.h>
#include <QMainWindow>
#include <QListWidget>
#include "extraction_level1.h"
#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pushButton_2_clicked();

    void on_list_itemClicked(QListWidgetItem *item);

private:
    Extraction_level1 level1;

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
