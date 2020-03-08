<map version="freeplane 1.7.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Import test" FOLDED="false" ID="ID_1723255651" CREATED="1283093380553" MODIFIED="1583261765174"><hook NAME="MapStyle">
    <properties show_icon_for_attributes="true" fit_to_viewport="false" edgeColorConfiguration="#808080ff,#808080ff,#808080ff,#808080ff,#808080ff" show_note_icons="true"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" MAX_WIDTH="600.0 px" COLOR="#000000" STYLE="as_parent">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="4" RULE="ON_BRANCH_CREATION"/>
<node TEXT="Instructions" POSITION="right" ID="ID_824740963" CREATED="1583678005652" MODIFIED="1583678007663">
<edge COLOR="#808080"/>
<node TEXT="Click View &gt; Node attributes &gt; Show all attributes" ID="ID_53931846" CREATED="1583678205461" MODIFIED="1583678243418"/>
<node TEXT="In Anki..." ID="ID_104509434" CREATED="1583678066096" MODIFIED="1583678069409">
<node TEXT="1. Create a &apos;Freeplane basic&apos; model in Anki" ID="ID_1976657161" CREATED="1583678009187" MODIFIED="1583678017582">
<node TEXT="Fields" ID="ID_1335136148" CREATED="1583678094593" MODIFIED="1583678098961">
<node TEXT="ID" ID="ID_60226868" CREATED="1583678102507" MODIFIED="1583678103092">
<node TEXT="has to be first" ID="ID_1312290943" CREATED="1583678107622" MODIFIED="1583678110101"/>
</node>
<node TEXT="Front" ID="ID_1083483892" CREATED="1583678099192" MODIFIED="1583678101428"/>
<node TEXT="Back" ID="ID_648780597" CREATED="1583678101554" MODIFIED="1583678102356"/>
</node>
</node>
<node TEXT="2. Click Tools &gt; Import mindmap" ID="ID_713570783" CREATED="1583678049585" MODIFIED="1583678133513"/>
<node TEXT="3. Click Browse and view cards in FreeplaneDeck deck" ID="ID_382222419" CREATED="1583678280162" MODIFIED="1583678289277"/>
</node>
<node TEXT="Try editing the cards in Freeplane and reimport" ID="ID_703508522" CREATED="1583678142281" MODIFIED="1583678267174"/>
</node>
<node TEXT="Deck" POSITION="right" ID="ID_793372572" CREATED="1415464979694" MODIFIED="1583262198781">
<edge COLOR="#00ff00"/>
<attribute NAME="anki:deck" VALUE="FreeplaneDeck"/>
<node TEXT="This is the front of card A" ID="ID_1194397559" CREATED="1415304958826" MODIFIED="1583678179420">
<attribute NAME="anki:model" VALUE="Freeplane basic"/>
<attribute NAME="anki:field:Front" VALUE="*"/>
<node TEXT="back of card A" ID="ID_624938500" CREATED="1415304964333" MODIFIED="1583678187579">
<attribute NAME="anki:field:Back" VALUE="This is the *"/>
</node>
</node>
<node TEXT="This is the front of card B" ID="ID_807505283" CREATED="1415304958826" MODIFIED="1583678197011">
<attribute NAME="anki:model" VALUE="Freeplane basic"/>
<attribute NAME="anki:field:Front" VALUE="*"/>
<attribute NAME="anki:field:Back" VALUE="This is the back of card B"/>
</node>
</node>
</node>
</map>
