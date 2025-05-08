#include <QApplication>

#include "sculator.hpp"

int main (int argc, char **argv) {
    QApplication app(argc, argv);
    app.setApplicationDisplayName("sculator");
    app.setApplicationName("sculator");
    app.setDesktopFileName("sculator");
    app.setApplicationVersion("0.0.1");
    app.setOrganizationName("LooksForFuture");

    Sculator sculator;
    sculator.setWindowTitle("sculator");
    sculator.show();
    return app.exec();
}
