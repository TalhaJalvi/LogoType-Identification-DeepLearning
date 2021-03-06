MZ?       ??  ?       @                                   ?   ? ?	?!?L?!This program cannot be run in DOS mode.
$       PE  L )8A`        ? !  :         X       `    @                       ?     2k   @?                           ?W  O    `  ?           D  ?!   ?                                                                       H           .text   8       :                    `.rsrc   ?   `      <              @  @.reloc      ?      B              @  B                ?W      H     ?U  0  	       P   ?4  U  ?                                   ?4  ????   ?   lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet          PADPADP,v?    ?   "i m a g e m a n i f e s t . x s d     !?3  <?xml version="1.0" encoding="utf-8"?>
<xs:schema id="ImageManifestSchema" elementFormDefault="qualified" targetNamespace="http://schemas.microsoft.com/VisualStudio/ImageManifestSchema/2014" xmlns="http://schemas.microsoft.com/VisualStudio/ImageManifestSchema/2014" xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <xs:simpleType name="ST_Guid">
    <!-- Any attribute with this type can have a guid with or without braces as valid entries. -->
    <xs:union>
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <!-- Guid w/ Braces Pattern: {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX} -->
          <xs:pattern value="\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}"/>
        </xs:restriction>
      </xs:simpleType>
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <!-- Guid w/o Braces Pattern: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX -->
          <xs:pattern value="[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:union>
  </xs:simpleType>

  <xs:simpleType name="ST_GuidValue">
    <!-- Any attribute with this type can have a guid or symbol as valid entries. -->
    <xs:union memberTypes="ST_Guid ST_SymbolReference"/>
  </xs:simpleType>

  <xs:simpleType name="ST_IdValue">
    <!-- Any attribute with this type can have an int or symbol as valid entries. -->
    <xs:union memberTypes="ST_NonNegativeInt ST_SymbolReference"/>
  </xs:simpleType>

  <xs:simpleType name="ST_MinLengthString">
    <xs:restriction base="xs:string">
      <xs:minLength value="1"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="ST_NativeType">
    <xs:union>
      <!-- This part of the enumeration allows VS Intellisense to suggest values for elements using this type -->
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="PNG"/>
          <xs:enumeration value="XAML"/>
        </xs:restriction>
      </xs:simpleType>
      <!-- This part of the enumeration allows elements using this type to enter case-insensitive enumeration values -->
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:pattern value="[Pp][Nn][Gg]"/>
          <xs:pattern value="[Xx][Aa][Mm][Ll]"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:union>
  </xs:simpleType>
    
  <xs:simpleType name="ST_NonNegativeInt">
    <xs:restriction base="xs:int">
      <xs:minInclusive value="0"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="ST_PositiveInt">
    <xs:restriction base="xs:int">
      <xs:minExclusive value="0"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="ST_SourceBackgroundType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Light"/>
      <xs:enumeration value="Dark"/>
      <xs:enumeration value="HighContrast"/>
      <xs:enumeration value="HighContrastLight"/>
      <xs:enumeration value="HighContrastDark"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="ST_SymbolName">
    <xs:restriction base="xs:string">
      <!-- Symbol Name Pattern: SymbolName follows the same rules as C-based identifiers -->
      <!-- The first char is letter or underscore, and the rest of the identifier can contain letters, numbers, and underscores-->
      <xs:pattern value="[a-zA-Z_]{1}[0-9a-zA-Z_]*"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="ST_SymbolReference">
    <xs:restriction base="xs:string">
      <!-- Symbol Reference Pattern: $(<SymbolName>) where <SymbolName> follows the same rules as C-based identifiers -->
      <!-- The first char is letter or underscore, and the rest of the identifier can contain letters, numbers, and underscores-->
      <xs:pattern value="\$\([a-zA-Z_]{1}[0-9a-zA-Z_]*\)"/>
    </xs:restriction>
  </xs:simpleType>
  
  <xs:element name="ImageManifest">
    <xs:complexType>
      <xs:all>
        <xs:element minOccurs="0" name="Symbols">
          <xs:complexType>
            <xs:choice minOccurs="0" maxOccurs="unbounded">
              <xs:annotation>
                <xs:documentation>Defines a symbol that can be used in place of hard-coded values.</xs:documentation>
              </xs:annotation>
              <xs:element name="Import">
                <xs:annotation>
                  <xs:documentation>[Optional] Imports the symbols from another manifest.</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                  <xs:attribute name="Manifest" use="required" type="ST_MinLengthString"/>
                </xs:complexType>
              </xs:element>
              <xs:element name="Guid">
                <xs:annotation>
                  <xs:documentation>[Optional] The symbol is a placeholder for a guid.</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                  <xs:attribute name="Name" use="required" type="ST_SymbolName"/>
                  <xs:attribute name="Value" use="required" type="ST_Guid"/>
                </xs:complexType>
              </xs:element>
              <xs:element name="ID">
                <xs:annotation>
                  <xs:documentation>[Optional] The symbol is a placeholder for an ID.</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                  <xs:attribute name="Name" use="required" type="ST_SymbolName"/>
                  <xs:attribute name="Value" use="required" type="ST_NonNegativeInt"/>
                </xs:complexType>
              </xs:element>
              <xs:element name="String">
                <xs:annotation>
                  <xs:documentation>[Optional] The symbol is a placeholder for an arbitrary string.</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                  <xs:attribute name="Name" use="required" type="ST_SymbolName"/>
                  <xs:attribute name="Value" use="required" type="xs:string"/>
                </xs:complexType>
              </xs:element>
            </xs:choice>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="0" name="Images">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="0" maxOccurs="unbounded" name="Image">
                <xs:annotation>
                  <xs:documentation>Defines an image that can be referenced by a moniker.</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                  <xs:sequence>
                    <xs:element maxOccurs="unbounded" name="Source">
                      <xs:annotation>
                        <xs:documentation>[Required] [Minimum: 1] Defines a single image source asset.</xs:documentation>
                      </xs:annotation>
                      <xs:complexType>
                        <xs:sequence>
                          <xs:choice minOccurs="0">
                            <xs:element name="Size">
                              <xs:annotation>
                                <xs:documentation>[Optional] The source will be used only for the the given value. (If specified, this must be the first child of the source)</xs:documentation>
                              </xs:annotation>
                              <xs:complexType>
                                <xs:attribute name="Value" use="required" type="ST_PositiveInt"/>
                              </xs:complexType>
                            </xs:element>
                            <xs:element name="SizeRange">
                              <xs:annotation>
                                <xs:documentation>[Optional] The source will be used between the min/max size inclusively. (If specified, this must be the first child of the source)</xs:documentation>
                              </xs:annotation>
                              <xs:complexType>
                                <xs:attribute name="MinSize" use="required" type="ST_PositiveInt"/>
                                <xs:attribute name="MaxSize" use="required" type="ST_PositiveInt"/>
                              </xs:complexType>
                            </xs:element>
                            <xs:element name="Dimensions">
                              <xs:annotation>
                                <xs:documentation>[Optional] The source will be used only for the given width and height. (If specified, this must be the first child of the source)</xs:documentation>
                              </xs:annotation>
                              <xs:complexType>
                                <xs:attribute name="Width" use="required" type="ST_PositiveInt"/>
                                <xs:attribute name="Height" use="required" type="ST_PositiveInt"/>
                              </xs:complexType>
                            </xs:element>
                            <xs:element name="DimensionRange">
                              <xs:annotation>
                                <xs:documentation>[Optional] The source will be used between the min/max width/height inclusively. (If specified, this must be the first child of the source)</xs:documentation>
                              </xs:annotation>
                              <xs:complexType>
                                <xs:attribute name="MinWidth" use="required" type="ST_PositiveInt"/>
                                <xs:attribute name="MinHeight" use="required" type="ST_PositiveInt"/>
                                <xs:attribute name="MaxWidth" use="required" type="ST_PositiveInt"/>
                                <xs:attribute name="MaxHeight" use="required" type="ST_PositiveInt"/>
                              </xs:complexType>
                            </xs:element>
                          </xs:choice>
                          <xs:element minOccurs="0" name="NativeResource">
                            <xs:annotation>
                              <xs:documentation>[Optional] The source is defined in a native assembly with the given resource ID and type. (If a size[range] or dimension[range] is specified for the source, this, if specified, must appear after other child.)</xs:documentation>
                            </xs:annotation>
                            <xs:complexType>
                              <xs:attribute name="ID" use="required" type="ST_IdValue"/>
                              <xs:attribute name="Type" use="required" type="ST_NativeType"/>
                            </xs:complexType>
                          </xs:element>
                        </xs:sequence>
                        <xs:attribute name="Uri" use="required" type="ST_MinLengthString"/>
                        <xs:attribute name="Background" use="optional" type="ST_SourceBackgroundType"/>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                  <xs:attribute name="Guid" use="required" type="ST_GuidValue"/>
                  <xs:attribute name="ID" use="required" type="ST_IdValue"/>
                  <xs:attribute name="AllowColorInversion" use="optional" type="xs:boolean"/>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="0" name="ImageLists">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="0" maxOccurs="unbounded" name="ImageList">
                <xs:annotation>
                  <xs:documentation>Defines a collection of images that can be returned in a single image strip.</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                  <xs:sequence>
                    <xs:element maxOccurs="unbounded" name="ContainedImage">
                      <xs:annotation>
                        <xs:documentation>[Required] [Minimum: 1] An image in the image strip. The order in the image list determines the order in the generated image strip.</xs:documentation>
                      </xs:annotation>
                      <xs:complexType>
                        <xs:attribute name="Guid" use="required" type="ST_GuidValue"/>
                        <xs:attribute name="ID" use="required" type="ST_IdValue"/>
                        <xs:attribute name="External" use="optional" type="xs:boolean"/>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                  <xs:attribute name="Guid" use="required" type="ST_GuidValue"/>
                  <xs:attribute name="ID" use="required" type="ST_IdValue"/>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:all>
      <xs:attribute name="PackageGuid" use="optional" type="ST_GuidValue"/>
    </xs:complexType>
  </xs:element>
  
</xs:schema>
???.pf?F?Ϊ*???|,n2;?Y?@?u??-k?!???s???Ý4?;ݯ????%?%?l??:?іD??7HC?v????W???p"?O?????(u??1??2?a??΃ ?p?^?&??//( BSJB         v4.0.30319     l   d   #~  ?   ?   #Strings    t     #US |     #GUID   ?  ?   #Blob               ?%3                 p                 ?             
 9        <      <Module> Microsoft.VisualStudio.Setup.Imaging.resources ru Microsoft.VisualStudio.Setup.Imaging.g.ru.resources Microsoft.VisualStudio.Setup.Imaging.resources.dll         _M?c??BI???????? ?? $  ?  ?      $  RSA1     ??WĮ???.???????j쏇?vl?L???;??????ݚ?6!?r<?????w??wO)?2?????!?????d\L????(]b,?e,??=t]o-??~^?Ė=&?Ce m??4MZғ ?W          ?W                          ?W            _CorDllMain mscoree.dll     ?%  @                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ?                  0  ?               	  H   X`  ?          ?4   V S _ V E R S I O N _ I N F O     ???   	  ?o	                             D    V a r F i l e I n f o     $    T r a n s l a t i o n     ??   S t r i n g F i l e I n f o   ?   0 4 1 9 0 4 b 0   l *  C o m m e n t s   >=B59=5@  4;O  7028A8<>AB59  A;C61K  >1@07>2  6   C o m p a n y N a m e     09:@>A>DB    ? .  F i l e D e s c r i p t i o n     0AB@>9:0  @01>BK  A  >1@070<8  4;O  V i s u a l   S t u d i o   >   F i l e V e r s i o n     2 . 9 . 3 3 5 2 . 2 8 5 7 9     ? 3  I n t e r n a l N a m e   M i c r o s o f t . V i s u a l S t u d i o . S e t u p . I m a g i n g . r e s o u r c e s . d l l     ? E  L e g a l C o p y r i g h t   ?   >@?>@0F8O  09:@>A>DB  ( M i c r o s o f t   C o r p o r a t i o n ) .   A5  ?@020  70I8I5=K.     ? 3  O r i g i n a l F i l e n a m e   M i c r o s o f t . V i s u a l S t u d i o . S e t u p . I m a g i n g . r e s o u r c e s . d l l     <   P r o d u c t N a m e     V i s u a l   S t u d i o   6 	  P r o d u c t V e r s i o n   2 . 9 . 3 3 5 2                                                                                                                                                                                                                                                                                                              P     8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ?!    0?!s	*?H????!d0?!`10	`?He 0\
