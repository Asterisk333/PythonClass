# Modellierung mit OOP

Schauen wir uns einen manuellen Ablauf an, mit dem viele Unternehmen zu kämpfen haben, nämlich das Rechnungsmanagement.
Viele Unternehmen erhalten Rechnungen, die pünktlich beglichen werden müssen. Verspätete Zahlungen ziehen
Säumnisgebühren nach sich, die zu einer Verschwendung von Geld führen. Bevor eine Rechnung bezahlt werden kann, muss sie
bearbeitet werden. Es ist üblich, dass eine Rechnung durch mehrere Hände geht, bevor sie irgendwo registriert wird und
die Zahlung erfolgt.

Der Prozess beginnt in der Regel mit einer ersten Sortierphase, in der die Rechnung an die zuständige Abteilung
weitergeleitet wird. Anschließend wird die Rechnung auf ihre Korrektheit geprüft und von einer Person mit der
entsprechenden Berechtigungsstufe genehmigt. Zum Schluss wird die Rechnung bezahlt. In einem kleinen Unternehmen kann
der Geschäftsinhaber alle diese Schritte durchführen. In einem großen Unternehmen können viele Personen und Prozesse
beteiligt sein, was die Rechnungsverwaltung zu einer komplexen Tätigkeit macht.

Sie finden die verschiedenen Artefakte Ihres Systems, indem Sie Fragen stellen wie:

Wer interagiert mit wem?
Wer macht was mit wem?
Mit solchen Fragen im Hinterkopf können Sie Aussagen machen. Lassen Sie uns die verschiedenen Artefakte in diesen
Aussagen hervorheben, damit deutlich wird, welche Teile für unser System wichtig sind.

Der Postdienst liefert eine Rechnung an das System.

Die Rechnung wird entweder nach einem Referenzcode oder manuell von einem Sortierer sortiert, um sicherzustellen, dass
sie in der richtigen Abteilung landet.

Die Rechnung wird von einem Genehmiger auf der Grundlage von Faktoren wie (zum Beispiel) Korrektheit und Höhe des
Betrags genehmigt oder abgelehnt.

Die Rechnung wird von einem Zahlungsabwickler unter Verwendung der angegebenen Zahlungsinformationen bezahlt.