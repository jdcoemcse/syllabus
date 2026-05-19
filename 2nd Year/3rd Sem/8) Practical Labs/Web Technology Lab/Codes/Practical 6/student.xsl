<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<xsl:template match="/">
    <html>
        <head>
            <style>
                table {
                    border-collapse: collapse;
                  }
                  th, td {
                    border: 1px solid #ddd;
                    padding: 10px;
                  }
                  tr:nth-child(1) {
                    background-color: cyan;
                  }
                  tr:not(:first-child) {
                    background-color: #ffe6e6; /* light pink */
                  }        
            </style>
        </head>
        <body>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>College Name</th>
                    <th>Branch</th>
                    <th>Year</th>
                    <th>Email</th>
                </tr>
                <xsl:for-each select="rtmnu/student">
                    <tr>
                        <td><xsl:value-of select="id"/></td>
                        <td><xsl:value-of select="name"/></td>
                        <td><xsl:value-of select="clgname"/></td>
                        <td><xsl:value-of select="branch"/></td>
                        <td><xsl:value-of select="joining"/></td>
                        <td><xsl:value-of select="email"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>