+?7?N0L0
+?70	 ??? 010	`?He  >T?Lߴ?0?f?H#J???ej?x??SdV??????r0??0???3  ލV?Z???g    ?0	*?H?? 0~10	UUS10U
Washington10URedmond10U
Microsoft Corporation1(0&UMicrosoft Code Signing PCA 20100201215212420Z211202212420Z0t10	UUS10U
Washington10URedmond10U
Microsoft Corporation10UMicrosoft Corporation0?"0	*?H?? ? 0?
? ????I?$H?^???? B?վ??[sq?????=U???hM?lZ^?Y9
R??g???*???=o??M?j?&??h?X?S?X?F???ؽ?h?㦳Vv	?>???e|XE,FB?M??5???????Y'??L??T.??uXr???~ݜJl,_?8?R??|?Q???/t
t?1ܒ??t?Z??? ?U$߭Qc??o?zz2>J????{1??8?:?:?????1?A?
%o ??y0?u0U%0
+?7=+0U$?;??Z????n???w?uL?0PUI0G?E0C1)0'U Microsoft Operations Puerto Rico10U230865+4631330U#0???_{?" X?rN??!t#2???0VUO0M0K?I?G?Ehttp://crl.microsoft.com/pki/crl/products/MicCodSigPCA_2010-07-06.crl0Z+N0L0J+0?>http://www.microsoft.com/pki/certs/MicCodSigPCA_2010-07-06.crt0U?0 0	*?H?? ? <_??M'?]?m?mDĝ<:??A???	(???DɱhM??M????????XV?? {[??O??pl????%??Y?~?
&????t??wfz???`??"???'???#?????n?o]??<?W??7?]~e???/]Vv?9L?r㺋F?!?M????????uY????9j1?,?Xɟt},ɺ?[??`?>*???!?I?ӧ0????ިȐ~?I%v????\?˴??!lt??}%΃N???)??0?p0?X?
aRL     0	*?H?? 0??10	UUS10U
Washington10URedmond10U
Microsoft Corporation1200U)Microsoft Root Certificate Authority 20100100706204017Z250706205017Z0~10	UUS10U
Washington10URedmond10U
Microsoft Corporation1(0&UMicrosoft Code Signing PCA 20100?"0	*?H?? ? 0?
? ?dPyg????	 L????Vh?D???XO??v|mE??9?????e??ҏ?D??e??,U??}?.+?A+??KnILk???q?͵K???̈?k?:??&????4?W?]I??*.Յ?Y????+?t?+?;F??FI?fT???UbWr?g?% 4?]???^?(??ղ???cӲ??Ȋ&
Y????5L??R[?????HwօG???????j-\`ƴ*[?#_E?o7?3?j?M?jfcx??0ϕ ???0??0	+?7 0U??_{?" X?rN??!t#2???0	+?7
 S u b C A0U?0U?0?0U#0???Vˏ??\bh?=??[?Κ?0VUO0M0K?I?G?Ehttp://crl.microsoft.com/pki/crl/products/MicRooCerAut_2010-06-23.crl0Z+N0L0J+0?>http://www.microsoft.com/pki/certs/MicRooCerAut_2010-06-23.crt0??U ??0??0??	+?7.0??0=+1http://www.microsoft.com/PKI/docs/CPS/default.htm0@+042  L e g a l _ P o l i c y _ S t a t e m e n t . 0	*?H?? ? t?WO){??x?P?"?	?????4?*,?????Ͽ???4?ہ?? ??5o??y?w??????Na??Z#???bQEg??<??0??9@???!)奡i?"??t???GC?S??0i??% moa????r ,i?v=Qۦ9H?7am?S˧?a¿⃫?k???}(Q??JQ??lȷJi????~?Ip????rGc??֢????D?c??i??F?z???!?{?#-?A˿L?ﱜ?"KI?n??v[?Sy??????=s5?<?T?RGj???Ҏڙg^2??7???u????ZW?¿????-????'ӵ^i???$gs?MO??V?z??RM?wO??????B	?v?#Vx"&6?ʱ?n????G3b??ɑ3_q@??e?"?B!%?-`?7?A?*?a<?h`R??G???@??w>??SP8??f3'9x?6?N?_??=GS????a=*ג,?7Z>@B1??V??$]Q?jy??????{%qD?j????#??u?1?t0?p0??0~10	UUS10U
Washington10URedmond10U
Microsoft Corporation1(0&UMicrosoft Code Signing PCA 20103  ލV?Z???g    ?0	`?He ???0	*?H??	1
+?70
+?710
+?70/	*?H??	1" ??Em"??q2A??b?>IE?=?X??=??i?0B
+?71402?? M i c r o s o f t??http://www.microsoft.com0	*?H?? ? 2bM????QG??+Jmg?4??U:3?E?h???]?"3N?B??&K??>?G?y3??խ??Ѓۆ??&?t?WO???0?8?#W?S????R?}??8d?%g????lA*?????p?ֽ?Q?q^?\6??I`l?????ӡH??????z?W?(?:???ڦ???E+ь.w?NR??fH_u_ha?:!j??IF8*b?{_??c`e;?.?쮗???Qƨ?i?m;?~E?UK?@?Rcʃ?S???
???0??
+?71??0??	*?H?????0??10	`?He 0?Y*?H??	??H?D0?@
+?Y
010	`?He   ?rI?jd?G??k??2?	t???|[;???'??:`<?8?20210304194250.393Z0????ؤ??0??10	UUS10U
Washington10URedmond10U
Microsoft Corporation1-0+U$Microsoft Ireland Operations Limited1&0$UThales TSS ESN:8D41-4BF7-B3B71%0#UMicrosoft Time-Stamp Service??M0??0???3  :??1?wII?    :0	*?H?? 0|10	UUS10U
Washington10URedmond10U
Microsoft Corporation1&0$UMicrosoft Time-Stamp PCA 20100201015172822Z220112172822Z0??10	UUS10U
Washington10URedmond10U
Microsoft Corporation1-0+U$Microsoft Ireland Operations Limited1&0$UThales TSS ESN:8D41-4BF7-B3B71%0#UMicrosoft Time-Stamp Service0?"0	*?H?? ? 0?
? ?_$?_??	L?؟??9?*qj?'?W&$??r,> ջfx???ô???(;'n?@}xS??Y?J?Z\ Y?ݽy??&?W??r?X??<?Ӊ{???W?W_??Kb?/??8??@????ۆ??L?L????Vr?vyB?FxsZ^?Ζ??nUElŎ?k???Q?f??I?.?@[b)ur?@n??	A?˸.?`??????d?q2?????k???????)???~?]Xv??l??	ϹH-9???(J2) ??0?0UV??_k??ou??	?E??0U#0??c:\?1??C{|F?3hZ?mU0VUO0M0K?I?G?Ehttp://crl.microsoft.com/pki/crl/products/MicTimStaPCA_2010-07-01.crl0Z+N0L0J+0?>http://www.microsoft.com/pki/certs/MicTimStaPCA_2010-07-01.crt0U?0 0U%0
+0	*?H?? ? ^7?>?-?x|mJNn@?H?m???+?.??9Z? A?v	4??Nhs??ײ< ?K???:*?G'?Ĩb酐=?5??Q??uvǃ????c%d?ԓ2?c?2;??]????L'?V?&?????????,%񥪽
??"????'??{5:??2e??	n<?m?E|??e؆`ʾ\4草:?:??5????m@???????Y?R??¾A??0'?e???槡Y?bL??p??)???E?P?tX?Z?#m) L?ٳ0?q0?Y?
a	?*     0	*?H?? 0??10	UUS10U
Washington10URedmond10U
Microsoft Corporation1200U)Microsoft Root Certificate Authority 20100100701213655Z250701214655Z0|10	UUS10U
Washington10URedmond10U
Microsoft Corporation1&0$UMicrosoft Time-Stamp PCA 20100?"0	*?H?? ? 0?
? ??w?: ?????i?ktTե
 ????|hK,_???a?v?>f+[?S'1A??	?|a0Y?0D?`??TC?M?8?Bݓ??s0W&??E???G?Ϳ$`2X`F?XG?2?tag?_?T?ϓL??Ħ]?an(??????a?F?'$gr!??Kd?Pb?]?w=?Wu???BM@Q??>g?f??D~??K?n??ʱ??z*
1??N???5?x????<?/D????d??? 	?x?????D]^?O"M ???0??0	+?7 0U?c:\?1??C{|F?3hZ?mU0	+?7
 S u b C A0U?0U?0?0U#0???Vˏ??\bh?=??[?Κ?0VUO0M0K?I?G?Ehttp://crl.microsoft.com/pki/crl/products/MicRooCerAut_2010-06-23.crl0Z+N0L0J+0?>http://www.microsoft.com/pki/certs/MicRooCerAut_2010-06-23.crt0??U ???0??0??	+?7.0??0=+1http://www.microsoft.com/PKI/docs/CPS/default.htm0@+042  L e g a l _ P o l i c y _ S t a t e m e n t . 0	*?H?? ? ??Q??????q=???!o?????1??????Wm0???f?j????x?Ǩ?%????kTW+Q?D??S???`?v?@@A??\?\?^5?$VKt?Bȯ???7}Z???yJ?R ?8?/y?e٩?k?????z oK0D$"<?????Y)????p?2J'?U?/????3?b_??W@??Ιf???jb??J?&?9?Jqc?{!mÜ??<?}?j?x?m?????8ؔ?ƥ
??????B?????"8 ?%?d????~cY%z.9Wv?q????a?˚?G????ͧ??}???;q	?]t?"aڰPo??? ??1??:?eGx???H???r~akow??˧	?9????؂?r???????*T9?[??U?z?s;??-???3.)??/T'!?ȬN?(???ۖ??B???AM???*??f0ӻt2K?c{???/?!?Y???D<?Pqס??U?i?W???0????M??]O??8/??X.??P5??	'ճ~5??6??_??t?I???0?@0? ??ؤ??0??10	UUS10U
Washington10URedmond10U
Microsoft Corporation1-0+U$Microsoft Ireland Operations Limited1&0$UThales TSS ESN:8D41-4BF7-B3B71%0#UMicrosoft Time-Stamp Service?#
0+ %????X?ܯb>5??5????0???~0|10	UUS10U
Washington10URedmond10U
Microsoft Corporation1&0$UMicrosoft Time-Stamp PCA 20100	*?H??  ??]?0"20210304212357Z20210305212357Z0w0=
+?Y
1/0-0
 ??]? 0
 ??0 ?0
 ???m 06
