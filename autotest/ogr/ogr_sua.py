#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  GDAL/OGR Test Suite
# Purpose:  Test read functionality for OGR SUA driver.
# Author:   Even Rouault <even dot rouault at mines dash paris dot org>
#
###############################################################################
# Copyright (c) 2010, Even Rouault <even dot rouault at mines-paris dot org>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################



import gdaltest
import ogrtest
from osgeo import ogr
import pytest

###############################################################################
# Basic test


def test_ogr_sua_1():

    ds = ogr.Open('data/za.sua')
    assert ds is not None, 'cannot open dataset'

    lyr = ds.GetLayer(0)
    assert lyr is not None, 'cannot find layer'

    feat = lyr.GetNextFeature()
    geom = feat.GetGeometryRef()
    if ogrtest.check_feature_geometry(feat, 'POLYGON ((24.760277777777777 -28.466666666666683,24.766895312434809 -28.46671727367243,24.773510850527718 -28.466869079419723,24.780122395865373 -28.467122038103,24.786727953485673 -28.467476073394735,24.793325530310469 -28.467931078467672,24.799913135516679 -28.468486916026166,24.806488781187785 -28.469143418346533,24.813050482985464 -28.469900387326192,24.819596260561802 -28.47075759454188,24.826124138325216 -28.47171478131645,24.832632145879771 -28.472771658795054,24.839118318703743 -28.47392790802968,24.845580698630823 -28.475183180072875,24.852017334528803 -28.476537096080108,24.858426282776776 -28.47798924742105,24.86480560789666 -28.479539195799475,24.871153383126547 -28.481186473381939,24.877467690931773 -28.482930582935339,24.883746623625481 -28.48477099797276,24.889988283903538 -28.486707162908274,24.896190785431472 -28.48873849322014,24.902352253349676 -28.490864375622735,24.908470824878808 -28.493084168246597,24.914544649847166 -28.495397200827426,24.920571891246279 -28.497802774903008,24.926550725747585 -28.500300164018839,24.932479344288705 -28.502888613941764,24.938355952571698 -28.505567342882131,24.944178771610126 -28.508335541723795,24.949946038264724 -28.511192374262492,24.955656005751909 -28.514136977452182,24.961306944165695 -28.517168461659423,24.966897141013046 -28.520285910925423,24.972424901704478 -28.523488383236369,24.977888550056022 -28.526774910801166,24.983286428814758 -28.530144500336959,24.988616900132001 -28.533596133362522,24.99387834606733 -28.537128766498796,24.999069169069763 -28.540741331777156,25.004187792453038 -28.544432736955102,25.009232660883608 -28.548201865839104,25.014202240830937 -28.552047578614662,25.019095021044684 -28.555968712183585,25.02390951301135 -28.559964080508252,25.028644251401499 -28.564032474962829,25.033297794511821 -28.568172664691346,25.037868724701763 -28.572383396972441,25.042355648839958 -28.576663397590849,25.046757198702647 -28.581011371215411,25.051072031428639 -28.585426001783489,25.055298829890791 -28.589905952891769,25.059436303127992 -28.594449868193294,25.063483186732412 -28.599056371800572,25.067438243238151 -28.603724068694731,25.071300262513763 -28.608451545140568,25.075068062113562 -28.613237369107495,25.078740487674832 -28.618080090695855,25.082316413248837 -28.622978242569175,25.085794741684015 -28.627930340391472,25.089174404927817 -28.632934883270281,25.092454364404489 -28.637990354204419,25.095633611313403 -28.643095220537134,25.098711166955503 -28.64824793441413,25.10168608305365 -28.653446933246229,25.104557442038406 -28.658690640176914,25.107324357344936 -28.663977464554407,25.109985973715663 -28.669305802407834,25.112541467439499 -28.674674036928209,25.114990046654459 -28.680080538952993,25.117330951578985 -28.685523667455101,25.119563454781961 -28.691001770035456,25.121686861395737 -28.696513183419484,25.123700509365641 -28.702056233957038,25.125603769666306 -28.707629238125719,25.127396046506441 -28.713230503037792,25.129076777527761 -28.718858326949757,25.130645434008265 -28.724510999775319,25.13210152102771 -28.730186803601043,25.133444577652867 -28.735884013204668,25.134674177090211 -28.741600896576003,25.135789926836566 -28.7473357154403,25.136791468828061 -28.753086725783632,25.137678479562659 -28.758852178380579,25.138450670228519 -28.764630319323757,25.139107786806342 -28.770419390555091,25.139649610175514 -28.776217630398676,25.140075956205322 -28.782023274095195,25.140386675823155 -28.787834554337508,25.140581655100206 -28.793649701807396,25.140660815291394 -28.799466945713419,25.140624112899374 -28.805284514329315,25.140471539698027 -28.811100635533307,25.140203122769478 -28.816913537347659,25.139818924509857 -28.822721448478802,25.139319042644907 -28.828522598857376,25.138703610206345 -28.834315220178425,25.137972795537667 -28.840097546441314,25.137126802248048 -28.845867814489324,25.136165869182687 -28.85162426454886,25.135090270371048 -28.857365140767754,25.133900314962272 -28.863088691752992,25.132596347160835 -28.868793171107171,25.131178746139458 -28.874476837963954,25.129647925945786 -28.880137957522209,25.128004335404732 -28.885774801578492,25.126248457993494 -28.891385649057952,25.124380811721167 -28.896968786543397,25.122401948989488 -28.902522508802292,25.120312456446726 -28.908045119311723,25.118112954838665 -28.913534930780742,25.11580409880861 -28.918990265670601,25.113386576755399 -28.924409456711885,25.110861110617904 -28.92979084741917,25.108228455676212 -28.935132792602516,25.105489400347579 -28.940433658875676,25.102644765960211 -28.94569182516129,25.099695406505884 -28.950905683192275,25.096642208420011 -28.956073638009698,25.093486090307582 -28.961194108456937,25.090228002679709 -28.96626552766962,25.086868927687608 -28.97128634356163,25.083409878829617 -28.976255019306763,25.079851900655964 -28.981170033815886,25.076196068457499 -28.986029882209536,25.072443487959553 -28.990833076285767,25.068595294982366 -28.995578144983043,25.064652655115509 -29.000263634838049,25.060616763368554 -29.004888110438372,25.05648884380911 -29.009450154869668,25.052270149197888 -29.013948370157522,25.04796196062637 -29.018381377703292,25.043565587113235 -29.022747818714564,25.039082365218423 -29.027046354629377,25.034513658643014 -29.031275667534388,25.029860857809823 -29.035434460576823,25.025125379446433 -29.039521458370103,25.020308666156058 -29.043535407392909,25.015412185972465 -29.047475076381517,25.010437431908937 -29.051339256715593,25.005385921523313 -29.055126762796746,25.000259196426232 -29.05883643242025,24.995058821820685 -29.062467127139698,24.98978638601983 -29.066017732624076,24.984443499974287 -29.069487159007593,24.979031796736475 -29.072874341232009,24.973552930996892 -29.076178239381264,24.96800857854516 -29.079397839008323,24.962400435777845 -29.082532151454132,24.95673021914298 -29.085580214158654,24.950999664626245 -29.088541090963787,24.945210527202558 -29.09141387240804,24.939364580306272 -29.094197676012925,24.933463615254794 -29.096891646561062,24.927509440705947 -29.09949495636549,24.921503882088025 -29.102006805530834,24.915448781031092 -29.104426422205322,24.909345994796006 -29.10675306282441,24.90319739567629 -29.108986012345341,24.897004870446018 -29.11112458447279,24.890770319697953 -29.113168121875631,24.884495657344228 -29.115115996394422,24.878182809944395 -29.116967609239822,24.871833716110423 -29.11872239118189,24.865450325918069 -29.120379802729857,24.859034600277788 -29.121939334302667,24.852588510335149 -29.123400506390141,24.846114036796582 -29.124762869704583,24.83961316938128 -29.1260260053228,24.8330879061436 -29.127189524818803,24.826540252848378 -29.128253070386421,24.819972222345168 -29.129216314952828,24.813385833911177 -29.1300789622818,24.806783112687896 -29.130840747067623,24.800166088946376 -29.131501435018961,24.793536797471898 -29.132060822933184,24.786897276912615 -29.132518738760538,24.780249569276663 -29.132875041658693,24.773595719053805 -29.133129622037345,24.766937772515039 -29.133282401592936,24.760277777777777 -29.13333333333334,24.753617783040514 -29.133282401592936,24.746959836501748 -29.133129622037345,24.740305986278891 -29.132875041658693,24.733658278642938 -29.132518738760538,24.727018758083656 -29.132060822933184,24.720389466609177 -29.131501435018961,24.713772442867658 -29.130840747067623,24.707169721644377 -29.1300789622818,24.700583333210385 -29.129216314952828,24.694015302707175 -29.128253070386421,24.687467649411953 -29.127189524818803,24.680942386174273 -29.1260260053228,24.674441518758972 -29.124762869704583,24.667967045220404 -29.123400506390141,24.661520955277766 -29.121939334302667,24.655105229637485 -29.120379802729857,24.64872183944513 -29.11872239118189,24.642372745611159 -29.116967609239822,24.636059898211325 -29.115115996394422,24.6297852358576 -29.113168121875631,24.623550685109535 -29.11112458447279,24.617358159879263 -29.108986012345341,24.611209560759548 -29.10675306282441,24.605106774524462 -29.104426422205322,24.599051673467528 -29.102006805530834,24.593046114849606 -29.09949495636549,24.587091940300759 -29.096891646561062,24.581190975249282 -29.094197676012925,24.575345028352995 -29.09141387240804,24.569555890929308 -29.088541090963787,24.563825336412574 -29.085580214158654,24.558155119777709 -29.082532151454132,24.552546977010394 -29.079397839008323,24.547002624558662 -29.076178239381264,24.541523758819078 -29.072874341232009,24.536112055581267 -29.069487159007593,24.530769169535724 -29.066017732624076,24.525496733734869 -29.062467127139698,24.520296359129322 -29.05883643242025,24.51516963403224 -29.055126762796746,24.510118123646617 -29.051339256715593,24.505143369583088 -29.047475076381517,24.500246889399495 -29.043535407392909,24.495430176109121 -29.039521458370103,24.490694697745731 -29.035434460576823,24.486041896912539 -29.031275667534388,24.48147319033713 -29.027046354629377,24.476989968442318 -29.022747818714564,24.472593594929183 -29.018381377703292,24.468285406357666 -29.013948370157522,24.464066711746444 -29.009450154869668,24.459938792187 -29.004888110438372,24.455902900440044 -29.000263634838049,24.451960260573188 -28.995578144983043,24.448112067596 -28.990833076285767,24.444359487098055 -28.986029882209536,24.44070365489959 -28.981170033815886,24.437145676725937 -28.976255019306763,24.433686627867946 -28.97128634356163,24.430327552875845 -28.96626552766962,24.427069465247971 -28.961194108456937,24.423913347135542 -28.956073638009698,24.42086014904967 -28.950905683192275,24.417910789595343 -28.94569182516129,24.415066155207974 -28.940433658875676,24.412327099879342 -28.935132792602516,24.409694444937649 -28.92979084741917,24.407168978800154 -28.924409456711885,24.404751456746943 -28.918990265670601,24.402442600716888 -28.913534930780742,24.400243099108827 -28.908045119311723,24.398153606566066 -28.902522508802292,24.396174743834386 -28.896968786543397,24.394307097562059 -28.891385649057952,24.392551220150821 -28.885774801578492,24.390907629609767 -28.880137957522209,24.389376809416095 -28.874476837963954,24.387959208394719 -28.868793171107171,24.386655240593281 -28.863088691752992,24.385465285184505 -28.857365140767754,24.384389686372867 -28.85162426454886,24.383428753306539 -28.845867814489324,24.382582760017886 -28.840097546441314,24.381851945350171 -28.834315220178425,24.381236512910647 -28.828522598857376,24.380736631045696 -28.822721448478802,24.380352432786076 -28.816913537347659,24.380084015857527 -28.811100635533307,24.379931442656179 -28.805284514329315,24.379894740264159 -28.799466945713419,24.379973900455347 -28.793649701807396,24.380168879732398 -28.787834554337508,24.380479599350231 -28.782023274095195,24.380905945380039 -28.776217630398676,24.381447768749211 -28.770419390555091,24.382104885327035 -28.764630319323757,24.382877075992894 -28.758852178380579,24.383764086727492 -28.753086725783632,24.384765628718988 -28.7473357154403,24.385881378465342 -28.741600896576003,24.387110977902687 -28.735884013204668,24.388454034527843 -28.730186803601043,24.389910121547288 -28.724510999775319,24.391478778027793 -28.718858326949757,24.393159509049113 -28.713230503037792,24.394951785889248 -28.707629238125719,24.396855046189913 -28.702056233957038,24.398868694159816 -28.696513183419484,24.400992100773593 -28.691001770035456,24.403224603976568 -28.685523667455101,24.405565508901095 -28.680080538952993,24.408014088116055 -28.674674036928209,24.410569581839891 -28.669305802407834,24.413231198210617 -28.663977464554407,24.415998113517148 -28.658690640176914,24.418869472501903 -28.653446933246229,24.42184438860005 -28.64824793441413,24.424921944242151 -28.643095220537134,24.428101191151065 -28.637990354204419,24.431381150627736 -28.632934883270281,24.434760813871538 -28.627930340391472,24.438239142306717 -28.622978242569175,24.441815067880722 -28.618080090695855,24.445487493441991 -28.613237369107495,24.449255293041791 -28.608451545140568,24.453117312317403 -28.603724068694731,24.457072368823141 -28.599056371800572,24.461119252427562 -28.594449868193294,24.465256725664762 -28.589905952891769,24.469483524126915 -28.585426001783489,24.473798356852907 -28.581011371215411,24.478199906715595 -28.576663397590849,24.48268683085379 -28.572383396972441,24.487257761043733 -28.568172664691346,24.491911304154055 -28.564032474962829,24.496646042544203 -28.559964080508252,24.501460534510869 -28.555968712183585,24.506353314724617 -28.552047578614662,24.511322894671945 -28.548201865839104,24.516367763102515 -28.544432736955102,24.52148638648579 -28.540741331777156,24.526677209488223 -28.537128766498796,24.531938655423552 -28.533596133362522,24.537269126740796 -28.530144500336959,24.542667005499531 -28.526774910801166,24.548130653851075 -28.523488383236369,24.553658414542507 -28.520285910925423,24.559248611389858 -28.517168461659423,24.564899549803645 -28.514136977452182,24.57060951729083 -28.511192374262492,24.576376783945427 -28.508335541723795,24.582199602983856 -28.505567342882131,24.588076211266849 -28.502888613941764,24.594004829807968 -28.500300164018839,24.599983664309274 -28.497802774903008,24.606010905708388 -28.495397200827426,24.612084730676745 -28.493084168246597,24.618203302205877 -28.490864375622735,24.624364770124082 -28.48873849322014,24.630567271652016 -28.486707162908274,24.636808931930073 -28.48477099797276,24.64308786462378 -28.482930582935339,24.649402172429006 -28.481186473381939,24.655749947658894 -28.479539195799475,24.662129272778778 -28.47798924742105,24.668538221026751 -28.476537096080108,24.674974856924731 -28.475183180072875,24.68143723685181 -28.47392790802968,24.687923409675783 -28.472771658795054,24.694431417230337 -28.47171478131645,24.700959294993751 -28.47075759454188,24.70750507257009 -28.469900387326192,24.714066774367769 -28.469143418346533,24.720642420038875 -28.468486916026166,24.727230025245085 -28.467931078467672,24.73382760206988 -28.467476073394735,24.740433159690181 -28.467122038103,24.747044705027836 -28.466869079419723,24.753660243120745 -28.46671727367243,24.760277777777777 -28.466666666666683))',
                                      max_error=0.0000001) != 0:
        print('did not get expected first geom')
        pytest.fail(geom.ExportToWkt())

    feat = lyr.GetNextFeature()
    geom = feat.GetGeometryRef()
    if ogrtest.check_feature_geometry(feat, 'POLYGON ((25.324444444444445 -28.735,25.324444444444445 -28.735,25.324444444444747 -28.735,25.3256844012835 -28.743637219488093,25.326752458414518 -28.752292221672775,25.327648242989319 -28.760962374913134,25.328371434292126 -28.769645042225264,25.328921763884399 -28.778337582080368,25.329299015739096 -28.787037349205164,25.329503026367707 -28.795741695383924,25.329533684919237 -28.804447970262672,25.329390933266499 -28.813153522154423,25.329074766083266 -28.821855698846022,25.328585230899417 -28.830551848405761,25.32792242813515 -28.839239319991876,25.327086511130251 -28.847915464661341,25.326077686158602 -28.856577636179196,25.324896212403537 -28.865223191827752,25.323542401945843 -28.873849493215474,25.322016619719491 -28.882453907085591,25.320319283456154 -28.891033806123644,25.31845086360034 -28.899586569764509,25.316411883234647 -28.908109584997732,25.314202917960664 -28.916600247171544,25.311824595781452 -28.925055960795305,25.309277596961152 -28.933474140339584,25.306562653857945 -28.941852211034359,25.303680550768494 -28.950187609664397,25.300632123720742 -28.958477785362163,25.29741826027432 -28.966720200397404,25.294039899300181 -28.974912330963704,25.290498030727949 -28.983051667961448,25.286793695305345 -28.991135717776984,25.282927984310767 -28.999162003057677,25.278902039273312 -29.007128063482853,25.274717051653134 -29.015031456530025,25.270374262533323 -29.022869758236496,25.265874962270246 -29.030640563955714,25.26122049013696 -29.038341489108532,25.256412233959036 -29.045970169928736,25.251451629715206 -29.053524264202991,25.246340161140221 -29.06100145200449,25.241079359298173 -29.068399436420506,25.23567080214746 -29.075715944273327,25.230116114090873 -29.082948726834402,25.224416965497046 -29.090095560531509,25.218575072228933 -29.097154247648504,25.212592195130505 -29.10412261701785,25.206470139518853 -29.110998524705039,25.200210754651753 -29.11777985468531,25.193815933175109 -29.124464519512046,25.187287610571182 -29.131050460976667,25.180627764570215 -29.137535650759972,25.173838414570472 -29.143918091074411,25.166921621027861 -29.150195815297337,25.159879484826497 -29.156366888594846,25.152714146662561 -29.162429408536127,25.145427786377269 -29.168381505697866,25.138022622300941 -29.174221344258754,25.130500910584292 -29.179947122583698,25.122864944495355 -29.185557073797725,25.115117053723321 -29.191049466349057,25.107259603657024 -29.196422604561548,25.099294994669837 -29.201674829175872,25.091225661355146 -29.206804517879718,25.083054071794677 -29.211810085826329,25.074782726776942 -29.216689986141546,25.066414159022649 -29.221442710419112,25.057950932399795 -29.226066789203841,25.049395641117307 -29.230560792462668,25.040750908918767 -29.234923330043529,25.032019388244304 -29.239153052121523,25.023203759421683 -29.243248649632577,25.014306729794193 -29.247208854694165,25.005331032890854 -29.251032441013166,24.996279427553059 -29.254718224280467,24.987154697052485 -29.258265062552468,24.977959648227149 -29.261671856618946,24.96869711057434 -29.264937550357544,24.959369935370919 -29.268061131074475,24.949980994740844 -29.271041629831515,24.940533180755306 -29.273878121758855,24.931029404524764 -29.276569726354225,24.921472595226302 -29.27911560776748,24.911865699212655 -29.281514975071246,24.902211679051732 -29.283767082516917,24.892513512561873 -29.285871229776419,24.882774191884664 -29.287826762169175,24.872996722502361 -29.289633070874672,24.863184122310912 -29.291289593130031,24.853339420578315 -29.292795812413047,24.843465657046142 -29.294151258610142,24.833565880890973 -29.295355508169479,24.823643149820615 -29.296408184238985,24.813700528987738 -29.297308956789578,24.803741090085058 -29.298057542722887,24.793767910343536 -29.298653705964284,24.783784071443542 -29.299097257540382,24.773792658660838 -29.299388055641543,24.763796759952577 -29.299526005669037,24.753799464358973 -29.299511060267122,24.743803861918728 -29.299343219339562,24.733813042177051 -29.299022530051275,24.723830092997549 -29.298549086814461,24.713858099961822 -29.297923031259401,24.703900145183407 -29.297144552190304,24.693959306309406 -29.296213885525674,24.684038655567267 -29.295131314223482,24.674141258801942 -29.293897168191322,24.664270174416327 -29.292511824181247,24.65442845241142 -29.290975705669538,24.644619133445421 -29.289289282721541,24.634845247808041 -29.287453071841185,24.625109814448344 -29.285467635805958,24.615415840038214 -29.283333583486638,24.605766317960285 -29.281051569652291,24.596164227391593 -29.278622294760709,24.586612532310763 -29.276046504733856,24.577114180572615 -29.273324990718947,24.567672102945274 -29.270458588834956,24.558289212193195 -29.267448179904818,24.548968402128249 -29.264294689173013,24.539712546687348 -29.260999086009392,24.530524499021816 -29.257562383598525,24.521407090592227 -29.253985638615347,24.512363130253711 -29.250269950886775,24.503395403389867 -29.246416463039765,24.494506670979664 -29.242426360135497,24.485699668772813 -29.238300869290413,24.476977106411617 -29.234041259283813,24.468341666547062 -29.229648840152166,24.459796004019395 -29.225124962770508,24.451342745027716 -29.220471018421009,24.442984486277584 -29.215688438348721,24.434723794192617 -29.210778693304832,24.426563204089472 -29.205743293077461,24.418505219398092 -29.200583786010426,24.410552310879975 -29.195301758509814,24.402706915859742 -29.189898834538667,24.394971437455574 -29.184376675100097,24.387348243856902 -29.178736977708979,24.379839667567335 -29.172981475852069,24.372448004707099 -29.167111938437387,24.365175514288836 -29.161130169232337,24.358024417543742 -29.155038006291477,24.350996897226008 -29.14883732137352,24.34409509694385 -29.142530019348044,24.337321120532131 -29.136118037592439,24.33067703138671 -29.129603345378626,24.324164851854118 -29.122987943250237,24.317786562621645 -29.116273862390543,24.311544102121797 -29.109463163980905,24.30543936594934 -29.10255793855049,24.2994742062996 -29.095560305316994,24.293650431416442 -29.088472411518978,24.287969805061284 -29.081296431740057,24.282434045985305 -29.074034567224615,24.277044827435564 -29.06668904518618,24.271803776659787 -29.059262118107824,24.266712474439807 -29.051756063035484,24.261772454629462 -29.044173180864007,24.256985203708833 -29.036515795616396,24.252352160375441 -29.02878625371649,24.247874715121878 -29.02098692325518,24.24355420984503 -29.013120193250629,24.239391937478619 -29.00518847290239,24.235389141624353 -28.997194190840176,24.231547016208346 -28.989139794367077,24.227866705162754 -28.981027748697628,24.224349302108447 -28.972860536191234,24.220995850059293 -28.964640655580638,24.217807341153009 -28.956370621196328,24.214784716384329 -28.948052962186651,24.211928865360008 -28.939690221734097,24.209240626079428 -28.931284956268058,24.206720784716541 -28.92283973467417,24.204370075425757 -28.914357137500531,24.202189180171864 -28.905839756161143,24.200178728561479 -28.897290192136808,24.198339297705129 -28.888711056173534,24.196671412087511 -28.880104967479028,24.195175543457147 -28.871474552917306,24.19385211072877 -28.862822446201619,24.192701479915275 -28.854151287086367,24.19172396405807 -28.845463720557575,24.190919823186178 -28.836762396022849,24.190289264288399 -28.828049966500572,24.189832441300496 -28.819329087808967,24.189549455112285 -28.810602417754893,24.189440353583787 -28.801872615323049,24.189505131591886 -28.793142339865469,24.189743731066635 -28.784414250291647,24.190156041080773 -28.775691004259812,24.190741897919008 -28.766975257369026,24.191501085191938 -28.758269662353158,24.192433333936325 -28.74957686827598,24.193538322762858 -28.740899519728529,24.194815678001433 -28.732240256028561,24.196264973852333 -28.723601710422116,24.197885732583238 -28.714986509287982,24.19967742470579 -28.706397271344827,24.201639469198703 -28.697836606861372,24.203771233721888 -28.68930711687004,24.206072034858177 -28.680811392383887,24.208541138376447 -28.672352013617413,24.211177759476751 -28.663931549211355,24.213981063100391 -28.655552555461597,24.2169501642021 -28.647217575552503,24.220084128082078 -28.638929138794964,24.223381970696099 -28.630689759869227,24.226842659002589 -28.622501938072631,24.230465111308209 -28.614368156572979,24.234248197645979 -28.606290881666965,24.238190740140944 -28.598272562044642,24.242291513417509 -28.590315628059457,24.246549244988177 -28.582422491004635,24.250962615689375 -28.574595542395741,24.255530260106084 -28.566837153259698,24.260250767015116 -28.559149673430525,24.265122679844414 -28.551535430851899,24.270144497143669 -28.543996730886917,24.275314673058389 -28.536535855634881,24.280631617835351 -28.529155063255686,24.286093698316382 -28.521856587301826,24.291699238459888 -28.514642636057971,24.297446519871226 -28.507515391888845,24.303333782336477 -28.500477010594921,24.309359224380383 -28.493529620776712,24.31552100381996 -28.486675323207294,24.321817238338735 -28.479916190213615,24.328246006069861 -28.473254265066558,24.334805346194791 -28.466691561380145,24.341493259533799 -28.4602300625194,24.348307709170513 -28.453871721018132,24.355246621064914 -28.447618458005579,24.362307884696193 -28.441472162642967,24.369489353694416 -28.435434691569711,24.376788846495483 -28.429507868359337,24.384204147000045 -28.423693482985684,24.391733005249641 -28.417993291298984,24.399373138086929 -28.412409014512306,24.407122229850941 -28.406942338698542,24.414977933080777 -28.401594914297746,24.422937869201576 -28.396368355635119,24.430999629236783 -28.391264240449956,24.43916077453795 -28.38628410943538,24.447418837487788 -28.381429465788997,24.455771322249223 -28.37670177477483,24.464215705504113 -28.372102463296528,24.472749437186824 -28.367632919481679,24.481369941250147 -28.363294492277845,24.490074616410581 -28.359088491059879,24.498860836925523 -28.355016185249198,24.50772595334951 -28.351078803944461,24.516667293338532 -28.347277535564402,24.525682162385579 -28.343613527502299,24.534767844672221 -28.340087885792698,24.543921603800779 -28.336701674789964,24.553140683623202 -28.333455916859251,24.562422309051517 -28.330351592079595,24.57176368682665 -28.327389637959214,24.581162006386851 -28.324570949163544,24.590614440635008 -28.3218963772552,24.60011814677102 -28.31936673044703,24.609670267145127 -28.316982773367286,24.619267930032869 -28.314745226837644,24.628908250528362 -28.312654767663972,24.63858833131291 -28.310712028439568,24.648305263544835 -28.308917597361543,24.658056127663254 -28.30727201805972,24.667837994267057 -28.305775789438641,24.677647924917796 -28.304429365532272,24.687482973026292 -28.303233155371913,24.697340184664604 -28.302187522866816,24.707216599457116 -28.301292786698056,24.717109251382755 -28.300549220225193,24.727015169673113 -28.299957051406295,24.736931379690652 -28.299516462730722,24.746854903656409 -28.299227591165192,24.756782761632255 -28.29909052811297,24.766711972434599 -28.299105319386072,24.776639554240347 -28.299271965190698,24.786562525734769 -28.299590420125625,24.796477906700915 -28.300060593194004,24.806382719171182 -28.300682347828001,24.816273988013755 -28.301455501926711,24.826148741958701 -28.302379827907302,24.836004014361414 -28.303455052768882,24.845836844098478 -28.304680858169917,24.855644276402057 -28.306056880518398,24.865423363765725 -28.307582711075085,24.875171166708189 -28.309257896070051,24.884884754678925 -28.311081936831783,24.894561206900327 -28.313054289929653,24.904197613154185 -28.315174367329107,24.913791074742456 -28.317441536559656,24.92333870518836 -28.31985512089615,24.932837631161526 -28.322414399552244,24.93611111111111 -28.323333333333334,24.93611111111111 -28.323333333333334,24.74 -28.466111111111111,24.74 -28.466111111111111,24.740000000006798 -28.466111111112809,24.746632430249097 -28.465871637044913,24.753268187622954 -28.465733642679226,24.759905272118928 -28.465697157550323,24.766541673734942 -28.465762180560702,24.77317539772077 -28.4659286799847,24.779804440348542 -28.466196593481584,24.786426802076775 -28.466565828117496,24.793040485511163 -28.467036260396483,24.799643496136763 -28.467607736300309,24.806233842740653 -28.468280071337446,24.812809538018556 -28.46905305060092,24.819368599277652 -28.469926428834924,24.825909048903572 -28.470899930510456,24.832428914991102 -28.471973249910022,24.838926231930369 -28.473146051220724,24.845399040894488 -28.474417968636757,24.85184539057164 -28.475788606470175,24.85826333757198 -28.477257539270838,24.864650947139452 -28.478824311954796,24.871006293602161 -28.480488439941709,24.877327461036565 -28.482249409300493,24.883612543751585 -28.484106676904105,24.889859646912562 -28.486059670592425,24.896066887037229 -28.488107789344113,24.902232392611545 -28.490250403456642,24.908354304611503 -28.492486854734935,24.91443077703882 -28.494816456688355,24.920459977479492 -28.49723849473618,24.926440087661302 -28.499752226420981,24.932369303955355 -28.502356881630817,24.938245837939125 -28.505051662829032,24.944067916906295 -28.50783574529251,24.949833784410384 -28.510708277357907,24.955541700766702 -28.51366838067581,24.961189943568936 -28.516715150472848,24.966776808222054 -28.519847655821607,24.972300608432882 -28.523064939918342,24.9777596767074 -28.526366020368442,24.983152364848348 -28.529749889479419,24.988477044467242 -28.533215514561434,24.993732107439818 -28.536761838235364,24.998915966414472 -28.540387778748141,25.004027055264203 -28.544092230295462,25.009063829563729 -28.547874063351784,25.014024767071181 -28.551732125007007,25.018908368153632 -28.555665239310756,25.023713156252619 -28.559672207623251,25.028437678344208 -28.563751808972938,25.033080505346668 -28.567902800421166,25.03764023257828 -28.572123917433132,25.042115480170764 -28.576413874255621,25.046504893485697 -28.580771364301086,25.050807143534044 -28.585195060537998,25.055020927375441 -28.589683615887409,25.059144968510566 -28.594235663625824,25.063178017286948 -28.598849817793635,25.067118851257888 -28.603524673609968,25.070966275578758 -28.608258807892824,25.074719123363518 -28.61305077948515,25.078376256041661 -28.617899129686265,25.081936563715608 -28.622802382688874,25.085398965501863 -28.627759046021239,25.088762409872622 -28.632767610994421,25.092025874965881 -28.637826553154852,25.095188368924873 -28.642934332741433,25.098248930184742 -28.648089395147835,25.101206627805809 -28.653290171388974,25.104060561732403 -28.658535078572456,25.106809863101081 -28.663822520374055,25.109453694502864 -28.669150887517645,25.111991250254196 -28.674518558259152,25.114421756659766 -28.679923898874449,25.116744472249401 -28.685365264151244,25.118958688020527 -28.690840997884379,25.121063727672666 -28.696349433375019,25.123058947821914 -28.701888893932889,25.124943738219745 -28.707457693382054,25.126717521933593 -28.713054136569667,25.128379755560044 -28.718676519877718,25.129929929402699 -28.724323131737549,25.131367567623556 -28.729992253147103,25.132692228430109 -28.735682158190684,25.13390350421783 -28.741391114561011,25.135001021699754 -28.747117384083495,25.135984442057644 -28.752859223242652,25.136853461048599 -28.75861488371028,25.137607809118133 -28.764382612875551,25.138247251504847 -28.770160654376411,25.138771588331661 -28.775947248632733,25.139180654678363 -28.781740633380437,25.139474320653182 -28.787539044207037,25.139652491459525 -28.793340715087666,25.139715107429993 -28.79914387892245,25.139662144076386 -28.804946768074032,25.139493612107152 -28.810747614905807,25.139444444444443 -28.811944444444446,25.139444444444443 -28.811944444444446,25.324444444444445 -28.735))',
                                      max_error=0.0000001) != 0:
        print('did not get expected second geom')
        pytest.fail(geom.ExportToWkt())

    



