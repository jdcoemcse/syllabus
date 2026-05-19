<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  
  <xsl:template match="/">
    <html>
      <head>
        <style>
          table,th,td{
            border: 1px solid black;
            border-collapse: collapse;
            padding: 2rem;
          }
          .author{
            text-transform: uppercase;
          }
          
        </style>
        
      </head>
      <body>
        <table>
          <tr bgcolor="#848884">
            <th>Book Name</th>
            <th>Author Name</th>
            <th>Publisher</th>
            <th>ISBN</th>
            <th>Edition</th>
            <th>Price</th>
          </tr>
          <xsl:for-each select="bookstore/book">
            <tr>
              <td bgcolor="#F67280"><xsl:value-of select="name" /></td>
              <td bgcolor="#87CEEB"><b><xsl:value-of select="author" /></b></td>
              <td bgcolor="#77DD77"><xsl:value-of select="publisher" /></td>
              <td bgcolor="#D291BC"><xsl:value-of select="isbn" /></td>
              <td bgcolor="#E6E6FA"><xsl:value-of select="edition" /></td>
              <td bgcolor="#FFFAA0"><xsl:value-of select="price" /></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>