+?Y
1(0&0
+?Y
?
0 ? ?
0 ??0	*?H?? ?? $?7s5???~????????k???Hʓ]&̰???n????5?^ʟ???ړ?*?LgӋK[	?PI?ٱ"?
 ~:$?{?>???O????DSmу????M_?/W?t???+?? 4F?][?ߦb????1?0?	0??0|10	UUS10U
Washington10URedmond10U
Microsoft Corporation1&0$UMicrosoft Time-Stamp PCA 20103  :??1?wII?    :0	`?He ??J0	*?H??	1*?H??	0/	*?H??	1" ??Vrbc?>f???nZQ;Zk?\c?? ?=NI ?b0??*?H??	/1??0??0??0?? ??Є?,_??/~?9????\??(???iC|?m0??0???~0|10	UUS10U
Washington10URedmond10U
Microsoft Corporation1&0$UMicrosoft Time-Stamp PCA 20103  :??1?wII?    :0" ?=.??g?<?????Wv?????Ti??????0	*?H?? ? ???ۄL&c??JK??n?7?'???3"?1???@???Q??g???????DO??R??r??H?y!U???=gNS???-??R33?kR[7?a6Yb?h?+&?dA??ܚ?}??,5???????????j
 ?ck*??%??"?c4?????[N??;ֳ|??[????,G=????????٠'2?wP@CO,???H??&̼????[?-??	R???o?ua^c??0??,?? ?~6?T?܁yt????!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 