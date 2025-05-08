#include "sculator.hpp"

#include <QGridLayout>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>

Sculator::Sculator() {
    QGridLayout *layout = new QGridLayout;
    setLayout(layout);
    QLabel* label = new QLabel("Enter your expression:");
    layout->addWidget(label, 0, 0);
    QLineEdit *lineEdit = new QLineEdit;
    layout->addWidget(lineEdit, 0, 1);
    QPushButton* button = new QPushButton("Enter");
    layout->addWidget(button, 0, 2);
    QLabel* output = new QLabel("output");
    layout->addWidget(output, 1, 1);
    layout->setAlignment(output, Qt::AlignHCenter);
}
