# Transpiler Mate (c) 2025
# Copyright 2026 Terradue
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from .software_application_models import CreativeWork
from pydantic import AnyUrl
from typing import Mapping

LICENSES_INDEX: Mapping[str, CreativeWork] = {
    "0BSD": CreativeWork(
        identifier="0BSD",
        name="BSD Zero Clause License",
        url=AnyUrl("http://landley.net/toybox/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/0BSD": CreativeWork(
        identifier="0BSD",
        name="BSD Zero Clause License",
        url=AnyUrl("http://landley.net/toybox/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/0BSD.html": CreativeWork(
        identifier="0BSD",
        name="BSD Zero Clause License",
        url=AnyUrl("http://landley.net/toybox/license.html"),
    ),  # type: ignore
    "http://landley.net/toybox/license.html": CreativeWork(
        identifier="0BSD",
        name="BSD Zero Clause License",
        url=AnyUrl("http://landley.net/toybox/license.html"),
    ),  # type: ignore
    "3D-Slicer-1.0": CreativeWork(
        identifier="3D-Slicer-1.0",
        name="3D Slicer License v1.0",
        url=AnyUrl("https://slicer.org/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/3D-Slicer-1.0": CreativeWork(
        identifier="3D-Slicer-1.0",
        name="3D Slicer License v1.0",
        url=AnyUrl("https://slicer.org/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/3D-Slicer-1.0.html": CreativeWork(
        identifier="3D-Slicer-1.0",
        name="3D Slicer License v1.0",
        url=AnyUrl("https://slicer.org/LICENSE"),
    ),  # type: ignore
    "https://slicer.org/LICENSE": CreativeWork(
        identifier="3D-Slicer-1.0",
        name="3D Slicer License v1.0",
        url=AnyUrl("https://slicer.org/LICENSE"),
    ),  # type: ignore
    "AAL": CreativeWork(
        identifier="AAL",
        name="Attribution Assurance License",
        url=AnyUrl("https://opensource.org/licenses/attribution"),
    ),  # type: ignore
    "https://spdx.org/licenses/AAL": CreativeWork(
        identifier="AAL",
        name="Attribution Assurance License",
        url=AnyUrl("https://opensource.org/licenses/attribution"),
    ),  # type: ignore
    "https://spdx.org/licenses/AAL.html": CreativeWork(
        identifier="AAL",
        name="Attribution Assurance License",
        url=AnyUrl("https://opensource.org/licenses/attribution"),
    ),  # type: ignore
    "https://opensource.org/licenses/attribution": CreativeWork(
        identifier="AAL",
        name="Attribution Assurance License",
        url=AnyUrl("https://opensource.org/licenses/attribution"),
    ),  # type: ignore
    "Abstyles": CreativeWork(
        identifier="Abstyles",
        name="Abstyles License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Abstyles"),
    ),  # type: ignore
    "https://spdx.org/licenses/Abstyles": CreativeWork(
        identifier="Abstyles",
        name="Abstyles License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Abstyles"),
    ),  # type: ignore
    "https://spdx.org/licenses/Abstyles.html": CreativeWork(
        identifier="Abstyles",
        name="Abstyles License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Abstyles"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Abstyles": CreativeWork(
        identifier="Abstyles",
        name="Abstyles License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Abstyles"),
    ),  # type: ignore
    "AdaCore-doc": CreativeWork(
        identifier="AdaCore-doc",
        name="AdaCore Doc License",
        url=AnyUrl("https://github.com/AdaCore/xmlada/blob/master/docs/index.rst"),
    ),  # type: ignore
    "https://spdx.org/licenses/AdaCore-doc": CreativeWork(
        identifier="AdaCore-doc",
        name="AdaCore Doc License",
        url=AnyUrl("https://github.com/AdaCore/xmlada/blob/master/docs/index.rst"),
    ),  # type: ignore
    "https://spdx.org/licenses/AdaCore-doc.html": CreativeWork(
        identifier="AdaCore-doc",
        name="AdaCore Doc License",
        url=AnyUrl("https://github.com/AdaCore/xmlada/blob/master/docs/index.rst"),
    ),  # type: ignore
    "https://github.com/AdaCore/xmlada/blob/master/docs/index.rst": CreativeWork(
        identifier="AdaCore-doc",
        name="AdaCore Doc License",
        url=AnyUrl("https://github.com/AdaCore/xmlada/blob/master/docs/index.rst"),
    ),  # type: ignore
    "Adobe-2006": CreativeWork(
        identifier="Adobe-2006",
        name="Adobe Systems Incorporated Source Code License Agreement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AdobeLicense"),
    ),  # type: ignore
    "https://spdx.org/licenses/Adobe-2006": CreativeWork(
        identifier="Adobe-2006",
        name="Adobe Systems Incorporated Source Code License Agreement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AdobeLicense"),
    ),  # type: ignore
    "https://spdx.org/licenses/Adobe-2006.html": CreativeWork(
        identifier="Adobe-2006",
        name="Adobe Systems Incorporated Source Code License Agreement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AdobeLicense"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/AdobeLicense": CreativeWork(
        identifier="Adobe-2006",
        name="Adobe Systems Incorporated Source Code License Agreement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AdobeLicense"),
    ),  # type: ignore
    "Adobe-Display-PostScript": CreativeWork(
        identifier="Adobe-Display-PostScript",
        name="Adobe Display PostScript License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L752"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Adobe-Display-PostScript": CreativeWork(
        identifier="Adobe-Display-PostScript",
        name="Adobe Display PostScript License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L752"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Adobe-Display-PostScript.html": CreativeWork(
        identifier="Adobe-Display-PostScript",
        name="Adobe Display PostScript License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L752"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L752": CreativeWork(
        identifier="Adobe-Display-PostScript",
        name="Adobe Display PostScript License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L752"
        ),
    ),  # type: ignore
    "Adobe-Glyph": CreativeWork(
        identifier="Adobe-Glyph",
        name="Adobe Glyph List License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#AdobeGlyph"),
    ),  # type: ignore
    "https://spdx.org/licenses/Adobe-Glyph": CreativeWork(
        identifier="Adobe-Glyph",
        name="Adobe Glyph List License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#AdobeGlyph"),
    ),  # type: ignore
    "https://spdx.org/licenses/Adobe-Glyph.html": CreativeWork(
        identifier="Adobe-Glyph",
        name="Adobe Glyph List License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#AdobeGlyph"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/MIT#AdobeGlyph": CreativeWork(
        identifier="Adobe-Glyph",
        name="Adobe Glyph List License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#AdobeGlyph"),
    ),  # type: ignore
    "Adobe-Utopia": CreativeWork(
        identifier="Adobe-Utopia",
        name="Adobe Utopia Font License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/adobe-utopia-100dpi/-/blob/master/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Adobe-Utopia": CreativeWork(
        identifier="Adobe-Utopia",
        name="Adobe Utopia Font License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/adobe-utopia-100dpi/-/blob/master/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Adobe-Utopia.html": CreativeWork(
        identifier="Adobe-Utopia",
        name="Adobe Utopia Font License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/adobe-utopia-100dpi/-/blob/master/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/font/adobe-utopia-100dpi/-/blob/master/COPYING?ref_type=heads": CreativeWork(
        identifier="Adobe-Utopia",
        name="Adobe Utopia Font License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/adobe-utopia-100dpi/-/blob/master/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "ADSL": CreativeWork(
        identifier="ADSL",
        name="Amazon Digital Services License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/AmazonDigitalServicesLicense"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ADSL": CreativeWork(
        identifier="ADSL",
        name="Amazon Digital Services License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/AmazonDigitalServicesLicense"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ADSL.html": CreativeWork(
        identifier="ADSL",
        name="Amazon Digital Services License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/AmazonDigitalServicesLicense"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/AmazonDigitalServicesLicense": CreativeWork(
        identifier="ADSL",
        name="Amazon Digital Services License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/AmazonDigitalServicesLicense"
        ),
    ),  # type: ignore
    "Advanced-Cryptics-Dictionary": CreativeWork(
        identifier="Advanced-Cryptics-Dictionary",
        name="Advanced Cryptics Dictionary License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Advanced-Cryptics-Dictionary": CreativeWork(
        identifier="Advanced-Cryptics-Dictionary",
        name="Advanced Cryptics Dictionary License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Advanced-Cryptics-Dictionary.html": CreativeWork(
        identifier="Advanced-Cryptics-Dictionary",
        name="Advanced Cryptics Dictionary License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2"
        ),
    ),  # type: ignore
    "https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2": CreativeWork(
        identifier="Advanced-Cryptics-Dictionary",
        name="Advanced Cryptics Dictionary License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2"
        ),
    ),  # type: ignore
    "AFL-1.1": CreativeWork(
        identifier="AFL-1.1",
        name="Academic Free License v1.1",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-1.1": CreativeWork(
        identifier="AFL-1.1",
        name="Academic Free License v1.1",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-1.1.html": CreativeWork(
        identifier="AFL-1.1",
        name="Academic Free License v1.1",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-1.1.txt"),
    ),  # type: ignore
    "http://opensource.linux-mirror.org/licenses/afl-1.1.txt": CreativeWork(
        identifier="AFL-1.1",
        name="Academic Free License v1.1",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-1.1.txt"),
    ),  # type: ignore
    "AFL-1.2": CreativeWork(
        identifier="AFL-1.2",
        name="Academic Free License v1.2",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-1.2": CreativeWork(
        identifier="AFL-1.2",
        name="Academic Free License v1.2",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-1.2.html": CreativeWork(
        identifier="AFL-1.2",
        name="Academic Free License v1.2",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-1.2.txt"),
    ),  # type: ignore
    "http://opensource.linux-mirror.org/licenses/afl-1.2.txt": CreativeWork(
        identifier="AFL-1.2",
        name="Academic Free License v1.2",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-1.2.txt"),
    ),  # type: ignore
    "AFL-2.0": CreativeWork(
        identifier="AFL-2.0",
        name="Academic Free License v2.0",
        url=AnyUrl(
            "http://wayback.archive.org/web/20060924134533/http://www.opensource.org/licenses/afl-2.0.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-2.0": CreativeWork(
        identifier="AFL-2.0",
        name="Academic Free License v2.0",
        url=AnyUrl(
            "http://wayback.archive.org/web/20060924134533/http://www.opensource.org/licenses/afl-2.0.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-2.0.html": CreativeWork(
        identifier="AFL-2.0",
        name="Academic Free License v2.0",
        url=AnyUrl(
            "http://wayback.archive.org/web/20060924134533/http://www.opensource.org/licenses/afl-2.0.txt"
        ),
    ),  # type: ignore
    "http://wayback.archive.org/web/20060924134533/http://www.opensource.org/licenses/afl-2.0.txt": CreativeWork(
        identifier="AFL-2.0",
        name="Academic Free License v2.0",
        url=AnyUrl(
            "http://wayback.archive.org/web/20060924134533/http://www.opensource.org/licenses/afl-2.0.txt"
        ),
    ),  # type: ignore
    "AFL-2.1": CreativeWork(
        identifier="AFL-2.1",
        name="Academic Free License v2.1",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-2.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-2.1": CreativeWork(
        identifier="AFL-2.1",
        name="Academic Free License v2.1",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-2.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-2.1.html": CreativeWork(
        identifier="AFL-2.1",
        name="Academic Free License v2.1",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-2.1.txt"),
    ),  # type: ignore
    "http://opensource.linux-mirror.org/licenses/afl-2.1.txt": CreativeWork(
        identifier="AFL-2.1",
        name="Academic Free License v2.1",
        url=AnyUrl("http://opensource.linux-mirror.org/licenses/afl-2.1.txt"),
    ),  # type: ignore
    "AFL-3.0": CreativeWork(
        identifier="AFL-3.0",
        name="Academic Free License v3.0",
        url=AnyUrl("http://www.rosenlaw.com/AFL3.0.htm"),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-3.0": CreativeWork(
        identifier="AFL-3.0",
        name="Academic Free License v3.0",
        url=AnyUrl("http://www.rosenlaw.com/AFL3.0.htm"),
    ),  # type: ignore
    "https://spdx.org/licenses/AFL-3.0.html": CreativeWork(
        identifier="AFL-3.0",
        name="Academic Free License v3.0",
        url=AnyUrl("http://www.rosenlaw.com/AFL3.0.htm"),
    ),  # type: ignore
    "http://www.rosenlaw.com/AFL3.0.htm": CreativeWork(
        identifier="AFL-3.0",
        name="Academic Free License v3.0",
        url=AnyUrl("http://www.rosenlaw.com/AFL3.0.htm"),
    ),  # type: ignore
    "Afmparse": CreativeWork(
        identifier="Afmparse",
        name="Afmparse License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Afmparse"),
    ),  # type: ignore
    "https://spdx.org/licenses/Afmparse": CreativeWork(
        identifier="Afmparse",
        name="Afmparse License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Afmparse"),
    ),  # type: ignore
    "https://spdx.org/licenses/Afmparse.html": CreativeWork(
        identifier="Afmparse",
        name="Afmparse License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Afmparse"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Afmparse": CreativeWork(
        identifier="Afmparse",
        name="Afmparse License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Afmparse"),
    ),  # type: ignore
    "AGPL-1.0": CreativeWork(
        identifier="AGPL-1.0",
        name="Affero General Public License v1.0",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-1.0": CreativeWork(
        identifier="AGPL-1.0",
        name="Affero General Public License v1.0",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-1.0.html": CreativeWork(
        identifier="AGPL-1.0",
        name="Affero General Public License v1.0",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "http://www.affero.org/oagpl.html": CreativeWork(
        identifier="AGPL-1.0",
        name="Affero General Public License v1.0",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "AGPL-1.0-only": CreativeWork(
        identifier="AGPL-1.0-only",
        name="Affero General Public License v1.0 only",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-1.0-only": CreativeWork(
        identifier="AGPL-1.0-only",
        name="Affero General Public License v1.0 only",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-1.0-only.html": CreativeWork(
        identifier="AGPL-1.0-only",
        name="Affero General Public License v1.0 only",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "AGPL-1.0-or-later": CreativeWork(
        identifier="AGPL-1.0-or-later",
        name="Affero General Public License v1.0 or later",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-1.0-or-later": CreativeWork(
        identifier="AGPL-1.0-or-later",
        name="Affero General Public License v1.0 or later",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-1.0-or-later.html": CreativeWork(
        identifier="AGPL-1.0-or-later",
        name="Affero General Public License v1.0 or later",
        url=AnyUrl("http://www.affero.org/oagpl.html"),
    ),  # type: ignore
    "AGPL-3.0": CreativeWork(
        identifier="AGPL-3.0",
        name="GNU Affero General Public License v3.0",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-3.0": CreativeWork(
        identifier="AGPL-3.0",
        name="GNU Affero General Public License v3.0",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-3.0.html": CreativeWork(
        identifier="AGPL-3.0",
        name="GNU Affero General Public License v3.0",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/agpl.txt": CreativeWork(
        identifier="AGPL-3.0",
        name="GNU Affero General Public License v3.0",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "AGPL-3.0-only": CreativeWork(
        identifier="AGPL-3.0-only",
        name="GNU Affero General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-3.0-only": CreativeWork(
        identifier="AGPL-3.0-only",
        name="GNU Affero General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-3.0-only.html": CreativeWork(
        identifier="AGPL-3.0-only",
        name="GNU Affero General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "AGPL-3.0-or-later": CreativeWork(
        identifier="AGPL-3.0-or-later",
        name="GNU Affero General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-3.0-or-later": CreativeWork(
        identifier="AGPL-3.0-or-later",
        name="GNU Affero General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/AGPL-3.0-or-later.html": CreativeWork(
        identifier="AGPL-3.0-or-later",
        name="GNU Affero General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/agpl.txt"),
    ),  # type: ignore
    "Aladdin": CreativeWork(
        identifier="Aladdin",
        name="Aladdin Free Public License",
        url=AnyUrl("http://pages.cs.wisc.edu/~ghost/doc/AFPL/6.01/Public.htm"),
    ),  # type: ignore
    "https://spdx.org/licenses/Aladdin": CreativeWork(
        identifier="Aladdin",
        name="Aladdin Free Public License",
        url=AnyUrl("http://pages.cs.wisc.edu/~ghost/doc/AFPL/6.01/Public.htm"),
    ),  # type: ignore
    "https://spdx.org/licenses/Aladdin.html": CreativeWork(
        identifier="Aladdin",
        name="Aladdin Free Public License",
        url=AnyUrl("http://pages.cs.wisc.edu/~ghost/doc/AFPL/6.01/Public.htm"),
    ),  # type: ignore
    "http://pages.cs.wisc.edu/~ghost/doc/AFPL/6.01/Public.htm": CreativeWork(
        identifier="Aladdin",
        name="Aladdin Free Public License",
        url=AnyUrl("http://pages.cs.wisc.edu/~ghost/doc/AFPL/6.01/Public.htm"),
    ),  # type: ignore
    "ALGLIB-Documentation": CreativeWork(
        identifier="ALGLIB-Documentation",
        name="ALGLIB Documentation License",
        url=AnyUrl("https://spdx.org/licenses/ALGLIB-Documentation.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/ALGLIB-Documentation": CreativeWork(
        identifier="ALGLIB-Documentation",
        name="ALGLIB Documentation License",
        url=AnyUrl("https://spdx.org/licenses/ALGLIB-Documentation.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/ALGLIB-Documentation.html": CreativeWork(
        identifier="ALGLIB-Documentation",
        name="ALGLIB Documentation License",
        url=AnyUrl("https://spdx.org/licenses/ALGLIB-Documentation.html"),
    ),  # type: ignore
    "AMD-newlib": CreativeWork(
        identifier="AMD-newlib",
        name="AMD newlib License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/sys/a29khif/_close.S;h=04f52ae00de1dafbd9055ad8d73c5c697a3aae7f;hb=HEAD"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/AMD-newlib": CreativeWork(
        identifier="AMD-newlib",
        name="AMD newlib License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/sys/a29khif/_close.S;h=04f52ae00de1dafbd9055ad8d73c5c697a3aae7f;hb=HEAD"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/AMD-newlib.html": CreativeWork(
        identifier="AMD-newlib",
        name="AMD newlib License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/sys/a29khif/_close.S;h=04f52ae00de1dafbd9055ad8d73c5c697a3aae7f;hb=HEAD"
        ),
    ),  # type: ignore
    "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/sys/a29khif/_close.S;h=04f52ae00de1dafbd9055ad8d73c5c697a3aae7f;hb=HEAD": CreativeWork(
        identifier="AMD-newlib",
        name="AMD newlib License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/sys/a29khif/_close.S;h=04f52ae00de1dafbd9055ad8d73c5c697a3aae7f;hb=HEAD"
        ),
    ),  # type: ignore
    "AMDPLPA": CreativeWork(
        identifier="AMDPLPA",
        name="AMD's plpa_map.c License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AMD_plpa_map_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/AMDPLPA": CreativeWork(
        identifier="AMDPLPA",
        name="AMD's plpa_map.c License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AMD_plpa_map_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/AMDPLPA.html": CreativeWork(
        identifier="AMDPLPA",
        name="AMD's plpa_map.c License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AMD_plpa_map_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/AMD_plpa_map_License": CreativeWork(
        identifier="AMDPLPA",
        name="AMD's plpa_map.c License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AMD_plpa_map_License"),
    ),  # type: ignore
    "AML": CreativeWork(
        identifier="AML",
        name="Apple MIT License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Apple_MIT_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/AML": CreativeWork(
        identifier="AML",
        name="Apple MIT License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Apple_MIT_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/AML.html": CreativeWork(
        identifier="AML",
        name="Apple MIT License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Apple_MIT_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Apple_MIT_License": CreativeWork(
        identifier="AML",
        name="Apple MIT License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Apple_MIT_License"),
    ),  # type: ignore
    "AML-glslang": CreativeWork(
        identifier="AML-glslang",
        name="AML glslang variant License",
        url=AnyUrl(
            "https://github.com/KhronosGroup/glslang/blob/main/LICENSE.txt#L949"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/AML-glslang": CreativeWork(
        identifier="AML-glslang",
        name="AML glslang variant License",
        url=AnyUrl(
            "https://github.com/KhronosGroup/glslang/blob/main/LICENSE.txt#L949"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/AML-glslang.html": CreativeWork(
        identifier="AML-glslang",
        name="AML glslang variant License",
        url=AnyUrl(
            "https://github.com/KhronosGroup/glslang/blob/main/LICENSE.txt#L949"
        ),
    ),  # type: ignore
    "https://github.com/KhronosGroup/glslang/blob/main/LICENSE.txt#L949": CreativeWork(
        identifier="AML-glslang",
        name="AML glslang variant License",
        url=AnyUrl(
            "https://github.com/KhronosGroup/glslang/blob/main/LICENSE.txt#L949"
        ),
    ),  # type: ignore
    "AMPAS": CreativeWork(
        identifier="AMPAS",
        name="Academy of Motion Picture Arts and Sciences BSD",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD#AMPASBSD"),
    ),  # type: ignore
    "https://spdx.org/licenses/AMPAS": CreativeWork(
        identifier="AMPAS",
        name="Academy of Motion Picture Arts and Sciences BSD",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD#AMPASBSD"),
    ),  # type: ignore
    "https://spdx.org/licenses/AMPAS.html": CreativeWork(
        identifier="AMPAS",
        name="Academy of Motion Picture Arts and Sciences BSD",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD#AMPASBSD"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/BSD#AMPASBSD": CreativeWork(
        identifier="AMPAS",
        name="Academy of Motion Picture Arts and Sciences BSD",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD#AMPASBSD"),
    ),  # type: ignore
    "ANTLR-PD": CreativeWork(
        identifier="ANTLR-PD",
        name="ANTLR Software Rights Notice",
        url=AnyUrl("http://www.antlr2.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/ANTLR-PD": CreativeWork(
        identifier="ANTLR-PD",
        name="ANTLR Software Rights Notice",
        url=AnyUrl("http://www.antlr2.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/ANTLR-PD.html": CreativeWork(
        identifier="ANTLR-PD",
        name="ANTLR Software Rights Notice",
        url=AnyUrl("http://www.antlr2.org/license.html"),
    ),  # type: ignore
    "http://www.antlr2.org/license.html": CreativeWork(
        identifier="ANTLR-PD",
        name="ANTLR Software Rights Notice",
        url=AnyUrl("http://www.antlr2.org/license.html"),
    ),  # type: ignore
    "ANTLR-PD-fallback": CreativeWork(
        identifier="ANTLR-PD-fallback",
        name="ANTLR Software Rights Notice with license fallback",
        url=AnyUrl("http://www.antlr2.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/ANTLR-PD-fallback": CreativeWork(
        identifier="ANTLR-PD-fallback",
        name="ANTLR Software Rights Notice with license fallback",
        url=AnyUrl("http://www.antlr2.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/ANTLR-PD-fallback.html": CreativeWork(
        identifier="ANTLR-PD-fallback",
        name="ANTLR Software Rights Notice with license fallback",
        url=AnyUrl("http://www.antlr2.org/license.html"),
    ),  # type: ignore
    "any-OSI": CreativeWork(
        identifier="any-OSI",
        name="Any OSI License",
        url=AnyUrl("https://metacpan.org/pod/Exporter::Tidy#LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/any-OSI": CreativeWork(
        identifier="any-OSI",
        name="Any OSI License",
        url=AnyUrl("https://metacpan.org/pod/Exporter::Tidy#LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/any-OSI.html": CreativeWork(
        identifier="any-OSI",
        name="Any OSI License",
        url=AnyUrl("https://metacpan.org/pod/Exporter::Tidy#LICENSE"),
    ),  # type: ignore
    "https://metacpan.org/pod/Exporter::Tidy#LICENSE": CreativeWork(
        identifier="any-OSI",
        name="Any OSI License",
        url=AnyUrl("https://metacpan.org/pod/Exporter::Tidy#LICENSE"),
    ),  # type: ignore
    "any-OSI-perl-modules": CreativeWork(
        identifier="any-OSI-perl-modules",
        name="Any OSI License - Perl Modules",
        url=AnyUrl(
            "https://metacpan.org/release/JUERD/Exporter-Tidy-0.09/view/Tidy.pm#LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/any-OSI-perl-modules": CreativeWork(
        identifier="any-OSI-perl-modules",
        name="Any OSI License - Perl Modules",
        url=AnyUrl(
            "https://metacpan.org/release/JUERD/Exporter-Tidy-0.09/view/Tidy.pm#LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/any-OSI-perl-modules.html": CreativeWork(
        identifier="any-OSI-perl-modules",
        name="Any OSI License - Perl Modules",
        url=AnyUrl(
            "https://metacpan.org/release/JUERD/Exporter-Tidy-0.09/view/Tidy.pm#LICENSE"
        ),
    ),  # type: ignore
    "https://metacpan.org/release/JUERD/Exporter-Tidy-0.09/view/Tidy.pm#LICENSE": CreativeWork(
        identifier="any-OSI-perl-modules",
        name="Any OSI License - Perl Modules",
        url=AnyUrl(
            "https://metacpan.org/release/JUERD/Exporter-Tidy-0.09/view/Tidy.pm#LICENSE"
        ),
    ),  # type: ignore
    "Apache-1.0": CreativeWork(
        identifier="Apache-1.0",
        name="Apache License 1.0",
        url=AnyUrl("http://www.apache.org/licenses/LICENSE-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Apache-1.0": CreativeWork(
        identifier="Apache-1.0",
        name="Apache License 1.0",
        url=AnyUrl("http://www.apache.org/licenses/LICENSE-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Apache-1.0.html": CreativeWork(
        identifier="Apache-1.0",
        name="Apache License 1.0",
        url=AnyUrl("http://www.apache.org/licenses/LICENSE-1.0"),
    ),  # type: ignore
    "http://www.apache.org/licenses/LICENSE-1.0": CreativeWork(
        identifier="Apache-1.0",
        name="Apache License 1.0",
        url=AnyUrl("http://www.apache.org/licenses/LICENSE-1.0"),
    ),  # type: ignore
    "Apache-1.1": CreativeWork(
        identifier="Apache-1.1",
        name="Apache License 1.1",
        url=AnyUrl("http://apache.org/licenses/LICENSE-1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/Apache-1.1": CreativeWork(
        identifier="Apache-1.1",
        name="Apache License 1.1",
        url=AnyUrl("http://apache.org/licenses/LICENSE-1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/Apache-1.1.html": CreativeWork(
        identifier="Apache-1.1",
        name="Apache License 1.1",
        url=AnyUrl("http://apache.org/licenses/LICENSE-1.1"),
    ),  # type: ignore
    "http://apache.org/licenses/LICENSE-1.1": CreativeWork(
        identifier="Apache-1.1",
        name="Apache License 1.1",
        url=AnyUrl("http://apache.org/licenses/LICENSE-1.1"),
    ),  # type: ignore
    "Apache-2.0": CreativeWork(
        identifier="Apache-2.0",
        name="Apache License 2.0",
        url=AnyUrl("https://www.apache.org/licenses/LICENSE-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Apache-2.0": CreativeWork(
        identifier="Apache-2.0",
        name="Apache License 2.0",
        url=AnyUrl("https://www.apache.org/licenses/LICENSE-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Apache-2.0.html": CreativeWork(
        identifier="Apache-2.0",
        name="Apache License 2.0",
        url=AnyUrl("https://www.apache.org/licenses/LICENSE-2.0"),
    ),  # type: ignore
    "https://www.apache.org/licenses/LICENSE-2.0": CreativeWork(
        identifier="Apache-2.0",
        name="Apache License 2.0",
        url=AnyUrl("https://www.apache.org/licenses/LICENSE-2.0"),
    ),  # type: ignore
    "APAFML": CreativeWork(
        identifier="APAFML",
        name="Adobe Postscript AFM License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AdobePostscriptAFM"),
    ),  # type: ignore
    "https://spdx.org/licenses/APAFML": CreativeWork(
        identifier="APAFML",
        name="Adobe Postscript AFM License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AdobePostscriptAFM"),
    ),  # type: ignore
    "https://spdx.org/licenses/APAFML.html": CreativeWork(
        identifier="APAFML",
        name="Adobe Postscript AFM License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AdobePostscriptAFM"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/AdobePostscriptAFM": CreativeWork(
        identifier="APAFML",
        name="Adobe Postscript AFM License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/AdobePostscriptAFM"),
    ),  # type: ignore
    "APL-1.0": CreativeWork(
        identifier="APL-1.0",
        name="Adaptive Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/APL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/APL-1.0": CreativeWork(
        identifier="APL-1.0",
        name="Adaptive Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/APL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/APL-1.0.html": CreativeWork(
        identifier="APL-1.0",
        name="Adaptive Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/APL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/APL-1.0": CreativeWork(
        identifier="APL-1.0",
        name="Adaptive Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/APL-1.0"),
    ),  # type: ignore
    "App-s2p": CreativeWork(
        identifier="App-s2p",
        name="App::s2p License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/App-s2p"),
    ),  # type: ignore
    "https://spdx.org/licenses/App-s2p": CreativeWork(
        identifier="App-s2p",
        name="App::s2p License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/App-s2p"),
    ),  # type: ignore
    "https://spdx.org/licenses/App-s2p.html": CreativeWork(
        identifier="App-s2p",
        name="App::s2p License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/App-s2p"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/App-s2p": CreativeWork(
        identifier="App-s2p",
        name="App::s2p License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/App-s2p"),
    ),  # type: ignore
    "APSL-1.0": CreativeWork(
        identifier="APSL-1.0",
        name="Apple Public Source License 1.0",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Apple_Public_Source_License_1.0"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/APSL-1.0": CreativeWork(
        identifier="APSL-1.0",
        name="Apple Public Source License 1.0",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Apple_Public_Source_License_1.0"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/APSL-1.0.html": CreativeWork(
        identifier="APSL-1.0",
        name="Apple Public Source License 1.0",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Apple_Public_Source_License_1.0"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Apple_Public_Source_License_1.0": CreativeWork(
        identifier="APSL-1.0",
        name="Apple Public Source License 1.0",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Apple_Public_Source_License_1.0"
        ),
    ),  # type: ignore
    "APSL-1.1": CreativeWork(
        identifier="APSL-1.1",
        name="Apple Public Source License 1.1",
        url=AnyUrl(
            "http://www.opensource.apple.com/source/IOSerialFamily/IOSerialFamily-7/APPLE_LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/APSL-1.1": CreativeWork(
        identifier="APSL-1.1",
        name="Apple Public Source License 1.1",
        url=AnyUrl(
            "http://www.opensource.apple.com/source/IOSerialFamily/IOSerialFamily-7/APPLE_LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/APSL-1.1.html": CreativeWork(
        identifier="APSL-1.1",
        name="Apple Public Source License 1.1",
        url=AnyUrl(
            "http://www.opensource.apple.com/source/IOSerialFamily/IOSerialFamily-7/APPLE_LICENSE"
        ),
    ),  # type: ignore
    "http://www.opensource.apple.com/source/IOSerialFamily/IOSerialFamily-7/APPLE_LICENSE": CreativeWork(
        identifier="APSL-1.1",
        name="Apple Public Source License 1.1",
        url=AnyUrl(
            "http://www.opensource.apple.com/source/IOSerialFamily/IOSerialFamily-7/APPLE_LICENSE"
        ),
    ),  # type: ignore
    "APSL-1.2": CreativeWork(
        identifier="APSL-1.2",
        name="Apple Public Source License 1.2",
        url=AnyUrl("http://www.samurajdata.se/opensource/mirror/licenses/apsl.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/APSL-1.2": CreativeWork(
        identifier="APSL-1.2",
        name="Apple Public Source License 1.2",
        url=AnyUrl("http://www.samurajdata.se/opensource/mirror/licenses/apsl.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/APSL-1.2.html": CreativeWork(
        identifier="APSL-1.2",
        name="Apple Public Source License 1.2",
        url=AnyUrl("http://www.samurajdata.se/opensource/mirror/licenses/apsl.php"),
    ),  # type: ignore
    "http://www.samurajdata.se/opensource/mirror/licenses/apsl.php": CreativeWork(
        identifier="APSL-1.2",
        name="Apple Public Source License 1.2",
        url=AnyUrl("http://www.samurajdata.se/opensource/mirror/licenses/apsl.php"),
    ),  # type: ignore
    "APSL-2.0": CreativeWork(
        identifier="APSL-2.0",
        name="Apple Public Source License 2.0",
        url=AnyUrl("http://www.opensource.apple.com/license/apsl/"),
    ),  # type: ignore
    "https://spdx.org/licenses/APSL-2.0": CreativeWork(
        identifier="APSL-2.0",
        name="Apple Public Source License 2.0",
        url=AnyUrl("http://www.opensource.apple.com/license/apsl/"),
    ),  # type: ignore
    "https://spdx.org/licenses/APSL-2.0.html": CreativeWork(
        identifier="APSL-2.0",
        name="Apple Public Source License 2.0",
        url=AnyUrl("http://www.opensource.apple.com/license/apsl/"),
    ),  # type: ignore
    "http://www.opensource.apple.com/license/apsl/": CreativeWork(
        identifier="APSL-2.0",
        name="Apple Public Source License 2.0",
        url=AnyUrl("http://www.opensource.apple.com/license/apsl/"),
    ),  # type: ignore
    "Arphic-1999": CreativeWork(
        identifier="Arphic-1999",
        name="Arphic Public License",
        url=AnyUrl("http://ftp.gnu.org/gnu/non-gnu/chinese-fonts-truetype/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/Arphic-1999": CreativeWork(
        identifier="Arphic-1999",
        name="Arphic Public License",
        url=AnyUrl("http://ftp.gnu.org/gnu/non-gnu/chinese-fonts-truetype/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/Arphic-1999.html": CreativeWork(
        identifier="Arphic-1999",
        name="Arphic Public License",
        url=AnyUrl("http://ftp.gnu.org/gnu/non-gnu/chinese-fonts-truetype/LICENSE"),
    ),  # type: ignore
    "http://ftp.gnu.org/gnu/non-gnu/chinese-fonts-truetype/LICENSE": CreativeWork(
        identifier="Arphic-1999",
        name="Arphic Public License",
        url=AnyUrl("http://ftp.gnu.org/gnu/non-gnu/chinese-fonts-truetype/LICENSE"),
    ),  # type: ignore
    "Artistic-1.0": CreativeWork(
        identifier="Artistic-1.0",
        name="Artistic License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Artistic-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-1.0": CreativeWork(
        identifier="Artistic-1.0",
        name="Artistic License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Artistic-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-1.0.html": CreativeWork(
        identifier="Artistic-1.0",
        name="Artistic License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Artistic-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/Artistic-1.0": CreativeWork(
        identifier="Artistic-1.0",
        name="Artistic License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Artistic-1.0"),
    ),  # type: ignore
    "Artistic-1.0-cl8": CreativeWork(
        identifier="Artistic-1.0-cl8",
        name="Artistic License 1.0 w/clause 8",
        url=AnyUrl("https://opensource.org/licenses/Artistic-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-1.0-cl8": CreativeWork(
        identifier="Artistic-1.0-cl8",
        name="Artistic License 1.0 w/clause 8",
        url=AnyUrl("https://opensource.org/licenses/Artistic-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-1.0-cl8.html": CreativeWork(
        identifier="Artistic-1.0-cl8",
        name="Artistic License 1.0 w/clause 8",
        url=AnyUrl("https://opensource.org/licenses/Artistic-1.0"),
    ),  # type: ignore
    "Artistic-1.0-Perl": CreativeWork(
        identifier="Artistic-1.0-Perl",
        name="Artistic License 1.0 (Perl)",
        url=AnyUrl("http://dev.perl.org/licenses/artistic.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-1.0-Perl": CreativeWork(
        identifier="Artistic-1.0-Perl",
        name="Artistic License 1.0 (Perl)",
        url=AnyUrl("http://dev.perl.org/licenses/artistic.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-1.0-Perl.html": CreativeWork(
        identifier="Artistic-1.0-Perl",
        name="Artistic License 1.0 (Perl)",
        url=AnyUrl("http://dev.perl.org/licenses/artistic.html"),
    ),  # type: ignore
    "http://dev.perl.org/licenses/artistic.html": CreativeWork(
        identifier="Artistic-1.0-Perl",
        name="Artistic License 1.0 (Perl)",
        url=AnyUrl("http://dev.perl.org/licenses/artistic.html"),
    ),  # type: ignore
    "Artistic-2.0": CreativeWork(
        identifier="Artistic-2.0",
        name="Artistic License 2.0",
        url=AnyUrl("http://www.perlfoundation.org/artistic_license_2_0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-2.0": CreativeWork(
        identifier="Artistic-2.0",
        name="Artistic License 2.0",
        url=AnyUrl("http://www.perlfoundation.org/artistic_license_2_0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-2.0.html": CreativeWork(
        identifier="Artistic-2.0",
        name="Artistic License 2.0",
        url=AnyUrl("http://www.perlfoundation.org/artistic_license_2_0"),
    ),  # type: ignore
    "http://www.perlfoundation.org/artistic_license_2_0": CreativeWork(
        identifier="Artistic-2.0",
        name="Artistic License 2.0",
        url=AnyUrl("http://www.perlfoundation.org/artistic_license_2_0"),
    ),  # type: ignore
    "Artistic-dist": CreativeWork(
        identifier="Artistic-dist",
        name="Artistic License 1.0 (dist)",
        url=AnyUrl(
            "https://github.com/pexip/os-perl/blob/833cf4c86cc465ccfc627ff16db67e783156a248/debian/copyright#L2720-L2845"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-dist": CreativeWork(
        identifier="Artistic-dist",
        name="Artistic License 1.0 (dist)",
        url=AnyUrl(
            "https://github.com/pexip/os-perl/blob/833cf4c86cc465ccfc627ff16db67e783156a248/debian/copyright#L2720-L2845"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Artistic-dist.html": CreativeWork(
        identifier="Artistic-dist",
        name="Artistic License 1.0 (dist)",
        url=AnyUrl(
            "https://github.com/pexip/os-perl/blob/833cf4c86cc465ccfc627ff16db67e783156a248/debian/copyright#L2720-L2845"
        ),
    ),  # type: ignore
    "https://github.com/pexip/os-perl/blob/833cf4c86cc465ccfc627ff16db67e783156a248/debian/copyright#L2720-L2845": CreativeWork(
        identifier="Artistic-dist",
        name="Artistic License 1.0 (dist)",
        url=AnyUrl(
            "https://github.com/pexip/os-perl/blob/833cf4c86cc465ccfc627ff16db67e783156a248/debian/copyright#L2720-L2845"
        ),
    ),  # type: ignore
    "Aspell-RU": CreativeWork(
        identifier="Aspell-RU",
        name="Aspell Russian License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/ru/aspell6-ru-0.99f7-1.tar.bz2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Aspell-RU": CreativeWork(
        identifier="Aspell-RU",
        name="Aspell Russian License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/ru/aspell6-ru-0.99f7-1.tar.bz2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Aspell-RU.html": CreativeWork(
        identifier="Aspell-RU",
        name="Aspell Russian License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/ru/aspell6-ru-0.99f7-1.tar.bz2"
        ),
    ),  # type: ignore
    "https://ftp.gnu.org/gnu/aspell/dict/ru/aspell6-ru-0.99f7-1.tar.bz2": CreativeWork(
        identifier="Aspell-RU",
        name="Aspell Russian License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/ru/aspell6-ru-0.99f7-1.tar.bz2"
        ),
    ),  # type: ignore
    "ASWF-Digital-Assets-1.0": CreativeWork(
        identifier="ASWF-Digital-Assets-1.0",
        name="ASWF Digital Assets License version 1.0",
        url=AnyUrl(
            "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.0.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ASWF-Digital-Assets-1.0": CreativeWork(
        identifier="ASWF-Digital-Assets-1.0",
        name="ASWF Digital Assets License version 1.0",
        url=AnyUrl(
            "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.0.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ASWF-Digital-Assets-1.0.html": CreativeWork(
        identifier="ASWF-Digital-Assets-1.0",
        name="ASWF Digital Assets License version 1.0",
        url=AnyUrl(
            "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.0.txt"
        ),
    ),  # type: ignore
    "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.0.txt": CreativeWork(
        identifier="ASWF-Digital-Assets-1.0",
        name="ASWF Digital Assets License version 1.0",
        url=AnyUrl(
            "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.0.txt"
        ),
    ),  # type: ignore
    "ASWF-Digital-Assets-1.1": CreativeWork(
        identifier="ASWF-Digital-Assets-1.1",
        name="ASWF Digital Assets License 1.1",
        url=AnyUrl(
            "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.1.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ASWF-Digital-Assets-1.1": CreativeWork(
        identifier="ASWF-Digital-Assets-1.1",
        name="ASWF Digital Assets License 1.1",
        url=AnyUrl(
            "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.1.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ASWF-Digital-Assets-1.1.html": CreativeWork(
        identifier="ASWF-Digital-Assets-1.1",
        name="ASWF Digital Assets License 1.1",
        url=AnyUrl(
            "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.1.txt"
        ),
    ),  # type: ignore
    "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.1.txt": CreativeWork(
        identifier="ASWF-Digital-Assets-1.1",
        name="ASWF Digital Assets License 1.1",
        url=AnyUrl(
            "https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.1.txt"
        ),
    ),  # type: ignore
    "Baekmuk": CreativeWork(
        identifier="Baekmuk",
        name="Baekmuk License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:Baekmuk?rd=Licensing/Baekmuk"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Baekmuk": CreativeWork(
        identifier="Baekmuk",
        name="Baekmuk License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:Baekmuk?rd=Licensing/Baekmuk"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Baekmuk.html": CreativeWork(
        identifier="Baekmuk",
        name="Baekmuk License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:Baekmuk?rd=Licensing/Baekmuk"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing:Baekmuk?rd=Licensing/Baekmuk": CreativeWork(
        identifier="Baekmuk",
        name="Baekmuk License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:Baekmuk?rd=Licensing/Baekmuk"
        ),
    ),  # type: ignore
    "Bahyph": CreativeWork(
        identifier="Bahyph",
        name="Bahyph License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Bahyph"),
    ),  # type: ignore
    "https://spdx.org/licenses/Bahyph": CreativeWork(
        identifier="Bahyph",
        name="Bahyph License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Bahyph"),
    ),  # type: ignore
    "https://spdx.org/licenses/Bahyph.html": CreativeWork(
        identifier="Bahyph",
        name="Bahyph License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Bahyph"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Bahyph": CreativeWork(
        identifier="Bahyph",
        name="Bahyph License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Bahyph"),
    ),  # type: ignore
    "Barr": CreativeWork(
        identifier="Barr",
        name="Barr License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Barr"),
    ),  # type: ignore
    "https://spdx.org/licenses/Barr": CreativeWork(
        identifier="Barr",
        name="Barr License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Barr"),
    ),  # type: ignore
    "https://spdx.org/licenses/Barr.html": CreativeWork(
        identifier="Barr",
        name="Barr License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Barr"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Barr": CreativeWork(
        identifier="Barr",
        name="Barr License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Barr"),
    ),  # type: ignore
    "bcrypt-Solar-Designer": CreativeWork(
        identifier="bcrypt-Solar-Designer",
        name="bcrypt Solar Designer License",
        url=AnyUrl(
            "https://github.com/bcrypt-ruby/bcrypt-ruby/blob/master/ext/mri/crypt_blowfish.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/bcrypt-Solar-Designer": CreativeWork(
        identifier="bcrypt-Solar-Designer",
        name="bcrypt Solar Designer License",
        url=AnyUrl(
            "https://github.com/bcrypt-ruby/bcrypt-ruby/blob/master/ext/mri/crypt_blowfish.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/bcrypt-Solar-Designer.html": CreativeWork(
        identifier="bcrypt-Solar-Designer",
        name="bcrypt Solar Designer License",
        url=AnyUrl(
            "https://github.com/bcrypt-ruby/bcrypt-ruby/blob/master/ext/mri/crypt_blowfish.c"
        ),
    ),  # type: ignore
    "https://github.com/bcrypt-ruby/bcrypt-ruby/blob/master/ext/mri/crypt_blowfish.c": CreativeWork(
        identifier="bcrypt-Solar-Designer",
        name="bcrypt Solar Designer License",
        url=AnyUrl(
            "https://github.com/bcrypt-ruby/bcrypt-ruby/blob/master/ext/mri/crypt_blowfish.c"
        ),
    ),  # type: ignore
    "Beerware": CreativeWork(
        identifier="Beerware",
        name="Beerware License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Beerware"),
    ),  # type: ignore
    "https://spdx.org/licenses/Beerware": CreativeWork(
        identifier="Beerware",
        name="Beerware License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Beerware"),
    ),  # type: ignore
    "https://spdx.org/licenses/Beerware.html": CreativeWork(
        identifier="Beerware",
        name="Beerware License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Beerware"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Beerware": CreativeWork(
        identifier="Beerware",
        name="Beerware License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Beerware"),
    ),  # type: ignore
    "Bitstream-Charter": CreativeWork(
        identifier="Bitstream-Charter",
        name="Bitstream Charter Font License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Charter#License_Text"),
    ),  # type: ignore
    "https://spdx.org/licenses/Bitstream-Charter": CreativeWork(
        identifier="Bitstream-Charter",
        name="Bitstream Charter Font License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Charter#License_Text"),
    ),  # type: ignore
    "https://spdx.org/licenses/Bitstream-Charter.html": CreativeWork(
        identifier="Bitstream-Charter",
        name="Bitstream Charter Font License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Charter#License_Text"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Charter#License_Text": CreativeWork(
        identifier="Bitstream-Charter",
        name="Bitstream Charter Font License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Charter#License_Text"),
    ),  # type: ignore
    "Bitstream-Vera": CreativeWork(
        identifier="Bitstream-Vera",
        name="Bitstream Vera Font License",
        url=AnyUrl(
            "https://web.archive.org/web/20080207013128/http://www.gnome.org/fonts/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Bitstream-Vera": CreativeWork(
        identifier="Bitstream-Vera",
        name="Bitstream Vera Font License",
        url=AnyUrl(
            "https://web.archive.org/web/20080207013128/http://www.gnome.org/fonts/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Bitstream-Vera.html": CreativeWork(
        identifier="Bitstream-Vera",
        name="Bitstream Vera Font License",
        url=AnyUrl(
            "https://web.archive.org/web/20080207013128/http://www.gnome.org/fonts/"
        ),
    ),  # type: ignore
    "https://web.archive.org/web/20080207013128/http://www.gnome.org/fonts/": CreativeWork(
        identifier="Bitstream-Vera",
        name="Bitstream Vera Font License",
        url=AnyUrl(
            "https://web.archive.org/web/20080207013128/http://www.gnome.org/fonts/"
        ),
    ),  # type: ignore
    "BitTorrent-1.0": CreativeWork(
        identifier="BitTorrent-1.0",
        name="BitTorrent Open Source License v1.0",
        url=AnyUrl(
            "http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/licenses/BitTorrent?r1=1.1&r2=1.1.1.1&diff_format=s"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BitTorrent-1.0": CreativeWork(
        identifier="BitTorrent-1.0",
        name="BitTorrent Open Source License v1.0",
        url=AnyUrl(
            "http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/licenses/BitTorrent?r1=1.1&r2=1.1.1.1&diff_format=s"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BitTorrent-1.0.html": CreativeWork(
        identifier="BitTorrent-1.0",
        name="BitTorrent Open Source License v1.0",
        url=AnyUrl(
            "http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/licenses/BitTorrent?r1=1.1&r2=1.1.1.1&diff_format=s"
        ),
    ),  # type: ignore
    "http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/licenses/BitTorrent?r1=1.1&r2=1.1.1.1&diff_format=s": CreativeWork(
        identifier="BitTorrent-1.0",
        name="BitTorrent Open Source License v1.0",
        url=AnyUrl(
            "http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/licenses/BitTorrent?r1=1.1&r2=1.1.1.1&diff_format=s"
        ),
    ),  # type: ignore
    "BitTorrent-1.1": CreativeWork(
        identifier="BitTorrent-1.1",
        name="BitTorrent Open Source License v1.1",
        url=AnyUrl("http://directory.fsf.org/wiki/License:BitTorrentOSL1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/BitTorrent-1.1": CreativeWork(
        identifier="BitTorrent-1.1",
        name="BitTorrent Open Source License v1.1",
        url=AnyUrl("http://directory.fsf.org/wiki/License:BitTorrentOSL1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/BitTorrent-1.1.html": CreativeWork(
        identifier="BitTorrent-1.1",
        name="BitTorrent Open Source License v1.1",
        url=AnyUrl("http://directory.fsf.org/wiki/License:BitTorrentOSL1.1"),
    ),  # type: ignore
    "http://directory.fsf.org/wiki/License:BitTorrentOSL1.1": CreativeWork(
        identifier="BitTorrent-1.1",
        name="BitTorrent Open Source License v1.1",
        url=AnyUrl("http://directory.fsf.org/wiki/License:BitTorrentOSL1.1"),
    ),  # type: ignore
    "blessing": CreativeWork(
        identifier="blessing",
        name="SQLite Blessing",
        url=AnyUrl("https://www.sqlite.org/src/artifact/e33a4df7e32d742a?ln=4-9"),
    ),  # type: ignore
    "https://spdx.org/licenses/blessing": CreativeWork(
        identifier="blessing",
        name="SQLite Blessing",
        url=AnyUrl("https://www.sqlite.org/src/artifact/e33a4df7e32d742a?ln=4-9"),
    ),  # type: ignore
    "https://spdx.org/licenses/blessing.html": CreativeWork(
        identifier="blessing",
        name="SQLite Blessing",
        url=AnyUrl("https://www.sqlite.org/src/artifact/e33a4df7e32d742a?ln=4-9"),
    ),  # type: ignore
    "https://www.sqlite.org/src/artifact/e33a4df7e32d742a?ln=4-9": CreativeWork(
        identifier="blessing",
        name="SQLite Blessing",
        url=AnyUrl("https://www.sqlite.org/src/artifact/e33a4df7e32d742a?ln=4-9"),
    ),  # type: ignore
    "BlueOak-1.0.0": CreativeWork(
        identifier="BlueOak-1.0.0",
        name="Blue Oak Model License 1.0.0",
        url=AnyUrl("https://blueoakcouncil.org/license/1.0.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/BlueOak-1.0.0": CreativeWork(
        identifier="BlueOak-1.0.0",
        name="Blue Oak Model License 1.0.0",
        url=AnyUrl("https://blueoakcouncil.org/license/1.0.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/BlueOak-1.0.0.html": CreativeWork(
        identifier="BlueOak-1.0.0",
        name="Blue Oak Model License 1.0.0",
        url=AnyUrl("https://blueoakcouncil.org/license/1.0.0"),
    ),  # type: ignore
    "https://blueoakcouncil.org/license/1.0.0": CreativeWork(
        identifier="BlueOak-1.0.0",
        name="Blue Oak Model License 1.0.0",
        url=AnyUrl("https://blueoakcouncil.org/license/1.0.0"),
    ),  # type: ignore
    "Boehm-GC": CreativeWork(
        identifier="Boehm-GC",
        name="Boehm-Demers-Weiser GC License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:MIT#Another_Minimal_variant_(found_in_libatomic_ops)"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Boehm-GC": CreativeWork(
        identifier="Boehm-GC",
        name="Boehm-Demers-Weiser GC License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:MIT#Another_Minimal_variant_(found_in_libatomic_ops)"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Boehm-GC.html": CreativeWork(
        identifier="Boehm-GC",
        name="Boehm-Demers-Weiser GC License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:MIT#Another_Minimal_variant_(found_in_libatomic_ops)"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing:MIT#Another_Minimal_variant_(found_in_libatomic_ops)": CreativeWork(
        identifier="Boehm-GC",
        name="Boehm-Demers-Weiser GC License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:MIT#Another_Minimal_variant_(found_in_libatomic_ops)"
        ),
    ),  # type: ignore
    "Boehm-GC-without-fee": CreativeWork(
        identifier="Boehm-GC-without-fee",
        name="Boehm-Demers-Weiser GC License (without fee)",
        url=AnyUrl("https://github.com/MariaDB/server/blob/11.6/libmysqld/lib_sql.cc"),
    ),  # type: ignore
    "https://spdx.org/licenses/Boehm-GC-without-fee": CreativeWork(
        identifier="Boehm-GC-without-fee",
        name="Boehm-Demers-Weiser GC License (without fee)",
        url=AnyUrl("https://github.com/MariaDB/server/blob/11.6/libmysqld/lib_sql.cc"),
    ),  # type: ignore
    "https://spdx.org/licenses/Boehm-GC-without-fee.html": CreativeWork(
        identifier="Boehm-GC-without-fee",
        name="Boehm-Demers-Weiser GC License (without fee)",
        url=AnyUrl("https://github.com/MariaDB/server/blob/11.6/libmysqld/lib_sql.cc"),
    ),  # type: ignore
    "https://github.com/MariaDB/server/blob/11.6/libmysqld/lib_sql.cc": CreativeWork(
        identifier="Boehm-GC-without-fee",
        name="Boehm-Demers-Weiser GC License (without fee)",
        url=AnyUrl("https://github.com/MariaDB/server/blob/11.6/libmysqld/lib_sql.cc"),
    ),  # type: ignore
    "BOLA-1.1": CreativeWork(
        identifier="BOLA-1.1",
        name="Buena Onda License Agreement v1.1",
        url=AnyUrl("https://blitiri.com.ar/p/bola/"),
    ),  # type: ignore
    "https://spdx.org/licenses/BOLA-1.1": CreativeWork(
        identifier="BOLA-1.1",
        name="Buena Onda License Agreement v1.1",
        url=AnyUrl("https://blitiri.com.ar/p/bola/"),
    ),  # type: ignore
    "https://spdx.org/licenses/BOLA-1.1.html": CreativeWork(
        identifier="BOLA-1.1",
        name="Buena Onda License Agreement v1.1",
        url=AnyUrl("https://blitiri.com.ar/p/bola/"),
    ),  # type: ignore
    "https://blitiri.com.ar/p/bola/": CreativeWork(
        identifier="BOLA-1.1",
        name="Buena Onda License Agreement v1.1",
        url=AnyUrl("https://blitiri.com.ar/p/bola/"),
    ),  # type: ignore
    "Borceux": CreativeWork(
        identifier="Borceux",
        name="Borceux license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Borceux"),
    ),  # type: ignore
    "https://spdx.org/licenses/Borceux": CreativeWork(
        identifier="Borceux",
        name="Borceux license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Borceux"),
    ),  # type: ignore
    "https://spdx.org/licenses/Borceux.html": CreativeWork(
        identifier="Borceux",
        name="Borceux license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Borceux"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Borceux": CreativeWork(
        identifier="Borceux",
        name="Borceux license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Borceux"),
    ),  # type: ignore
    "Brian-Gladman-2-Clause": CreativeWork(
        identifier="Brian-Gladman-2-Clause",
        name="Brian Gladman 2-Clause License",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L140-L156"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Brian-Gladman-2-Clause": CreativeWork(
        identifier="Brian-Gladman-2-Clause",
        name="Brian Gladman 2-Clause License",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L140-L156"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Brian-Gladman-2-Clause.html": CreativeWork(
        identifier="Brian-Gladman-2-Clause",
        name="Brian Gladman 2-Clause License",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L140-L156"
        ),
    ),  # type: ignore
    "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L140-L156": CreativeWork(
        identifier="Brian-Gladman-2-Clause",
        name="Brian Gladman 2-Clause License",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L140-L156"
        ),
    ),  # type: ignore
    "Brian-Gladman-3-Clause": CreativeWork(
        identifier="Brian-Gladman-3-Clause",
        name="Brian Gladman 3-Clause License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/packages-clib/blob/master/sha1/brg_endian.h"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Brian-Gladman-3-Clause": CreativeWork(
        identifier="Brian-Gladman-3-Clause",
        name="Brian Gladman 3-Clause License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/packages-clib/blob/master/sha1/brg_endian.h"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Brian-Gladman-3-Clause.html": CreativeWork(
        identifier="Brian-Gladman-3-Clause",
        name="Brian Gladman 3-Clause License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/packages-clib/blob/master/sha1/brg_endian.h"
        ),
    ),  # type: ignore
    "https://github.com/SWI-Prolog/packages-clib/blob/master/sha1/brg_endian.h": CreativeWork(
        identifier="Brian-Gladman-3-Clause",
        name="Brian Gladman 3-Clause License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/packages-clib/blob/master/sha1/brg_endian.h"
        ),
    ),  # type: ignore
    "BSD-1-Clause": CreativeWork(
        identifier="BSD-1-Clause",
        name="BSD 1-Clause License",
        url=AnyUrl(
            "https://svnweb.freebsd.org/base/head/include/ifaddrs.h?revision=326823"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-1-Clause": CreativeWork(
        identifier="BSD-1-Clause",
        name="BSD 1-Clause License",
        url=AnyUrl(
            "https://svnweb.freebsd.org/base/head/include/ifaddrs.h?revision=326823"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-1-Clause.html": CreativeWork(
        identifier="BSD-1-Clause",
        name="BSD 1-Clause License",
        url=AnyUrl(
            "https://svnweb.freebsd.org/base/head/include/ifaddrs.h?revision=326823"
        ),
    ),  # type: ignore
    "https://svnweb.freebsd.org/base/head/include/ifaddrs.h?revision=326823": CreativeWork(
        identifier="BSD-1-Clause",
        name="BSD 1-Clause License",
        url=AnyUrl(
            "https://svnweb.freebsd.org/base/head/include/ifaddrs.h?revision=326823"
        ),
    ),  # type: ignore
    "BSD-2-Clause": CreativeWork(
        identifier="BSD-2-Clause",
        name='BSD 2-Clause "Simplified" License',
        url=AnyUrl("https://opensource.org/licenses/BSD-2-Clause"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause": CreativeWork(
        identifier="BSD-2-Clause",
        name='BSD 2-Clause "Simplified" License',
        url=AnyUrl("https://opensource.org/licenses/BSD-2-Clause"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause.html": CreativeWork(
        identifier="BSD-2-Clause",
        name='BSD 2-Clause "Simplified" License',
        url=AnyUrl("https://opensource.org/licenses/BSD-2-Clause"),
    ),  # type: ignore
    "https://opensource.org/licenses/BSD-2-Clause": CreativeWork(
        identifier="BSD-2-Clause",
        name='BSD 2-Clause "Simplified" License',
        url=AnyUrl("https://opensource.org/licenses/BSD-2-Clause"),
    ),  # type: ignore
    "BSD-2-Clause-Darwin": CreativeWork(
        identifier="BSD-2-Clause-Darwin",
        name="BSD 2-Clause - Ian Darwin variant",
        url=AnyUrl("https://github.com/file/file/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-Darwin": CreativeWork(
        identifier="BSD-2-Clause-Darwin",
        name="BSD 2-Clause - Ian Darwin variant",
        url=AnyUrl("https://github.com/file/file/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-Darwin.html": CreativeWork(
        identifier="BSD-2-Clause-Darwin",
        name="BSD 2-Clause - Ian Darwin variant",
        url=AnyUrl("https://github.com/file/file/blob/master/COPYING"),
    ),  # type: ignore
    "https://github.com/file/file/blob/master/COPYING": CreativeWork(
        identifier="BSD-2-Clause-Darwin",
        name="BSD 2-Clause - Ian Darwin variant",
        url=AnyUrl("https://github.com/file/file/blob/master/COPYING"),
    ),  # type: ignore
    "BSD-2-Clause-first-lines": CreativeWork(
        identifier="BSD-2-Clause-first-lines",
        name="BSD 2-Clause - first lines requirement",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L664-L690"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-first-lines": CreativeWork(
        identifier="BSD-2-Clause-first-lines",
        name="BSD 2-Clause - first lines requirement",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L664-L690"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-first-lines.html": CreativeWork(
        identifier="BSD-2-Clause-first-lines",
        name="BSD 2-Clause - first lines requirement",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L664-L690"
        ),
    ),  # type: ignore
    "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L664-L690": CreativeWork(
        identifier="BSD-2-Clause-first-lines",
        name="BSD 2-Clause - first lines requirement",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L664-L690"
        ),
    ),  # type: ignore
    "BSD-2-Clause-FreeBSD": CreativeWork(
        identifier="BSD-2-Clause-FreeBSD",
        name="BSD 2-Clause FreeBSD License",
        url=AnyUrl("http://www.freebsd.org/copyright/freebsd-license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-FreeBSD": CreativeWork(
        identifier="BSD-2-Clause-FreeBSD",
        name="BSD 2-Clause FreeBSD License",
        url=AnyUrl("http://www.freebsd.org/copyright/freebsd-license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-FreeBSD.html": CreativeWork(
        identifier="BSD-2-Clause-FreeBSD",
        name="BSD 2-Clause FreeBSD License",
        url=AnyUrl("http://www.freebsd.org/copyright/freebsd-license.html"),
    ),  # type: ignore
    "http://www.freebsd.org/copyright/freebsd-license.html": CreativeWork(
        identifier="BSD-2-Clause-FreeBSD",
        name="BSD 2-Clause FreeBSD License",
        url=AnyUrl("http://www.freebsd.org/copyright/freebsd-license.html"),
    ),  # type: ignore
    "BSD-2-Clause-NetBSD": CreativeWork(
        identifier="BSD-2-Clause-NetBSD",
        name="BSD 2-Clause NetBSD License",
        url=AnyUrl("http://www.netbsd.org/about/redistribution.html#default"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-NetBSD": CreativeWork(
        identifier="BSD-2-Clause-NetBSD",
        name="BSD 2-Clause NetBSD License",
        url=AnyUrl("http://www.netbsd.org/about/redistribution.html#default"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-NetBSD.html": CreativeWork(
        identifier="BSD-2-Clause-NetBSD",
        name="BSD 2-Clause NetBSD License",
        url=AnyUrl("http://www.netbsd.org/about/redistribution.html#default"),
    ),  # type: ignore
    "http://www.netbsd.org/about/redistribution.html#default": CreativeWork(
        identifier="BSD-2-Clause-NetBSD",
        name="BSD 2-Clause NetBSD License",
        url=AnyUrl("http://www.netbsd.org/about/redistribution.html#default"),
    ),  # type: ignore
    "BSD-2-Clause-Patent": CreativeWork(
        identifier="BSD-2-Clause-Patent",
        name="BSD-2-Clause Plus Patent License",
        url=AnyUrl("https://opensource.org/licenses/BSDplusPatent"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-Patent": CreativeWork(
        identifier="BSD-2-Clause-Patent",
        name="BSD-2-Clause Plus Patent License",
        url=AnyUrl("https://opensource.org/licenses/BSDplusPatent"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-Patent.html": CreativeWork(
        identifier="BSD-2-Clause-Patent",
        name="BSD-2-Clause Plus Patent License",
        url=AnyUrl("https://opensource.org/licenses/BSDplusPatent"),
    ),  # type: ignore
    "https://opensource.org/licenses/BSDplusPatent": CreativeWork(
        identifier="BSD-2-Clause-Patent",
        name="BSD-2-Clause Plus Patent License",
        url=AnyUrl("https://opensource.org/licenses/BSDplusPatent"),
    ),  # type: ignore
    "BSD-2-Clause-pkgconf-disclaimer": CreativeWork(
        identifier="BSD-2-Clause-pkgconf-disclaimer",
        name="BSD 2-Clause pkgconf disclaimer variant",
        url=AnyUrl(
            "https://github.com/audacious-media-player/audacious/blob/master/src/audacious/main.cc"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-pkgconf-disclaimer": CreativeWork(
        identifier="BSD-2-Clause-pkgconf-disclaimer",
        name="BSD 2-Clause pkgconf disclaimer variant",
        url=AnyUrl(
            "https://github.com/audacious-media-player/audacious/blob/master/src/audacious/main.cc"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-pkgconf-disclaimer.html": CreativeWork(
        identifier="BSD-2-Clause-pkgconf-disclaimer",
        name="BSD 2-Clause pkgconf disclaimer variant",
        url=AnyUrl(
            "https://github.com/audacious-media-player/audacious/blob/master/src/audacious/main.cc"
        ),
    ),  # type: ignore
    "https://github.com/audacious-media-player/audacious/blob/master/src/audacious/main.cc": CreativeWork(
        identifier="BSD-2-Clause-pkgconf-disclaimer",
        name="BSD 2-Clause pkgconf disclaimer variant",
        url=AnyUrl(
            "https://github.com/audacious-media-player/audacious/blob/master/src/audacious/main.cc"
        ),
    ),  # type: ignore
    "BSD-2-Clause-Views": CreativeWork(
        identifier="BSD-2-Clause-Views",
        name="BSD 2-Clause with views sentence",
        url=AnyUrl("http://www.freebsd.org/copyright/freebsd-license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-Views": CreativeWork(
        identifier="BSD-2-Clause-Views",
        name="BSD 2-Clause with views sentence",
        url=AnyUrl("http://www.freebsd.org/copyright/freebsd-license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-2-Clause-Views.html": CreativeWork(
        identifier="BSD-2-Clause-Views",
        name="BSD 2-Clause with views sentence",
        url=AnyUrl("http://www.freebsd.org/copyright/freebsd-license.html"),
    ),  # type: ignore
    "BSD-3-Clause": CreativeWork(
        identifier="BSD-3-Clause",
        name='BSD 3-Clause "New" or "Revised" License',
        url=AnyUrl("https://opensource.org/licenses/BSD-3-Clause"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause": CreativeWork(
        identifier="BSD-3-Clause",
        name='BSD 3-Clause "New" or "Revised" License',
        url=AnyUrl("https://opensource.org/licenses/BSD-3-Clause"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause.html": CreativeWork(
        identifier="BSD-3-Clause",
        name='BSD 3-Clause "New" or "Revised" License',
        url=AnyUrl("https://opensource.org/licenses/BSD-3-Clause"),
    ),  # type: ignore
    "https://opensource.org/licenses/BSD-3-Clause": CreativeWork(
        identifier="BSD-3-Clause",
        name='BSD 3-Clause "New" or "Revised" License',
        url=AnyUrl("https://opensource.org/licenses/BSD-3-Clause"),
    ),  # type: ignore
    "BSD-3-Clause-acpica": CreativeWork(
        identifier="BSD-3-Clause-acpica",
        name="BSD 3-Clause acpica variant",
        url=AnyUrl(
            "https://github.com/acpica/acpica/blob/master/source/common/acfileio.c#L119"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-acpica": CreativeWork(
        identifier="BSD-3-Clause-acpica",
        name="BSD 3-Clause acpica variant",
        url=AnyUrl(
            "https://github.com/acpica/acpica/blob/master/source/common/acfileio.c#L119"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-acpica.html": CreativeWork(
        identifier="BSD-3-Clause-acpica",
        name="BSD 3-Clause acpica variant",
        url=AnyUrl(
            "https://github.com/acpica/acpica/blob/master/source/common/acfileio.c#L119"
        ),
    ),  # type: ignore
    "https://github.com/acpica/acpica/blob/master/source/common/acfileio.c#L119": CreativeWork(
        identifier="BSD-3-Clause-acpica",
        name="BSD 3-Clause acpica variant",
        url=AnyUrl(
            "https://github.com/acpica/acpica/blob/master/source/common/acfileio.c#L119"
        ),
    ),  # type: ignore
    "BSD-3-Clause-Attribution": CreativeWork(
        identifier="BSD-3-Clause-Attribution",
        name="BSD with attribution",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD_with_Attribution"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Attribution": CreativeWork(
        identifier="BSD-3-Clause-Attribution",
        name="BSD with attribution",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD_with_Attribution"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Attribution.html": CreativeWork(
        identifier="BSD-3-Clause-Attribution",
        name="BSD with attribution",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD_with_Attribution"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/BSD_with_Attribution": CreativeWork(
        identifier="BSD-3-Clause-Attribution",
        name="BSD with attribution",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD_with_Attribution"),
    ),  # type: ignore
    "BSD-3-Clause-Clear": CreativeWork(
        identifier="BSD-3-Clause-Clear",
        name="BSD 3-Clause Clear License",
        url=AnyUrl("http://labs.metacarta.com/license-explanation.html#license"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Clear": CreativeWork(
        identifier="BSD-3-Clause-Clear",
        name="BSD 3-Clause Clear License",
        url=AnyUrl("http://labs.metacarta.com/license-explanation.html#license"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Clear.html": CreativeWork(
        identifier="BSD-3-Clause-Clear",
        name="BSD 3-Clause Clear License",
        url=AnyUrl("http://labs.metacarta.com/license-explanation.html#license"),
    ),  # type: ignore
    "http://labs.metacarta.com/license-explanation.html#license": CreativeWork(
        identifier="BSD-3-Clause-Clear",
        name="BSD 3-Clause Clear License",
        url=AnyUrl("http://labs.metacarta.com/license-explanation.html#license"),
    ),  # type: ignore
    "BSD-3-Clause-flex": CreativeWork(
        identifier="BSD-3-Clause-flex",
        name="BSD 3-Clause Flex variant",
        url=AnyUrl("https://github.com/westes/flex/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-flex": CreativeWork(
        identifier="BSD-3-Clause-flex",
        name="BSD 3-Clause Flex variant",
        url=AnyUrl("https://github.com/westes/flex/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-flex.html": CreativeWork(
        identifier="BSD-3-Clause-flex",
        name="BSD 3-Clause Flex variant",
        url=AnyUrl("https://github.com/westes/flex/blob/master/COPYING"),
    ),  # type: ignore
    "https://github.com/westes/flex/blob/master/COPYING": CreativeWork(
        identifier="BSD-3-Clause-flex",
        name="BSD 3-Clause Flex variant",
        url=AnyUrl("https://github.com/westes/flex/blob/master/COPYING"),
    ),  # type: ignore
    "BSD-3-Clause-HP": CreativeWork(
        identifier="BSD-3-Clause-HP",
        name="Hewlett-Packard BSD variant license",
        url=AnyUrl("https://github.com/zdohnal/hplip/blob/master/COPYING#L939"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-HP": CreativeWork(
        identifier="BSD-3-Clause-HP",
        name="Hewlett-Packard BSD variant license",
        url=AnyUrl("https://github.com/zdohnal/hplip/blob/master/COPYING#L939"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-HP.html": CreativeWork(
        identifier="BSD-3-Clause-HP",
        name="Hewlett-Packard BSD variant license",
        url=AnyUrl("https://github.com/zdohnal/hplip/blob/master/COPYING#L939"),
    ),  # type: ignore
    "https://github.com/zdohnal/hplip/blob/master/COPYING#L939": CreativeWork(
        identifier="BSD-3-Clause-HP",
        name="Hewlett-Packard BSD variant license",
        url=AnyUrl("https://github.com/zdohnal/hplip/blob/master/COPYING#L939"),
    ),  # type: ignore
    "BSD-3-Clause-LBNL": CreativeWork(
        identifier="BSD-3-Clause-LBNL",
        name="Lawrence Berkeley National Labs BSD variant license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/LBNLBSD"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-LBNL": CreativeWork(
        identifier="BSD-3-Clause-LBNL",
        name="Lawrence Berkeley National Labs BSD variant license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/LBNLBSD"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-LBNL.html": CreativeWork(
        identifier="BSD-3-Clause-LBNL",
        name="Lawrence Berkeley National Labs BSD variant license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/LBNLBSD"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/LBNLBSD": CreativeWork(
        identifier="BSD-3-Clause-LBNL",
        name="Lawrence Berkeley National Labs BSD variant license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/LBNLBSD"),
    ),  # type: ignore
    "BSD-3-Clause-Modification": CreativeWork(
        identifier="BSD-3-Clause-Modification",
        name="BSD 3-Clause Modification",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:BSD#Modification_Variant"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Modification": CreativeWork(
        identifier="BSD-3-Clause-Modification",
        name="BSD 3-Clause Modification",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:BSD#Modification_Variant"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Modification.html": CreativeWork(
        identifier="BSD-3-Clause-Modification",
        name="BSD 3-Clause Modification",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:BSD#Modification_Variant"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing:BSD#Modification_Variant": CreativeWork(
        identifier="BSD-3-Clause-Modification",
        name="BSD 3-Clause Modification",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:BSD#Modification_Variant"),
    ),  # type: ignore
    "BSD-3-Clause-No-Military-License": CreativeWork(
        identifier="BSD-3-Clause-No-Military-License",
        name="BSD 3-Clause No Military License",
        url=AnyUrl("https://gitlab.syncad.com/hive/dhive/-/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-No-Military-License": CreativeWork(
        identifier="BSD-3-Clause-No-Military-License",
        name="BSD 3-Clause No Military License",
        url=AnyUrl("https://gitlab.syncad.com/hive/dhive/-/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-No-Military-License.html": CreativeWork(
        identifier="BSD-3-Clause-No-Military-License",
        name="BSD 3-Clause No Military License",
        url=AnyUrl("https://gitlab.syncad.com/hive/dhive/-/blob/master/LICENSE"),
    ),  # type: ignore
    "https://gitlab.syncad.com/hive/dhive/-/blob/master/LICENSE": CreativeWork(
        identifier="BSD-3-Clause-No-Military-License",
        name="BSD 3-Clause No Military License",
        url=AnyUrl("https://gitlab.syncad.com/hive/dhive/-/blob/master/LICENSE"),
    ),  # type: ignore
    "BSD-3-Clause-No-Nuclear-License": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-License",
        name="BSD 3-Clause No Nuclear License",
        url=AnyUrl("http://download.oracle.com/otn-pub/java/licenses/bsd.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-License",
        name="BSD 3-Clause No Nuclear License",
        url=AnyUrl("http://download.oracle.com/otn-pub/java/licenses/bsd.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License.html": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-License",
        name="BSD 3-Clause No Nuclear License",
        url=AnyUrl("http://download.oracle.com/otn-pub/java/licenses/bsd.txt"),
    ),  # type: ignore
    "http://download.oracle.com/otn-pub/java/licenses/bsd.txt": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-License",
        name="BSD 3-Clause No Nuclear License",
        url=AnyUrl("http://download.oracle.com/otn-pub/java/licenses/bsd.txt"),
    ),  # type: ignore
    "BSD-3-Clause-No-Nuclear-License-2014": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-License-2014",
        name="BSD 3-Clause No Nuclear License 2014",
        url=AnyUrl("https://java.net/projects/javaeetutorial/pages/BerkeleyLicense"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License-2014": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-License-2014",
        name="BSD 3-Clause No Nuclear License 2014",
        url=AnyUrl("https://java.net/projects/javaeetutorial/pages/BerkeleyLicense"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License-2014.html": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-License-2014",
        name="BSD 3-Clause No Nuclear License 2014",
        url=AnyUrl("https://java.net/projects/javaeetutorial/pages/BerkeleyLicense"),
    ),  # type: ignore
    "https://java.net/projects/javaeetutorial/pages/BerkeleyLicense": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-License-2014",
        name="BSD 3-Clause No Nuclear License 2014",
        url=AnyUrl("https://java.net/projects/javaeetutorial/pages/BerkeleyLicense"),
    ),  # type: ignore
    "BSD-3-Clause-No-Nuclear-Warranty": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-Warranty",
        name="BSD 3-Clause No Nuclear Warranty",
        url=AnyUrl("https://jogamp.org/git/?p=gluegen.git;a=blob_plain;f=LICENSE.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-Warranty": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-Warranty",
        name="BSD 3-Clause No Nuclear Warranty",
        url=AnyUrl("https://jogamp.org/git/?p=gluegen.git;a=blob_plain;f=LICENSE.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-Warranty.html": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-Warranty",
        name="BSD 3-Clause No Nuclear Warranty",
        url=AnyUrl("https://jogamp.org/git/?p=gluegen.git;a=blob_plain;f=LICENSE.txt"),
    ),  # type: ignore
    "https://jogamp.org/git/?p=gluegen.git;a=blob_plain;f=LICENSE.txt": CreativeWork(
        identifier="BSD-3-Clause-No-Nuclear-Warranty",
        name="BSD 3-Clause No Nuclear Warranty",
        url=AnyUrl("https://jogamp.org/git/?p=gluegen.git;a=blob_plain;f=LICENSE.txt"),
    ),  # type: ignore
    "BSD-3-Clause-Open-MPI": CreativeWork(
        identifier="BSD-3-Clause-Open-MPI",
        name="BSD 3-Clause Open MPI variant",
        url=AnyUrl("https://www.open-mpi.org/community/license.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Open-MPI": CreativeWork(
        identifier="BSD-3-Clause-Open-MPI",
        name="BSD 3-Clause Open MPI variant",
        url=AnyUrl("https://www.open-mpi.org/community/license.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Open-MPI.html": CreativeWork(
        identifier="BSD-3-Clause-Open-MPI",
        name="BSD 3-Clause Open MPI variant",
        url=AnyUrl("https://www.open-mpi.org/community/license.php"),
    ),  # type: ignore
    "https://www.open-mpi.org/community/license.php": CreativeWork(
        identifier="BSD-3-Clause-Open-MPI",
        name="BSD 3-Clause Open MPI variant",
        url=AnyUrl("https://www.open-mpi.org/community/license.php"),
    ),  # type: ignore
    "BSD-3-Clause-Sun": CreativeWork(
        identifier="BSD-3-Clause-Sun",
        name="BSD 3-Clause Sun Microsystems",
        url=AnyUrl(
            "https://github.com/xmlark/msv/blob/b9316e2f2270bc1606952ea4939ec87fbba157f3/xsdlib/src/main/java/com/sun/msv/datatype/regexp/InternalImpl.java"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Sun": CreativeWork(
        identifier="BSD-3-Clause-Sun",
        name="BSD 3-Clause Sun Microsystems",
        url=AnyUrl(
            "https://github.com/xmlark/msv/blob/b9316e2f2270bc1606952ea4939ec87fbba157f3/xsdlib/src/main/java/com/sun/msv/datatype/regexp/InternalImpl.java"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Sun.html": CreativeWork(
        identifier="BSD-3-Clause-Sun",
        name="BSD 3-Clause Sun Microsystems",
        url=AnyUrl(
            "https://github.com/xmlark/msv/blob/b9316e2f2270bc1606952ea4939ec87fbba157f3/xsdlib/src/main/java/com/sun/msv/datatype/regexp/InternalImpl.java"
        ),
    ),  # type: ignore
    "https://github.com/xmlark/msv/blob/b9316e2f2270bc1606952ea4939ec87fbba157f3/xsdlib/src/main/java/com/sun/msv/datatype/regexp/InternalImpl.java": CreativeWork(
        identifier="BSD-3-Clause-Sun",
        name="BSD 3-Clause Sun Microsystems",
        url=AnyUrl(
            "https://github.com/xmlark/msv/blob/b9316e2f2270bc1606952ea4939ec87fbba157f3/xsdlib/src/main/java/com/sun/msv/datatype/regexp/InternalImpl.java"
        ),
    ),  # type: ignore
    "BSD-3-Clause-Tso": CreativeWork(
        identifier="BSD-3-Clause-Tso",
        name="BSD 3-Clause Tso variant",
        url=AnyUrl(
            "https://www.x.org/archive/current/doc/xorg-docs/License.html#Theodore_Tso"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Tso": CreativeWork(
        identifier="BSD-3-Clause-Tso",
        name="BSD 3-Clause Tso variant",
        url=AnyUrl(
            "https://www.x.org/archive/current/doc/xorg-docs/License.html#Theodore_Tso"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-3-Clause-Tso.html": CreativeWork(
        identifier="BSD-3-Clause-Tso",
        name="BSD 3-Clause Tso variant",
        url=AnyUrl(
            "https://www.x.org/archive/current/doc/xorg-docs/License.html#Theodore_Tso"
        ),
    ),  # type: ignore
    "https://www.x.org/archive/current/doc/xorg-docs/License.html#Theodore_Tso": CreativeWork(
        identifier="BSD-3-Clause-Tso",
        name="BSD 3-Clause Tso variant",
        url=AnyUrl(
            "https://www.x.org/archive/current/doc/xorg-docs/License.html#Theodore_Tso"
        ),
    ),  # type: ignore
    "BSD-4-Clause": CreativeWork(
        identifier="BSD-4-Clause",
        name='BSD 4-Clause "Original" or "Old" License',
        url=AnyUrl("http://directory.fsf.org/wiki/License:BSD_4Clause"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4-Clause": CreativeWork(
        identifier="BSD-4-Clause",
        name='BSD 4-Clause "Original" or "Old" License',
        url=AnyUrl("http://directory.fsf.org/wiki/License:BSD_4Clause"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4-Clause.html": CreativeWork(
        identifier="BSD-4-Clause",
        name='BSD 4-Clause "Original" or "Old" License',
        url=AnyUrl("http://directory.fsf.org/wiki/License:BSD_4Clause"),
    ),  # type: ignore
    "http://directory.fsf.org/wiki/License:BSD_4Clause": CreativeWork(
        identifier="BSD-4-Clause",
        name='BSD 4-Clause "Original" or "Old" License',
        url=AnyUrl("http://directory.fsf.org/wiki/License:BSD_4Clause"),
    ),  # type: ignore
    "BSD-4-Clause-Shortened": CreativeWork(
        identifier="BSD-4-Clause-Shortened",
        name="BSD 4 Clause Shortened",
        url=AnyUrl(
            "https://metadata.ftp-master.debian.org/changelogs//main/a/arpwatch/arpwatch_2.1a15-7_copyright"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4-Clause-Shortened": CreativeWork(
        identifier="BSD-4-Clause-Shortened",
        name="BSD 4 Clause Shortened",
        url=AnyUrl(
            "https://metadata.ftp-master.debian.org/changelogs//main/a/arpwatch/arpwatch_2.1a15-7_copyright"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4-Clause-Shortened.html": CreativeWork(
        identifier="BSD-4-Clause-Shortened",
        name="BSD 4 Clause Shortened",
        url=AnyUrl(
            "https://metadata.ftp-master.debian.org/changelogs//main/a/arpwatch/arpwatch_2.1a15-7_copyright"
        ),
    ),  # type: ignore
    "https://metadata.ftp-master.debian.org/changelogs//main/a/arpwatch/arpwatch_2.1a15-7_copyright": CreativeWork(
        identifier="BSD-4-Clause-Shortened",
        name="BSD 4 Clause Shortened",
        url=AnyUrl(
            "https://metadata.ftp-master.debian.org/changelogs//main/a/arpwatch/arpwatch_2.1a15-7_copyright"
        ),
    ),  # type: ignore
    "BSD-4-Clause-UC": CreativeWork(
        identifier="BSD-4-Clause-UC",
        name="BSD-4-Clause (University of California-Specific)",
        url=AnyUrl("http://www.freebsd.org/copyright/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4-Clause-UC": CreativeWork(
        identifier="BSD-4-Clause-UC",
        name="BSD-4-Clause (University of California-Specific)",
        url=AnyUrl("http://www.freebsd.org/copyright/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4-Clause-UC.html": CreativeWork(
        identifier="BSD-4-Clause-UC",
        name="BSD-4-Clause (University of California-Specific)",
        url=AnyUrl("http://www.freebsd.org/copyright/license.html"),
    ),  # type: ignore
    "http://www.freebsd.org/copyright/license.html": CreativeWork(
        identifier="BSD-4-Clause-UC",
        name="BSD-4-Clause (University of California-Specific)",
        url=AnyUrl("http://www.freebsd.org/copyright/license.html"),
    ),  # type: ignore
    "BSD-4.3RENO": CreativeWork(
        identifier="BSD-4.3RENO",
        name="BSD 4.3 RENO License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=libiberty/strcasecmp.c;h=131d81c2ce7881fa48c363dc5bf5fb302c61ce0b;hb=HEAD"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4.3RENO": CreativeWork(
        identifier="BSD-4.3RENO",
        name="BSD 4.3 RENO License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=libiberty/strcasecmp.c;h=131d81c2ce7881fa48c363dc5bf5fb302c61ce0b;hb=HEAD"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4.3RENO.html": CreativeWork(
        identifier="BSD-4.3RENO",
        name="BSD 4.3 RENO License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=libiberty/strcasecmp.c;h=131d81c2ce7881fa48c363dc5bf5fb302c61ce0b;hb=HEAD"
        ),
    ),  # type: ignore
    "https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=libiberty/strcasecmp.c;h=131d81c2ce7881fa48c363dc5bf5fb302c61ce0b;hb=HEAD": CreativeWork(
        identifier="BSD-4.3RENO",
        name="BSD 4.3 RENO License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=libiberty/strcasecmp.c;h=131d81c2ce7881fa48c363dc5bf5fb302c61ce0b;hb=HEAD"
        ),
    ),  # type: ignore
    "BSD-4.3TAHOE": CreativeWork(
        identifier="BSD-4.3TAHOE",
        name="BSD 4.3 TAHOE License",
        url=AnyUrl(
            "https://github.com/389ds/389-ds-base/blob/main/ldap/include/sysexits-compat.h#L15"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4.3TAHOE": CreativeWork(
        identifier="BSD-4.3TAHOE",
        name="BSD 4.3 TAHOE License",
        url=AnyUrl(
            "https://github.com/389ds/389-ds-base/blob/main/ldap/include/sysexits-compat.h#L15"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-4.3TAHOE.html": CreativeWork(
        identifier="BSD-4.3TAHOE",
        name="BSD 4.3 TAHOE License",
        url=AnyUrl(
            "https://github.com/389ds/389-ds-base/blob/main/ldap/include/sysexits-compat.h#L15"
        ),
    ),  # type: ignore
    "https://github.com/389ds/389-ds-base/blob/main/ldap/include/sysexits-compat.h#L15": CreativeWork(
        identifier="BSD-4.3TAHOE",
        name="BSD 4.3 TAHOE License",
        url=AnyUrl(
            "https://github.com/389ds/389-ds-base/blob/main/ldap/include/sysexits-compat.h#L15"
        ),
    ),  # type: ignore
    "BSD-Advertising-Acknowledgement": CreativeWork(
        identifier="BSD-Advertising-Acknowledgement",
        name="BSD Advertising Acknowledgement License",
        url=AnyUrl("https://github.com/python-excel/xlrd/blob/master/LICENSE#L33"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Advertising-Acknowledgement": CreativeWork(
        identifier="BSD-Advertising-Acknowledgement",
        name="BSD Advertising Acknowledgement License",
        url=AnyUrl("https://github.com/python-excel/xlrd/blob/master/LICENSE#L33"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Advertising-Acknowledgement.html": CreativeWork(
        identifier="BSD-Advertising-Acknowledgement",
        name="BSD Advertising Acknowledgement License",
        url=AnyUrl("https://github.com/python-excel/xlrd/blob/master/LICENSE#L33"),
    ),  # type: ignore
    "https://github.com/python-excel/xlrd/blob/master/LICENSE#L33": CreativeWork(
        identifier="BSD-Advertising-Acknowledgement",
        name="BSD Advertising Acknowledgement License",
        url=AnyUrl("https://github.com/python-excel/xlrd/blob/master/LICENSE#L33"),
    ),  # type: ignore
    "BSD-Attribution-HPND-disclaimer": CreativeWork(
        identifier="BSD-Attribution-HPND-disclaimer",
        name="BSD with Attribution and HPND disclaimer",
        url=AnyUrl("https://github.com/cyrusimap/cyrus-sasl/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Attribution-HPND-disclaimer": CreativeWork(
        identifier="BSD-Attribution-HPND-disclaimer",
        name="BSD with Attribution and HPND disclaimer",
        url=AnyUrl("https://github.com/cyrusimap/cyrus-sasl/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Attribution-HPND-disclaimer.html": CreativeWork(
        identifier="BSD-Attribution-HPND-disclaimer",
        name="BSD with Attribution and HPND disclaimer",
        url=AnyUrl("https://github.com/cyrusimap/cyrus-sasl/blob/master/COPYING"),
    ),  # type: ignore
    "https://github.com/cyrusimap/cyrus-sasl/blob/master/COPYING": CreativeWork(
        identifier="BSD-Attribution-HPND-disclaimer",
        name="BSD with Attribution and HPND disclaimer",
        url=AnyUrl("https://github.com/cyrusimap/cyrus-sasl/blob/master/COPYING"),
    ),  # type: ignore
    "BSD-Inferno-Nettverk": CreativeWork(
        identifier="BSD-Inferno-Nettverk",
        name="BSD-Inferno-Nettverk",
        url=AnyUrl("https://www.inet.no/dante/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Inferno-Nettverk": CreativeWork(
        identifier="BSD-Inferno-Nettverk",
        name="BSD-Inferno-Nettverk",
        url=AnyUrl("https://www.inet.no/dante/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Inferno-Nettverk.html": CreativeWork(
        identifier="BSD-Inferno-Nettverk",
        name="BSD-Inferno-Nettverk",
        url=AnyUrl("https://www.inet.no/dante/LICENSE"),
    ),  # type: ignore
    "https://www.inet.no/dante/LICENSE": CreativeWork(
        identifier="BSD-Inferno-Nettverk",
        name="BSD-Inferno-Nettverk",
        url=AnyUrl("https://www.inet.no/dante/LICENSE"),
    ),  # type: ignore
    "BSD-Mark-Modifications": CreativeWork(
        identifier="BSD-Mark-Modifications",
        name="BSD Mark Modifications License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Mark-Modifications": CreativeWork(
        identifier="BSD-Mark-Modifications",
        name="BSD Mark Modifications License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Mark-Modifications.html": CreativeWork(
        identifier="BSD-Mark-Modifications",
        name="BSD Mark Modifications License",
        url=AnyUrl(
            "https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-2020.12.07-0.tar.bz2"
        ),
    ),  # type: ignore
    "BSD-Protection": CreativeWork(
        identifier="BSD-Protection",
        name="BSD Protection License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD_Protection_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Protection": CreativeWork(
        identifier="BSD-Protection",
        name="BSD Protection License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD_Protection_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Protection.html": CreativeWork(
        identifier="BSD-Protection",
        name="BSD Protection License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD_Protection_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/BSD_Protection_License": CreativeWork(
        identifier="BSD-Protection",
        name="BSD Protection License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/BSD_Protection_License"),
    ),  # type: ignore
    "BSD-Source-beginning-file": CreativeWork(
        identifier="BSD-Source-beginning-file",
        name="BSD Source Code Attribution - beginning of file variant",
        url=AnyUrl("https://github.com/lattera/freebsd/blob/master/sys/cam/cam.c#L4"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Source-beginning-file": CreativeWork(
        identifier="BSD-Source-beginning-file",
        name="BSD Source Code Attribution - beginning of file variant",
        url=AnyUrl("https://github.com/lattera/freebsd/blob/master/sys/cam/cam.c#L4"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Source-beginning-file.html": CreativeWork(
        identifier="BSD-Source-beginning-file",
        name="BSD Source Code Attribution - beginning of file variant",
        url=AnyUrl("https://github.com/lattera/freebsd/blob/master/sys/cam/cam.c#L4"),
    ),  # type: ignore
    "https://github.com/lattera/freebsd/blob/master/sys/cam/cam.c#L4": CreativeWork(
        identifier="BSD-Source-beginning-file",
        name="BSD Source Code Attribution - beginning of file variant",
        url=AnyUrl("https://github.com/lattera/freebsd/blob/master/sys/cam/cam.c#L4"),
    ),  # type: ignore
    "BSD-Source-Code": CreativeWork(
        identifier="BSD-Source-Code",
        name="BSD Source Code Attribution",
        url=AnyUrl(
            "https://github.com/robbiehanson/CocoaHTTPServer/blob/master/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Source-Code": CreativeWork(
        identifier="BSD-Source-Code",
        name="BSD Source Code Attribution",
        url=AnyUrl(
            "https://github.com/robbiehanson/CocoaHTTPServer/blob/master/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Source-Code.html": CreativeWork(
        identifier="BSD-Source-Code",
        name="BSD Source Code Attribution",
        url=AnyUrl(
            "https://github.com/robbiehanson/CocoaHTTPServer/blob/master/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://github.com/robbiehanson/CocoaHTTPServer/blob/master/LICENSE.txt": CreativeWork(
        identifier="BSD-Source-Code",
        name="BSD Source Code Attribution",
        url=AnyUrl(
            "https://github.com/robbiehanson/CocoaHTTPServer/blob/master/LICENSE.txt"
        ),
    ),  # type: ignore
    "BSD-Systemics": CreativeWork(
        identifier="BSD-Systemics",
        name="Systemics BSD variant license",
        url=AnyUrl(
            "https://metacpan.org/release/DPARIS/Crypt-DES-2.07/source/COPYRIGHT"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Systemics": CreativeWork(
        identifier="BSD-Systemics",
        name="Systemics BSD variant license",
        url=AnyUrl(
            "https://metacpan.org/release/DPARIS/Crypt-DES-2.07/source/COPYRIGHT"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Systemics.html": CreativeWork(
        identifier="BSD-Systemics",
        name="Systemics BSD variant license",
        url=AnyUrl(
            "https://metacpan.org/release/DPARIS/Crypt-DES-2.07/source/COPYRIGHT"
        ),
    ),  # type: ignore
    "https://metacpan.org/release/DPARIS/Crypt-DES-2.07/source/COPYRIGHT": CreativeWork(
        identifier="BSD-Systemics",
        name="Systemics BSD variant license",
        url=AnyUrl(
            "https://metacpan.org/release/DPARIS/Crypt-DES-2.07/source/COPYRIGHT"
        ),
    ),  # type: ignore
    "BSD-Systemics-W3Works": CreativeWork(
        identifier="BSD-Systemics-W3Works",
        name="Systemics W3Works BSD variant license",
        url=AnyUrl(
            "https://metacpan.org/release/DPARIS/Crypt-Blowfish-2.14/source/COPYRIGHT#L7"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Systemics-W3Works": CreativeWork(
        identifier="BSD-Systemics-W3Works",
        name="Systemics W3Works BSD variant license",
        url=AnyUrl(
            "https://metacpan.org/release/DPARIS/Crypt-Blowfish-2.14/source/COPYRIGHT#L7"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/BSD-Systemics-W3Works.html": CreativeWork(
        identifier="BSD-Systemics-W3Works",
        name="Systemics W3Works BSD variant license",
        url=AnyUrl(
            "https://metacpan.org/release/DPARIS/Crypt-Blowfish-2.14/source/COPYRIGHT#L7"
        ),
    ),  # type: ignore
    "https://metacpan.org/release/DPARIS/Crypt-Blowfish-2.14/source/COPYRIGHT#L7": CreativeWork(
        identifier="BSD-Systemics-W3Works",
        name="Systemics W3Works BSD variant license",
        url=AnyUrl(
            "https://metacpan.org/release/DPARIS/Crypt-Blowfish-2.14/source/COPYRIGHT#L7"
        ),
    ),  # type: ignore
    "BSL-1.0": CreativeWork(
        identifier="BSL-1.0",
        name="Boost Software License 1.0",
        url=AnyUrl("http://www.boost.org/LICENSE_1_0.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSL-1.0": CreativeWork(
        identifier="BSL-1.0",
        name="Boost Software License 1.0",
        url=AnyUrl("http://www.boost.org/LICENSE_1_0.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/BSL-1.0.html": CreativeWork(
        identifier="BSL-1.0",
        name="Boost Software License 1.0",
        url=AnyUrl("http://www.boost.org/LICENSE_1_0.txt"),
    ),  # type: ignore
    "http://www.boost.org/LICENSE_1_0.txt": CreativeWork(
        identifier="BSL-1.0",
        name="Boost Software License 1.0",
        url=AnyUrl("http://www.boost.org/LICENSE_1_0.txt"),
    ),  # type: ignore
    "Buddy": CreativeWork(
        identifier="Buddy",
        name="Buddy License",
        url=AnyUrl("https://sourceforge.net/p/buddy/gitcode/ci/master/tree/README"),
    ),  # type: ignore
    "https://spdx.org/licenses/Buddy": CreativeWork(
        identifier="Buddy",
        name="Buddy License",
        url=AnyUrl("https://sourceforge.net/p/buddy/gitcode/ci/master/tree/README"),
    ),  # type: ignore
    "https://spdx.org/licenses/Buddy.html": CreativeWork(
        identifier="Buddy",
        name="Buddy License",
        url=AnyUrl("https://sourceforge.net/p/buddy/gitcode/ci/master/tree/README"),
    ),  # type: ignore
    "https://sourceforge.net/p/buddy/gitcode/ci/master/tree/README": CreativeWork(
        identifier="Buddy",
        name="Buddy License",
        url=AnyUrl("https://sourceforge.net/p/buddy/gitcode/ci/master/tree/README"),
    ),  # type: ignore
    "BUSL-1.1": CreativeWork(
        identifier="BUSL-1.1",
        name="Business Source License 1.1",
        url=AnyUrl("https://mariadb.com/bsl11/"),
    ),  # type: ignore
    "https://spdx.org/licenses/BUSL-1.1": CreativeWork(
        identifier="BUSL-1.1",
        name="Business Source License 1.1",
        url=AnyUrl("https://mariadb.com/bsl11/"),
    ),  # type: ignore
    "https://spdx.org/licenses/BUSL-1.1.html": CreativeWork(
        identifier="BUSL-1.1",
        name="Business Source License 1.1",
        url=AnyUrl("https://mariadb.com/bsl11/"),
    ),  # type: ignore
    "https://mariadb.com/bsl11/": CreativeWork(
        identifier="BUSL-1.1",
        name="Business Source License 1.1",
        url=AnyUrl("https://mariadb.com/bsl11/"),
    ),  # type: ignore
    "bzip2-1.0.5": CreativeWork(
        identifier="bzip2-1.0.5",
        name="bzip2 and libbzip2 License v1.0.5",
        url=AnyUrl("https://sourceware.org/bzip2/1.0.5/bzip2-manual-1.0.5.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/bzip2-1.0.5": CreativeWork(
        identifier="bzip2-1.0.5",
        name="bzip2 and libbzip2 License v1.0.5",
        url=AnyUrl("https://sourceware.org/bzip2/1.0.5/bzip2-manual-1.0.5.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/bzip2-1.0.5.html": CreativeWork(
        identifier="bzip2-1.0.5",
        name="bzip2 and libbzip2 License v1.0.5",
        url=AnyUrl("https://sourceware.org/bzip2/1.0.5/bzip2-manual-1.0.5.html"),
    ),  # type: ignore
    "https://sourceware.org/bzip2/1.0.5/bzip2-manual-1.0.5.html": CreativeWork(
        identifier="bzip2-1.0.5",
        name="bzip2 and libbzip2 License v1.0.5",
        url=AnyUrl("https://sourceware.org/bzip2/1.0.5/bzip2-manual-1.0.5.html"),
    ),  # type: ignore
    "bzip2-1.0.6": CreativeWork(
        identifier="bzip2-1.0.6",
        name="bzip2 and libbzip2 License v1.0.6",
        url=AnyUrl(
            "https://sourceware.org/git/?p=bzip2.git;a=blob;f=LICENSE;hb=bzip2-1.0.6"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/bzip2-1.0.6": CreativeWork(
        identifier="bzip2-1.0.6",
        name="bzip2 and libbzip2 License v1.0.6",
        url=AnyUrl(
            "https://sourceware.org/git/?p=bzip2.git;a=blob;f=LICENSE;hb=bzip2-1.0.6"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/bzip2-1.0.6.html": CreativeWork(
        identifier="bzip2-1.0.6",
        name="bzip2 and libbzip2 License v1.0.6",
        url=AnyUrl(
            "https://sourceware.org/git/?p=bzip2.git;a=blob;f=LICENSE;hb=bzip2-1.0.6"
        ),
    ),  # type: ignore
    "https://sourceware.org/git/?p=bzip2.git;a=blob;f=LICENSE;hb=bzip2-1.0.6": CreativeWork(
        identifier="bzip2-1.0.6",
        name="bzip2 and libbzip2 License v1.0.6",
        url=AnyUrl(
            "https://sourceware.org/git/?p=bzip2.git;a=blob;f=LICENSE;hb=bzip2-1.0.6"
        ),
    ),  # type: ignore
    "C-UDA-1.0": CreativeWork(
        identifier="C-UDA-1.0",
        name="Computational Use of Data Agreement v1.0",
        url=AnyUrl(
            "https://github.com/microsoft/Computational-Use-of-Data-Agreement/blob/master/C-UDA-1.0.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/C-UDA-1.0": CreativeWork(
        identifier="C-UDA-1.0",
        name="Computational Use of Data Agreement v1.0",
        url=AnyUrl(
            "https://github.com/microsoft/Computational-Use-of-Data-Agreement/blob/master/C-UDA-1.0.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/C-UDA-1.0.html": CreativeWork(
        identifier="C-UDA-1.0",
        name="Computational Use of Data Agreement v1.0",
        url=AnyUrl(
            "https://github.com/microsoft/Computational-Use-of-Data-Agreement/blob/master/C-UDA-1.0.md"
        ),
    ),  # type: ignore
    "https://github.com/microsoft/Computational-Use-of-Data-Agreement/blob/master/C-UDA-1.0.md": CreativeWork(
        identifier="C-UDA-1.0",
        name="Computational Use of Data Agreement v1.0",
        url=AnyUrl(
            "https://github.com/microsoft/Computational-Use-of-Data-Agreement/blob/master/C-UDA-1.0.md"
        ),
    ),  # type: ignore
    "CAL-1.0": CreativeWork(
        identifier="CAL-1.0",
        name="Cryptographic Autonomy License 1.0",
        url=AnyUrl("http://cryptographicautonomylicense.com/license-text.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CAL-1.0": CreativeWork(
        identifier="CAL-1.0",
        name="Cryptographic Autonomy License 1.0",
        url=AnyUrl("http://cryptographicautonomylicense.com/license-text.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CAL-1.0.html": CreativeWork(
        identifier="CAL-1.0",
        name="Cryptographic Autonomy License 1.0",
        url=AnyUrl("http://cryptographicautonomylicense.com/license-text.html"),
    ),  # type: ignore
    "http://cryptographicautonomylicense.com/license-text.html": CreativeWork(
        identifier="CAL-1.0",
        name="Cryptographic Autonomy License 1.0",
        url=AnyUrl("http://cryptographicautonomylicense.com/license-text.html"),
    ),  # type: ignore
    "CAL-1.0-Combined-Work-Exception": CreativeWork(
        identifier="CAL-1.0-Combined-Work-Exception",
        name="Cryptographic Autonomy License 1.0 (Combined Work Exception)",
        url=AnyUrl("http://cryptographicautonomylicense.com/license-text.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CAL-1.0-Combined-Work-Exception": CreativeWork(
        identifier="CAL-1.0-Combined-Work-Exception",
        name="Cryptographic Autonomy License 1.0 (Combined Work Exception)",
        url=AnyUrl("http://cryptographicautonomylicense.com/license-text.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CAL-1.0-Combined-Work-Exception.html": CreativeWork(
        identifier="CAL-1.0-Combined-Work-Exception",
        name="Cryptographic Autonomy License 1.0 (Combined Work Exception)",
        url=AnyUrl("http://cryptographicautonomylicense.com/license-text.html"),
    ),  # type: ignore
    "Caldera": CreativeWork(
        identifier="Caldera",
        name="Caldera License",
        url=AnyUrl("http://www.lemis.com/grog/UNIX/ancient-source-all.pdf"),
    ),  # type: ignore
    "https://spdx.org/licenses/Caldera": CreativeWork(
        identifier="Caldera",
        name="Caldera License",
        url=AnyUrl("http://www.lemis.com/grog/UNIX/ancient-source-all.pdf"),
    ),  # type: ignore
    "https://spdx.org/licenses/Caldera.html": CreativeWork(
        identifier="Caldera",
        name="Caldera License",
        url=AnyUrl("http://www.lemis.com/grog/UNIX/ancient-source-all.pdf"),
    ),  # type: ignore
    "http://www.lemis.com/grog/UNIX/ancient-source-all.pdf": CreativeWork(
        identifier="Caldera",
        name="Caldera License",
        url=AnyUrl("http://www.lemis.com/grog/UNIX/ancient-source-all.pdf"),
    ),  # type: ignore
    "Caldera-no-preamble": CreativeWork(
        identifier="Caldera-no-preamble",
        name="Caldera License (without preamble)",
        url=AnyUrl("https://github.com/apache/apr/blob/trunk/LICENSE#L298C6-L298C29"),
    ),  # type: ignore
    "https://spdx.org/licenses/Caldera-no-preamble": CreativeWork(
        identifier="Caldera-no-preamble",
        name="Caldera License (without preamble)",
        url=AnyUrl("https://github.com/apache/apr/blob/trunk/LICENSE#L298C6-L298C29"),
    ),  # type: ignore
    "https://spdx.org/licenses/Caldera-no-preamble.html": CreativeWork(
        identifier="Caldera-no-preamble",
        name="Caldera License (without preamble)",
        url=AnyUrl("https://github.com/apache/apr/blob/trunk/LICENSE#L298C6-L298C29"),
    ),  # type: ignore
    "https://github.com/apache/apr/blob/trunk/LICENSE#L298C6-L298C29": CreativeWork(
        identifier="Caldera-no-preamble",
        name="Caldera License (without preamble)",
        url=AnyUrl("https://github.com/apache/apr/blob/trunk/LICENSE#L298C6-L298C29"),
    ),  # type: ignore
    "CAPEC-tou": CreativeWork(
        identifier="CAPEC-tou",
        name="Common Attack    Pattern Enumeration and Classification License",
        url=AnyUrl("https://capec.mitre.org/about/termsofuse.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CAPEC-tou": CreativeWork(
        identifier="CAPEC-tou",
        name="Common Attack    Pattern Enumeration and Classification License",
        url=AnyUrl("https://capec.mitre.org/about/termsofuse.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CAPEC-tou.html": CreativeWork(
        identifier="CAPEC-tou",
        name="Common Attack    Pattern Enumeration and Classification License",
        url=AnyUrl("https://capec.mitre.org/about/termsofuse.html"),
    ),  # type: ignore
    "https://capec.mitre.org/about/termsofuse.html": CreativeWork(
        identifier="CAPEC-tou",
        name="Common Attack    Pattern Enumeration and Classification License",
        url=AnyUrl("https://capec.mitre.org/about/termsofuse.html"),
    ),  # type: ignore
    "Catharon": CreativeWork(
        identifier="Catharon",
        name="Catharon License",
        url=AnyUrl(
            "https://github.com/scummvm/scummvm/blob/v2.8.0/LICENSES/CatharonLicense.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Catharon": CreativeWork(
        identifier="Catharon",
        name="Catharon License",
        url=AnyUrl(
            "https://github.com/scummvm/scummvm/blob/v2.8.0/LICENSES/CatharonLicense.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Catharon.html": CreativeWork(
        identifier="Catharon",
        name="Catharon License",
        url=AnyUrl(
            "https://github.com/scummvm/scummvm/blob/v2.8.0/LICENSES/CatharonLicense.txt"
        ),
    ),  # type: ignore
    "https://github.com/scummvm/scummvm/blob/v2.8.0/LICENSES/CatharonLicense.txt": CreativeWork(
        identifier="Catharon",
        name="Catharon License",
        url=AnyUrl(
            "https://github.com/scummvm/scummvm/blob/v2.8.0/LICENSES/CatharonLicense.txt"
        ),
    ),  # type: ignore
    "CATOSL-1.1": CreativeWork(
        identifier="CATOSL-1.1",
        name="Computer Associates Trusted Open Source License 1.1",
        url=AnyUrl("https://opensource.org/licenses/CATOSL-1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/CATOSL-1.1": CreativeWork(
        identifier="CATOSL-1.1",
        name="Computer Associates Trusted Open Source License 1.1",
        url=AnyUrl("https://opensource.org/licenses/CATOSL-1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/CATOSL-1.1.html": CreativeWork(
        identifier="CATOSL-1.1",
        name="Computer Associates Trusted Open Source License 1.1",
        url=AnyUrl("https://opensource.org/licenses/CATOSL-1.1"),
    ),  # type: ignore
    "https://opensource.org/licenses/CATOSL-1.1": CreativeWork(
        identifier="CATOSL-1.1",
        name="Computer Associates Trusted Open Source License 1.1",
        url=AnyUrl("https://opensource.org/licenses/CATOSL-1.1"),
    ),  # type: ignore
    "CC-BY-1.0": CreativeWork(
        identifier="CC-BY-1.0",
        name="Creative Commons Attribution 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-1.0": CreativeWork(
        identifier="CC-BY-1.0",
        name="Creative Commons Attribution 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-1.0.html": CreativeWork(
        identifier="CC-BY-1.0",
        name="Creative Commons Attribution 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/1.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/1.0/legalcode": CreativeWork(
        identifier="CC-BY-1.0",
        name="Creative Commons Attribution 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/1.0/legalcode"),
    ),  # type: ignore
    "CC-BY-2.0": CreativeWork(
        identifier="CC-BY-2.0",
        name="Creative Commons Attribution 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-2.0": CreativeWork(
        identifier="CC-BY-2.0",
        name="Creative Commons Attribution 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-2.0.html": CreativeWork(
        identifier="CC-BY-2.0",
        name="Creative Commons Attribution 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/2.0/legalcode": CreativeWork(
        identifier="CC-BY-2.0",
        name="Creative Commons Attribution 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.0/legalcode"),
    ),  # type: ignore
    "CC-BY-2.5": CreativeWork(
        identifier="CC-BY-2.5",
        name="Creative Commons Attribution 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-2.5": CreativeWork(
        identifier="CC-BY-2.5",
        name="Creative Commons Attribution 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-2.5.html": CreativeWork(
        identifier="CC-BY-2.5",
        name="Creative Commons Attribution 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.5/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/2.5/legalcode": CreativeWork(
        identifier="CC-BY-2.5",
        name="Creative Commons Attribution 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.5/legalcode"),
    ),  # type: ignore
    "CC-BY-2.5-AU": CreativeWork(
        identifier="CC-BY-2.5-AU",
        name="Creative Commons Attribution 2.5 Australia",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.5/au/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-2.5-AU": CreativeWork(
        identifier="CC-BY-2.5-AU",
        name="Creative Commons Attribution 2.5 Australia",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.5/au/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-2.5-AU.html": CreativeWork(
        identifier="CC-BY-2.5-AU",
        name="Creative Commons Attribution 2.5 Australia",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.5/au/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/2.5/au/legalcode": CreativeWork(
        identifier="CC-BY-2.5-AU",
        name="Creative Commons Attribution 2.5 Australia",
        url=AnyUrl("https://creativecommons.org/licenses/by/2.5/au/legalcode"),
    ),  # type: ignore
    "CC-BY-3.0": CreativeWork(
        identifier="CC-BY-3.0",
        name="Creative Commons Attribution 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0": CreativeWork(
        identifier="CC-BY-3.0",
        name="Creative Commons Attribution 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0.html": CreativeWork(
        identifier="CC-BY-3.0",
        name="Creative Commons Attribution 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/3.0/legalcode": CreativeWork(
        identifier="CC-BY-3.0",
        name="Creative Commons Attribution 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/legalcode"),
    ),  # type: ignore
    "CC-BY-3.0-AT": CreativeWork(
        identifier="CC-BY-3.0-AT",
        name="Creative Commons Attribution 3.0 Austria",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/at/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-AT": CreativeWork(
        identifier="CC-BY-3.0-AT",
        name="Creative Commons Attribution 3.0 Austria",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/at/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-AT.html": CreativeWork(
        identifier="CC-BY-3.0-AT",
        name="Creative Commons Attribution 3.0 Austria",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/at/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/3.0/at/legalcode": CreativeWork(
        identifier="CC-BY-3.0-AT",
        name="Creative Commons Attribution 3.0 Austria",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/at/legalcode"),
    ),  # type: ignore
    "CC-BY-3.0-AU": CreativeWork(
        identifier="CC-BY-3.0-AU",
        name="Creative Commons Attribution 3.0 Australia",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/au/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-AU": CreativeWork(
        identifier="CC-BY-3.0-AU",
        name="Creative Commons Attribution 3.0 Australia",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/au/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-AU.html": CreativeWork(
        identifier="CC-BY-3.0-AU",
        name="Creative Commons Attribution 3.0 Australia",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/au/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/3.0/au/legalcode": CreativeWork(
        identifier="CC-BY-3.0-AU",
        name="Creative Commons Attribution 3.0 Australia",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/au/legalcode"),
    ),  # type: ignore
    "CC-BY-3.0-DE": CreativeWork(
        identifier="CC-BY-3.0-DE",
        name="Creative Commons Attribution 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-DE": CreativeWork(
        identifier="CC-BY-3.0-DE",
        name="Creative Commons Attribution 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-DE.html": CreativeWork(
        identifier="CC-BY-3.0-DE",
        name="Creative Commons Attribution 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/de/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/3.0/de/legalcode": CreativeWork(
        identifier="CC-BY-3.0-DE",
        name="Creative Commons Attribution 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/de/legalcode"),
    ),  # type: ignore
    "CC-BY-3.0-IGO": CreativeWork(
        identifier="CC-BY-3.0-IGO",
        name="Creative Commons Attribution 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-IGO": CreativeWork(
        identifier="CC-BY-3.0-IGO",
        name="Creative Commons Attribution 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-IGO.html": CreativeWork(
        identifier="CC-BY-3.0-IGO",
        name="Creative Commons Attribution 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/3.0/igo/legalcode": CreativeWork(
        identifier="CC-BY-3.0-IGO",
        name="Creative Commons Attribution 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/igo/legalcode"),
    ),  # type: ignore
    "CC-BY-3.0-NL": CreativeWork(
        identifier="CC-BY-3.0-NL",
        name="Creative Commons Attribution 3.0 Netherlands",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/nl/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-NL": CreativeWork(
        identifier="CC-BY-3.0-NL",
        name="Creative Commons Attribution 3.0 Netherlands",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/nl/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-NL.html": CreativeWork(
        identifier="CC-BY-3.0-NL",
        name="Creative Commons Attribution 3.0 Netherlands",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/nl/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/3.0/nl/legalcode": CreativeWork(
        identifier="CC-BY-3.0-NL",
        name="Creative Commons Attribution 3.0 Netherlands",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/nl/legalcode"),
    ),  # type: ignore
    "CC-BY-3.0-US": CreativeWork(
        identifier="CC-BY-3.0-US",
        name="Creative Commons Attribution 3.0 United States",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/us/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-US": CreativeWork(
        identifier="CC-BY-3.0-US",
        name="Creative Commons Attribution 3.0 United States",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/us/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-3.0-US.html": CreativeWork(
        identifier="CC-BY-3.0-US",
        name="Creative Commons Attribution 3.0 United States",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/us/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/3.0/us/legalcode": CreativeWork(
        identifier="CC-BY-3.0-US",
        name="Creative Commons Attribution 3.0 United States",
        url=AnyUrl("https://creativecommons.org/licenses/by/3.0/us/legalcode"),
    ),  # type: ignore
    "CC-BY-4.0": CreativeWork(
        identifier="CC-BY-4.0",
        name="Creative Commons Attribution 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-4.0": CreativeWork(
        identifier="CC-BY-4.0",
        name="Creative Commons Attribution 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-4.0.html": CreativeWork(
        identifier="CC-BY-4.0",
        name="Creative Commons Attribution 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by/4.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by/4.0/legalcode": CreativeWork(
        identifier="CC-BY-4.0",
        name="Creative Commons Attribution 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by/4.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-1.0": CreativeWork(
        identifier="CC-BY-NC-1.0",
        name="Creative Commons Attribution Non Commercial 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-1.0": CreativeWork(
        identifier="CC-BY-NC-1.0",
        name="Creative Commons Attribution Non Commercial 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-1.0.html": CreativeWork(
        identifier="CC-BY-NC-1.0",
        name="Creative Commons Attribution Non Commercial 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/1.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc/1.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-1.0",
        name="Creative Commons Attribution Non Commercial 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/1.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-2.0": CreativeWork(
        identifier="CC-BY-NC-2.0",
        name="Creative Commons Attribution Non Commercial 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-2.0": CreativeWork(
        identifier="CC-BY-NC-2.0",
        name="Creative Commons Attribution Non Commercial 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-2.0.html": CreativeWork(
        identifier="CC-BY-NC-2.0",
        name="Creative Commons Attribution Non Commercial 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/2.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc/2.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-2.0",
        name="Creative Commons Attribution Non Commercial 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/2.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-2.5": CreativeWork(
        identifier="CC-BY-NC-2.5",
        name="Creative Commons Attribution Non Commercial 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-2.5": CreativeWork(
        identifier="CC-BY-NC-2.5",
        name="Creative Commons Attribution Non Commercial 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-2.5.html": CreativeWork(
        identifier="CC-BY-NC-2.5",
        name="Creative Commons Attribution Non Commercial 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/2.5/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc/2.5/legalcode": CreativeWork(
        identifier="CC-BY-NC-2.5",
        name="Creative Commons Attribution Non Commercial 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/2.5/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-3.0": CreativeWork(
        identifier="CC-BY-NC-3.0",
        name="Creative Commons Attribution Non Commercial 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-3.0": CreativeWork(
        identifier="CC-BY-NC-3.0",
        name="Creative Commons Attribution Non Commercial 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-3.0.html": CreativeWork(
        identifier="CC-BY-NC-3.0",
        name="Creative Commons Attribution Non Commercial 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/3.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc/3.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-3.0",
        name="Creative Commons Attribution Non Commercial 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/3.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-3.0-DE": CreativeWork(
        identifier="CC-BY-NC-3.0-DE",
        name="Creative Commons Attribution Non Commercial 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-3.0-DE": CreativeWork(
        identifier="CC-BY-NC-3.0-DE",
        name="Creative Commons Attribution Non Commercial 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-3.0-DE.html": CreativeWork(
        identifier="CC-BY-NC-3.0-DE",
        name="Creative Commons Attribution Non Commercial 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/3.0/de/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc/3.0/de/legalcode": CreativeWork(
        identifier="CC-BY-NC-3.0-DE",
        name="Creative Commons Attribution Non Commercial 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/3.0/de/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-4.0": CreativeWork(
        identifier="CC-BY-NC-4.0",
        name="Creative Commons Attribution Non Commercial 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-4.0": CreativeWork(
        identifier="CC-BY-NC-4.0",
        name="Creative Commons Attribution Non Commercial 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-4.0.html": CreativeWork(
        identifier="CC-BY-NC-4.0",
        name="Creative Commons Attribution Non Commercial 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/4.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc/4.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-4.0",
        name="Creative Commons Attribution Non Commercial 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc/4.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-ND-1.0": CreativeWork(
        identifier="CC-BY-NC-ND-1.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd-nc/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-1.0": CreativeWork(
        identifier="CC-BY-NC-ND-1.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd-nc/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-1.0.html": CreativeWork(
        identifier="CC-BY-NC-ND-1.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd-nc/1.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nd-nc/1.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-ND-1.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd-nc/1.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-ND-2.0": CreativeWork(
        identifier="CC-BY-NC-ND-2.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-2.0": CreativeWork(
        identifier="CC-BY-NC-ND-2.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-2.0.html": CreativeWork(
        identifier="CC-BY-NC-ND-2.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/2.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-nd/2.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-ND-2.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/2.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-ND-2.5": CreativeWork(
        identifier="CC-BY-NC-ND-2.5",
        name="Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-2.5": CreativeWork(
        identifier="CC-BY-NC-ND-2.5",
        name="Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-2.5.html": CreativeWork(
        identifier="CC-BY-NC-ND-2.5",
        name="Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/2.5/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-nd/2.5/legalcode": CreativeWork(
        identifier="CC-BY-NC-ND-2.5",
        name="Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/2.5/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-ND-3.0": CreativeWork(
        identifier="CC-BY-NC-ND-3.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-3.0": CreativeWork(
        identifier="CC-BY-NC-ND-3.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-3.0.html": CreativeWork(
        identifier="CC-BY-NC-ND-3.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-ND-3.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-ND-3.0-DE": CreativeWork(
        identifier="CC-BY-NC-ND-3.0-DE",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-3.0-DE": CreativeWork(
        identifier="CC-BY-NC-ND-3.0-DE",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-3.0-DE.html": CreativeWork(
        identifier="CC-BY-NC-ND-3.0-DE",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/de/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-nd/3.0/de/legalcode": CreativeWork(
        identifier="CC-BY-NC-ND-3.0-DE",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/de/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-ND-3.0-IGO": CreativeWork(
        identifier="CC-BY-NC-ND-3.0-IGO",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-3.0-IGO": CreativeWork(
        identifier="CC-BY-NC-ND-3.0-IGO",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-3.0-IGO.html": CreativeWork(
        identifier="CC-BY-NC-ND-3.0-IGO",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-nd/3.0/igo/legalcode": CreativeWork(
        identifier="CC-BY-NC-ND-3.0-IGO",
        name="Creative Commons Attribution Non Commercial No Derivatives 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/3.0/igo/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-ND-4.0": CreativeWork(
        identifier="CC-BY-NC-ND-4.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-4.0": CreativeWork(
        identifier="CC-BY-NC-ND-4.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-ND-4.0.html": CreativeWork(
        identifier="CC-BY-NC-ND-4.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-ND-4.0",
        name="Creative Commons Attribution Non Commercial No Derivatives 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-1.0": CreativeWork(
        identifier="CC-BY-NC-SA-1.0",
        name="Creative Commons Attribution Non Commercial Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-1.0": CreativeWork(
        identifier="CC-BY-NC-SA-1.0",
        name="Creative Commons Attribution Non Commercial Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-1.0.html": CreativeWork(
        identifier="CC-BY-NC-SA-1.0",
        name="Creative Commons Attribution Non Commercial Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/1.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/1.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-1.0",
        name="Creative Commons Attribution Non Commercial Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/1.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-2.0": CreativeWork(
        identifier="CC-BY-NC-SA-2.0",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.0": CreativeWork(
        identifier="CC-BY-NC-SA-2.0",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.0.html": CreativeWork(
        identifier="CC-BY-NC-SA-2.0",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/2.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-2.0",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-2.0-DE": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-DE",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.0-DE": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-DE",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.0-DE.html": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-DE",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/de/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/2.0/de/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-DE",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/de/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-2.0-FR": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-FR",
        name="Creative Commons Attribution-NonCommercial-ShareAlike 2.0 France",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/fr/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.0-FR": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-FR",
        name="Creative Commons Attribution-NonCommercial-ShareAlike 2.0 France",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/fr/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.0-FR.html": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-FR",
        name="Creative Commons Attribution-NonCommercial-ShareAlike 2.0 France",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/fr/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/2.0/fr/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-FR",
        name="Creative Commons Attribution-NonCommercial-ShareAlike 2.0 France",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/fr/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-2.0-UK": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-UK",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 England and Wales",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/uk/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.0-UK": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-UK",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 England and Wales",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/uk/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.0-UK.html": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-UK",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 England and Wales",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/uk/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/2.0/uk/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-2.0-UK",
        name="Creative Commons Attribution Non Commercial Share Alike 2.0 England and Wales",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.0/uk/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-2.5": CreativeWork(
        identifier="CC-BY-NC-SA-2.5",
        name="Creative Commons Attribution Non Commercial Share Alike 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.5": CreativeWork(
        identifier="CC-BY-NC-SA-2.5",
        name="Creative Commons Attribution Non Commercial Share Alike 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-2.5.html": CreativeWork(
        identifier="CC-BY-NC-SA-2.5",
        name="Creative Commons Attribution Non Commercial Share Alike 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.5/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/2.5/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-2.5",
        name="Creative Commons Attribution Non Commercial Share Alike 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/2.5/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-3.0": CreativeWork(
        identifier="CC-BY-NC-SA-3.0",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-3.0": CreativeWork(
        identifier="CC-BY-NC-SA-3.0",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-3.0.html": CreativeWork(
        identifier="CC-BY-NC-SA-3.0",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-3.0",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-3.0-DE": CreativeWork(
        identifier="CC-BY-NC-SA-3.0-DE",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-3.0-DE": CreativeWork(
        identifier="CC-BY-NC-SA-3.0-DE",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-3.0-DE.html": CreativeWork(
        identifier="CC-BY-NC-SA-3.0-DE",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/de/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/3.0/de/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-3.0-DE",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/de/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-3.0-IGO": CreativeWork(
        identifier="CC-BY-NC-SA-3.0-IGO",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-3.0-IGO": CreativeWork(
        identifier="CC-BY-NC-SA-3.0-IGO",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-3.0-IGO.html": CreativeWork(
        identifier="CC-BY-NC-SA-3.0-IGO",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/3.0/igo/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-3.0-IGO",
        name="Creative Commons Attribution Non Commercial Share Alike 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/3.0/igo/legalcode"),
    ),  # type: ignore
    "CC-BY-NC-SA-4.0": CreativeWork(
        identifier="CC-BY-NC-SA-4.0",
        name="Creative Commons Attribution Non Commercial Share Alike 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-4.0": CreativeWork(
        identifier="CC-BY-NC-SA-4.0",
        name="Creative Commons Attribution Non Commercial Share Alike 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-NC-SA-4.0.html": CreativeWork(
        identifier="CC-BY-NC-SA-4.0",
        name="Creative Commons Attribution Non Commercial Share Alike 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode": CreativeWork(
        identifier="CC-BY-NC-SA-4.0",
        name="Creative Commons Attribution Non Commercial Share Alike 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode"),
    ),  # type: ignore
    "CC-BY-ND-1.0": CreativeWork(
        identifier="CC-BY-ND-1.0",
        name="Creative Commons Attribution No Derivatives 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-1.0": CreativeWork(
        identifier="CC-BY-ND-1.0",
        name="Creative Commons Attribution No Derivatives 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-1.0.html": CreativeWork(
        identifier="CC-BY-ND-1.0",
        name="Creative Commons Attribution No Derivatives 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/1.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nd/1.0/legalcode": CreativeWork(
        identifier="CC-BY-ND-1.0",
        name="Creative Commons Attribution No Derivatives 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/1.0/legalcode"),
    ),  # type: ignore
    "CC-BY-ND-2.0": CreativeWork(
        identifier="CC-BY-ND-2.0",
        name="Creative Commons Attribution No Derivatives 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-2.0": CreativeWork(
        identifier="CC-BY-ND-2.0",
        name="Creative Commons Attribution No Derivatives 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-2.0.html": CreativeWork(
        identifier="CC-BY-ND-2.0",
        name="Creative Commons Attribution No Derivatives 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/2.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nd/2.0/legalcode": CreativeWork(
        identifier="CC-BY-ND-2.0",
        name="Creative Commons Attribution No Derivatives 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/2.0/legalcode"),
    ),  # type: ignore
    "CC-BY-ND-2.5": CreativeWork(
        identifier="CC-BY-ND-2.5",
        name="Creative Commons Attribution No Derivatives 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-2.5": CreativeWork(
        identifier="CC-BY-ND-2.5",
        name="Creative Commons Attribution No Derivatives 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-2.5.html": CreativeWork(
        identifier="CC-BY-ND-2.5",
        name="Creative Commons Attribution No Derivatives 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/2.5/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nd/2.5/legalcode": CreativeWork(
        identifier="CC-BY-ND-2.5",
        name="Creative Commons Attribution No Derivatives 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/2.5/legalcode"),
    ),  # type: ignore
    "CC-BY-ND-3.0": CreativeWork(
        identifier="CC-BY-ND-3.0",
        name="Creative Commons Attribution No Derivatives 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-3.0": CreativeWork(
        identifier="CC-BY-ND-3.0",
        name="Creative Commons Attribution No Derivatives 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-3.0.html": CreativeWork(
        identifier="CC-BY-ND-3.0",
        name="Creative Commons Attribution No Derivatives 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/3.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nd/3.0/legalcode": CreativeWork(
        identifier="CC-BY-ND-3.0",
        name="Creative Commons Attribution No Derivatives 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/3.0/legalcode"),
    ),  # type: ignore
    "CC-BY-ND-3.0-DE": CreativeWork(
        identifier="CC-BY-ND-3.0-DE",
        name="Creative Commons Attribution No Derivatives 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-3.0-DE": CreativeWork(
        identifier="CC-BY-ND-3.0-DE",
        name="Creative Commons Attribution No Derivatives 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-3.0-DE.html": CreativeWork(
        identifier="CC-BY-ND-3.0-DE",
        name="Creative Commons Attribution No Derivatives 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/3.0/de/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nd/3.0/de/legalcode": CreativeWork(
        identifier="CC-BY-ND-3.0-DE",
        name="Creative Commons Attribution No Derivatives 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/3.0/de/legalcode"),
    ),  # type: ignore
    "CC-BY-ND-4.0": CreativeWork(
        identifier="CC-BY-ND-4.0",
        name="Creative Commons Attribution No Derivatives 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-4.0": CreativeWork(
        identifier="CC-BY-ND-4.0",
        name="Creative Commons Attribution No Derivatives 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-ND-4.0.html": CreativeWork(
        identifier="CC-BY-ND-4.0",
        name="Creative Commons Attribution No Derivatives 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/4.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-nd/4.0/legalcode": CreativeWork(
        identifier="CC-BY-ND-4.0",
        name="Creative Commons Attribution No Derivatives 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-nd/4.0/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-1.0": CreativeWork(
        identifier="CC-BY-SA-1.0",
        name="Creative Commons Attribution Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-1.0": CreativeWork(
        identifier="CC-BY-SA-1.0",
        name="Creative Commons Attribution Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-1.0.html": CreativeWork(
        identifier="CC-BY-SA-1.0",
        name="Creative Commons Attribution Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/1.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/1.0/legalcode": CreativeWork(
        identifier="CC-BY-SA-1.0",
        name="Creative Commons Attribution Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/1.0/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-2.0": CreativeWork(
        identifier="CC-BY-SA-2.0",
        name="Creative Commons Attribution Share Alike 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-2.0": CreativeWork(
        identifier="CC-BY-SA-2.0",
        name="Creative Commons Attribution Share Alike 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-2.0.html": CreativeWork(
        identifier="CC-BY-SA-2.0",
        name="Creative Commons Attribution Share Alike 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/2.0/legalcode": CreativeWork(
        identifier="CC-BY-SA-2.0",
        name="Creative Commons Attribution Share Alike 2.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.0/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-2.0-UK": CreativeWork(
        identifier="CC-BY-SA-2.0-UK",
        name="Creative Commons Attribution Share Alike 2.0 England and Wales",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.0/uk/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-2.0-UK": CreativeWork(
        identifier="CC-BY-SA-2.0-UK",
        name="Creative Commons Attribution Share Alike 2.0 England and Wales",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.0/uk/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-2.0-UK.html": CreativeWork(
        identifier="CC-BY-SA-2.0-UK",
        name="Creative Commons Attribution Share Alike 2.0 England and Wales",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.0/uk/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/2.0/uk/legalcode": CreativeWork(
        identifier="CC-BY-SA-2.0-UK",
        name="Creative Commons Attribution Share Alike 2.0 England and Wales",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.0/uk/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-2.1-JP": CreativeWork(
        identifier="CC-BY-SA-2.1-JP",
        name="Creative Commons Attribution Share Alike 2.1 Japan",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.1/jp/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-2.1-JP": CreativeWork(
        identifier="CC-BY-SA-2.1-JP",
        name="Creative Commons Attribution Share Alike 2.1 Japan",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.1/jp/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-2.1-JP.html": CreativeWork(
        identifier="CC-BY-SA-2.1-JP",
        name="Creative Commons Attribution Share Alike 2.1 Japan",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.1/jp/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/2.1/jp/legalcode": CreativeWork(
        identifier="CC-BY-SA-2.1-JP",
        name="Creative Commons Attribution Share Alike 2.1 Japan",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.1/jp/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-2.5": CreativeWork(
        identifier="CC-BY-SA-2.5",
        name="Creative Commons Attribution Share Alike 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-2.5": CreativeWork(
        identifier="CC-BY-SA-2.5",
        name="Creative Commons Attribution Share Alike 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.5/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-2.5.html": CreativeWork(
        identifier="CC-BY-SA-2.5",
        name="Creative Commons Attribution Share Alike 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.5/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/2.5/legalcode": CreativeWork(
        identifier="CC-BY-SA-2.5",
        name="Creative Commons Attribution Share Alike 2.5 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/2.5/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-3.0": CreativeWork(
        identifier="CC-BY-SA-3.0",
        name="Creative Commons Attribution Share Alike 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-3.0": CreativeWork(
        identifier="CC-BY-SA-3.0",
        name="Creative Commons Attribution Share Alike 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-3.0.html": CreativeWork(
        identifier="CC-BY-SA-3.0",
        name="Creative Commons Attribution Share Alike 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/3.0/legalcode": CreativeWork(
        identifier="CC-BY-SA-3.0",
        name="Creative Commons Attribution Share Alike 3.0 Unported",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-3.0-AT": CreativeWork(
        identifier="CC-BY-SA-3.0-AT",
        name="Creative Commons Attribution Share Alike 3.0 Austria",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/at/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-3.0-AT": CreativeWork(
        identifier="CC-BY-SA-3.0-AT",
        name="Creative Commons Attribution Share Alike 3.0 Austria",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/at/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-3.0-AT.html": CreativeWork(
        identifier="CC-BY-SA-3.0-AT",
        name="Creative Commons Attribution Share Alike 3.0 Austria",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/at/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/3.0/at/legalcode": CreativeWork(
        identifier="CC-BY-SA-3.0-AT",
        name="Creative Commons Attribution Share Alike 3.0 Austria",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/at/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-3.0-DE": CreativeWork(
        identifier="CC-BY-SA-3.0-DE",
        name="Creative Commons Attribution Share Alike 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-3.0-DE": CreativeWork(
        identifier="CC-BY-SA-3.0-DE",
        name="Creative Commons Attribution Share Alike 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/de/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-3.0-DE.html": CreativeWork(
        identifier="CC-BY-SA-3.0-DE",
        name="Creative Commons Attribution Share Alike 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/de/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/3.0/de/legalcode": CreativeWork(
        identifier="CC-BY-SA-3.0-DE",
        name="Creative Commons Attribution Share Alike 3.0 Germany",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/de/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-3.0-IGO": CreativeWork(
        identifier="CC-BY-SA-3.0-IGO",
        name="Creative Commons Attribution-ShareAlike 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-3.0-IGO": CreativeWork(
        identifier="CC-BY-SA-3.0-IGO",
        name="Creative Commons Attribution-ShareAlike 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-3.0-IGO.html": CreativeWork(
        identifier="CC-BY-SA-3.0-IGO",
        name="Creative Commons Attribution-ShareAlike 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/igo/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/3.0/igo/legalcode": CreativeWork(
        identifier="CC-BY-SA-3.0-IGO",
        name="Creative Commons Attribution-ShareAlike 3.0 IGO",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/3.0/igo/legalcode"),
    ),  # type: ignore
    "CC-BY-SA-4.0": CreativeWork(
        identifier="CC-BY-SA-4.0",
        name="Creative Commons Attribution Share Alike 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-4.0": CreativeWork(
        identifier="CC-BY-SA-4.0",
        name="Creative Commons Attribution Share Alike 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/4.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-BY-SA-4.0.html": CreativeWork(
        identifier="CC-BY-SA-4.0",
        name="Creative Commons Attribution Share Alike 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/4.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/by-sa/4.0/legalcode": CreativeWork(
        identifier="CC-BY-SA-4.0",
        name="Creative Commons Attribution Share Alike 4.0 International",
        url=AnyUrl("https://creativecommons.org/licenses/by-sa/4.0/legalcode"),
    ),  # type: ignore
    "CC-PDDC": CreativeWork(
        identifier="CC-PDDC",
        name="Creative Commons Public Domain Dedication and Certification",
        url=AnyUrl("https://creativecommons.org/licenses/publicdomain/"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-PDDC": CreativeWork(
        identifier="CC-PDDC",
        name="Creative Commons Public Domain Dedication and Certification",
        url=AnyUrl("https://creativecommons.org/licenses/publicdomain/"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-PDDC.html": CreativeWork(
        identifier="CC-PDDC",
        name="Creative Commons Public Domain Dedication and Certification",
        url=AnyUrl("https://creativecommons.org/licenses/publicdomain/"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/publicdomain/": CreativeWork(
        identifier="CC-PDDC",
        name="Creative Commons Public Domain Dedication and Certification",
        url=AnyUrl("https://creativecommons.org/licenses/publicdomain/"),
    ),  # type: ignore
    "CC-PDM-1.0": CreativeWork(
        identifier="CC-PDM-1.0",
        name="Creative    Commons Public Domain Mark 1.0 Universal",
        url=AnyUrl("https://creativecommons.org/publicdomain/mark/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-PDM-1.0": CreativeWork(
        identifier="CC-PDM-1.0",
        name="Creative    Commons Public Domain Mark 1.0 Universal",
        url=AnyUrl("https://creativecommons.org/publicdomain/mark/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-PDM-1.0.html": CreativeWork(
        identifier="CC-PDM-1.0",
        name="Creative    Commons Public Domain Mark 1.0 Universal",
        url=AnyUrl("https://creativecommons.org/publicdomain/mark/1.0/"),
    ),  # type: ignore
    "https://creativecommons.org/publicdomain/mark/1.0/": CreativeWork(
        identifier="CC-PDM-1.0",
        name="Creative    Commons Public Domain Mark 1.0 Universal",
        url=AnyUrl("https://creativecommons.org/publicdomain/mark/1.0/"),
    ),  # type: ignore
    "CC-SA-1.0": CreativeWork(
        identifier="CC-SA-1.0",
        name="Creative Commons Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/sa/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-SA-1.0": CreativeWork(
        identifier="CC-SA-1.0",
        name="Creative Commons Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/sa/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC-SA-1.0.html": CreativeWork(
        identifier="CC-SA-1.0",
        name="Creative Commons Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/sa/1.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/licenses/sa/1.0/legalcode": CreativeWork(
        identifier="CC-SA-1.0",
        name="Creative Commons Share Alike 1.0 Generic",
        url=AnyUrl("https://creativecommons.org/licenses/sa/1.0/legalcode"),
    ),  # type: ignore
    "CC0-1.0": CreativeWork(
        identifier="CC0-1.0",
        name="Creative Commons Zero v1.0 Universal",
        url=AnyUrl("https://creativecommons.org/publicdomain/zero/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC0-1.0": CreativeWork(
        identifier="CC0-1.0",
        name="Creative Commons Zero v1.0 Universal",
        url=AnyUrl("https://creativecommons.org/publicdomain/zero/1.0/legalcode"),
    ),  # type: ignore
    "https://spdx.org/licenses/CC0-1.0.html": CreativeWork(
        identifier="CC0-1.0",
        name="Creative Commons Zero v1.0 Universal",
        url=AnyUrl("https://creativecommons.org/publicdomain/zero/1.0/legalcode"),
    ),  # type: ignore
    "https://creativecommons.org/publicdomain/zero/1.0/legalcode": CreativeWork(
        identifier="CC0-1.0",
        name="Creative Commons Zero v1.0 Universal",
        url=AnyUrl("https://creativecommons.org/publicdomain/zero/1.0/legalcode"),
    ),  # type: ignore
    "CDDL-1.0": CreativeWork(
        identifier="CDDL-1.0",
        name="Common Development and Distribution License 1.0",
        url=AnyUrl("https://opensource.org/licenses/cddl1"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDDL-1.0": CreativeWork(
        identifier="CDDL-1.0",
        name="Common Development and Distribution License 1.0",
        url=AnyUrl("https://opensource.org/licenses/cddl1"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDDL-1.0.html": CreativeWork(
        identifier="CDDL-1.0",
        name="Common Development and Distribution License 1.0",
        url=AnyUrl("https://opensource.org/licenses/cddl1"),
    ),  # type: ignore
    "https://opensource.org/licenses/cddl1": CreativeWork(
        identifier="CDDL-1.0",
        name="Common Development and Distribution License 1.0",
        url=AnyUrl("https://opensource.org/licenses/cddl1"),
    ),  # type: ignore
    "CDDL-1.1": CreativeWork(
        identifier="CDDL-1.1",
        name="Common Development and Distribution License 1.1",
        url=AnyUrl("http://glassfish.java.net/public/CDDL+GPL_1_1.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDDL-1.1": CreativeWork(
        identifier="CDDL-1.1",
        name="Common Development and Distribution License 1.1",
        url=AnyUrl("http://glassfish.java.net/public/CDDL+GPL_1_1.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDDL-1.1.html": CreativeWork(
        identifier="CDDL-1.1",
        name="Common Development and Distribution License 1.1",
        url=AnyUrl("http://glassfish.java.net/public/CDDL+GPL_1_1.html"),
    ),  # type: ignore
    "http://glassfish.java.net/public/CDDL+GPL_1_1.html": CreativeWork(
        identifier="CDDL-1.1",
        name="Common Development and Distribution License 1.1",
        url=AnyUrl("http://glassfish.java.net/public/CDDL+GPL_1_1.html"),
    ),  # type: ignore
    "CDL-1.0": CreativeWork(
        identifier="CDL-1.0",
        name="Common Documentation License 1.0",
        url=AnyUrl("http://www.opensource.apple.com/cdl/"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDL-1.0": CreativeWork(
        identifier="CDL-1.0",
        name="Common Documentation License 1.0",
        url=AnyUrl("http://www.opensource.apple.com/cdl/"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDL-1.0.html": CreativeWork(
        identifier="CDL-1.0",
        name="Common Documentation License 1.0",
        url=AnyUrl("http://www.opensource.apple.com/cdl/"),
    ),  # type: ignore
    "http://www.opensource.apple.com/cdl/": CreativeWork(
        identifier="CDL-1.0",
        name="Common Documentation License 1.0",
        url=AnyUrl("http://www.opensource.apple.com/cdl/"),
    ),  # type: ignore
    "CDLA-Permissive-1.0": CreativeWork(
        identifier="CDLA-Permissive-1.0",
        name="Community Data License Agreement Permissive 1.0",
        url=AnyUrl("https://cdla.io/permissive-1-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDLA-Permissive-1.0": CreativeWork(
        identifier="CDLA-Permissive-1.0",
        name="Community Data License Agreement Permissive 1.0",
        url=AnyUrl("https://cdla.io/permissive-1-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDLA-Permissive-1.0.html": CreativeWork(
        identifier="CDLA-Permissive-1.0",
        name="Community Data License Agreement Permissive 1.0",
        url=AnyUrl("https://cdla.io/permissive-1-0"),
    ),  # type: ignore
    "https://cdla.io/permissive-1-0": CreativeWork(
        identifier="CDLA-Permissive-1.0",
        name="Community Data License Agreement Permissive 1.0",
        url=AnyUrl("https://cdla.io/permissive-1-0"),
    ),  # type: ignore
    "CDLA-Permissive-2.0": CreativeWork(
        identifier="CDLA-Permissive-2.0",
        name="Community Data License Agreement Permissive 2.0",
        url=AnyUrl("https://cdla.dev/permissive-2-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDLA-Permissive-2.0": CreativeWork(
        identifier="CDLA-Permissive-2.0",
        name="Community Data License Agreement Permissive 2.0",
        url=AnyUrl("https://cdla.dev/permissive-2-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDLA-Permissive-2.0.html": CreativeWork(
        identifier="CDLA-Permissive-2.0",
        name="Community Data License Agreement Permissive 2.0",
        url=AnyUrl("https://cdla.dev/permissive-2-0"),
    ),  # type: ignore
    "https://cdla.dev/permissive-2-0": CreativeWork(
        identifier="CDLA-Permissive-2.0",
        name="Community Data License Agreement Permissive 2.0",
        url=AnyUrl("https://cdla.dev/permissive-2-0"),
    ),  # type: ignore
    "CDLA-Sharing-1.0": CreativeWork(
        identifier="CDLA-Sharing-1.0",
        name="Community Data License Agreement Sharing 1.0",
        url=AnyUrl("https://cdla.io/sharing-1-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDLA-Sharing-1.0": CreativeWork(
        identifier="CDLA-Sharing-1.0",
        name="Community Data License Agreement Sharing 1.0",
        url=AnyUrl("https://cdla.io/sharing-1-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CDLA-Sharing-1.0.html": CreativeWork(
        identifier="CDLA-Sharing-1.0",
        name="Community Data License Agreement Sharing 1.0",
        url=AnyUrl("https://cdla.io/sharing-1-0"),
    ),  # type: ignore
    "https://cdla.io/sharing-1-0": CreativeWork(
        identifier="CDLA-Sharing-1.0",
        name="Community Data License Agreement Sharing 1.0",
        url=AnyUrl("https://cdla.io/sharing-1-0"),
    ),  # type: ignore
    "CECILL-1.0": CreativeWork(
        identifier="CECILL-1.0",
        name="CeCILL Free Software License Agreement v1.0",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V1-fr.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-1.0": CreativeWork(
        identifier="CECILL-1.0",
        name="CeCILL Free Software License Agreement v1.0",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V1-fr.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-1.0.html": CreativeWork(
        identifier="CECILL-1.0",
        name="CeCILL Free Software License Agreement v1.0",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V1-fr.html"),
    ),  # type: ignore
    "http://www.cecill.info/licences/Licence_CeCILL_V1-fr.html": CreativeWork(
        identifier="CECILL-1.0",
        name="CeCILL Free Software License Agreement v1.0",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V1-fr.html"),
    ),  # type: ignore
    "CECILL-1.1": CreativeWork(
        identifier="CECILL-1.1",
        name="CeCILL Free Software License Agreement v1.1",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V1.1-US.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-1.1": CreativeWork(
        identifier="CECILL-1.1",
        name="CeCILL Free Software License Agreement v1.1",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V1.1-US.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-1.1.html": CreativeWork(
        identifier="CECILL-1.1",
        name="CeCILL Free Software License Agreement v1.1",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V1.1-US.html"),
    ),  # type: ignore
    "http://www.cecill.info/licences/Licence_CeCILL_V1.1-US.html": CreativeWork(
        identifier="CECILL-1.1",
        name="CeCILL Free Software License Agreement v1.1",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V1.1-US.html"),
    ),  # type: ignore
    "CECILL-2.0": CreativeWork(
        identifier="CECILL-2.0",
        name="CeCILL Free Software License Agreement v2.0",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V2-en.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-2.0": CreativeWork(
        identifier="CECILL-2.0",
        name="CeCILL Free Software License Agreement v2.0",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V2-en.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-2.0.html": CreativeWork(
        identifier="CECILL-2.0",
        name="CeCILL Free Software License Agreement v2.0",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V2-en.html"),
    ),  # type: ignore
    "http://www.cecill.info/licences/Licence_CeCILL_V2-en.html": CreativeWork(
        identifier="CECILL-2.0",
        name="CeCILL Free Software License Agreement v2.0",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V2-en.html"),
    ),  # type: ignore
    "CECILL-2.1": CreativeWork(
        identifier="CECILL-2.1",
        name="CeCILL Free Software License Agreement v2.1",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-2.1": CreativeWork(
        identifier="CECILL-2.1",
        name="CeCILL Free Software License Agreement v2.1",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-2.1.html": CreativeWork(
        identifier="CECILL-2.1",
        name="CeCILL Free Software License Agreement v2.1",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html"),
    ),  # type: ignore
    "http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html": CreativeWork(
        identifier="CECILL-2.1",
        name="CeCILL Free Software License Agreement v2.1",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html"),
    ),  # type: ignore
    "CECILL-B": CreativeWork(
        identifier="CECILL-B",
        name="CeCILL-B Free Software License Agreement",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-B": CreativeWork(
        identifier="CECILL-B",
        name="CeCILL-B Free Software License Agreement",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-B.html": CreativeWork(
        identifier="CECILL-B",
        name="CeCILL-B Free Software License Agreement",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html"),
    ),  # type: ignore
    "http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html": CreativeWork(
        identifier="CECILL-B",
        name="CeCILL-B Free Software License Agreement",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html"),
    ),  # type: ignore
    "CECILL-C": CreativeWork(
        identifier="CECILL-C",
        name="CeCILL-C Free Software License Agreement",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-C": CreativeWork(
        identifier="CECILL-C",
        name="CeCILL-C Free Software License Agreement",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CECILL-C.html": CreativeWork(
        identifier="CECILL-C",
        name="CeCILL-C Free Software License Agreement",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html"),
    ),  # type: ignore
    "http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html": CreativeWork(
        identifier="CECILL-C",
        name="CeCILL-C Free Software License Agreement",
        url=AnyUrl("http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html"),
    ),  # type: ignore
    "CERN-OHL-1.1": CreativeWork(
        identifier="CERN-OHL-1.1",
        name="CERN Open Hardware Licence v1.1",
        url=AnyUrl("https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-1.1": CreativeWork(
        identifier="CERN-OHL-1.1",
        name="CERN Open Hardware Licence v1.1",
        url=AnyUrl("https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-1.1.html": CreativeWork(
        identifier="CERN-OHL-1.1",
        name="CERN Open Hardware Licence v1.1",
        url=AnyUrl("https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.1"),
    ),  # type: ignore
    "https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.1": CreativeWork(
        identifier="CERN-OHL-1.1",
        name="CERN Open Hardware Licence v1.1",
        url=AnyUrl("https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.1"),
    ),  # type: ignore
    "CERN-OHL-1.2": CreativeWork(
        identifier="CERN-OHL-1.2",
        name="CERN Open Hardware Licence v1.2",
        url=AnyUrl("https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.2"),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-1.2": CreativeWork(
        identifier="CERN-OHL-1.2",
        name="CERN Open Hardware Licence v1.2",
        url=AnyUrl("https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.2"),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-1.2.html": CreativeWork(
        identifier="CERN-OHL-1.2",
        name="CERN Open Hardware Licence v1.2",
        url=AnyUrl("https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.2"),
    ),  # type: ignore
    "https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.2": CreativeWork(
        identifier="CERN-OHL-1.2",
        name="CERN Open Hardware Licence v1.2",
        url=AnyUrl("https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.2"),
    ),  # type: ignore
    "CERN-OHL-P-2.0": CreativeWork(
        identifier="CERN-OHL-P-2.0",
        name="CERN Open Hardware Licence Version 2 - Permissive",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-P-2.0": CreativeWork(
        identifier="CERN-OHL-P-2.0",
        name="CERN Open Hardware Licence Version 2 - Permissive",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-P-2.0.html": CreativeWork(
        identifier="CERN-OHL-P-2.0",
        name="CERN Open Hardware Licence Version 2 - Permissive",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2": CreativeWork(
        identifier="CERN-OHL-P-2.0",
        name="CERN Open Hardware Licence Version 2 - Permissive",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "CERN-OHL-S-2.0": CreativeWork(
        identifier="CERN-OHL-S-2.0",
        name="CERN Open Hardware Licence Version 2 - Strongly Reciprocal",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-S-2.0": CreativeWork(
        identifier="CERN-OHL-S-2.0",
        name="CERN Open Hardware Licence Version 2 - Strongly Reciprocal",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-S-2.0.html": CreativeWork(
        identifier="CERN-OHL-S-2.0",
        name="CERN Open Hardware Licence Version 2 - Strongly Reciprocal",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "CERN-OHL-W-2.0": CreativeWork(
        identifier="CERN-OHL-W-2.0",
        name="CERN Open Hardware Licence Version 2 - Weakly Reciprocal",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-W-2.0": CreativeWork(
        identifier="CERN-OHL-W-2.0",
        name="CERN Open Hardware Licence Version 2 - Weakly Reciprocal",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CERN-OHL-W-2.0.html": CreativeWork(
        identifier="CERN-OHL-W-2.0",
        name="CERN Open Hardware Licence Version 2 - Weakly Reciprocal",
        url=AnyUrl(
            "https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2"
        ),
    ),  # type: ignore
    "CFITSIO": CreativeWork(
        identifier="CFITSIO",
        name="CFITSIO License",
        url=AnyUrl(
            "https://heasarc.gsfc.nasa.gov/docs/software/fitsio/c/f_user/node9.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CFITSIO": CreativeWork(
        identifier="CFITSIO",
        name="CFITSIO License",
        url=AnyUrl(
            "https://heasarc.gsfc.nasa.gov/docs/software/fitsio/c/f_user/node9.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CFITSIO.html": CreativeWork(
        identifier="CFITSIO",
        name="CFITSIO License",
        url=AnyUrl(
            "https://heasarc.gsfc.nasa.gov/docs/software/fitsio/c/f_user/node9.html"
        ),
    ),  # type: ignore
    "https://heasarc.gsfc.nasa.gov/docs/software/fitsio/c/f_user/node9.html": CreativeWork(
        identifier="CFITSIO",
        name="CFITSIO License",
        url=AnyUrl(
            "https://heasarc.gsfc.nasa.gov/docs/software/fitsio/c/f_user/node9.html"
        ),
    ),  # type: ignore
    "check-cvs": CreativeWork(
        identifier="check-cvs",
        name="check-cvs License",
        url=AnyUrl(
            "http://cvs.savannah.gnu.org/viewvc/cvs/ccvs/contrib/check_cvs.in?revision=1.1.4.3&view=markup&pathrev=cvs1-11-23#l2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/check-cvs": CreativeWork(
        identifier="check-cvs",
        name="check-cvs License",
        url=AnyUrl(
            "http://cvs.savannah.gnu.org/viewvc/cvs/ccvs/contrib/check_cvs.in?revision=1.1.4.3&view=markup&pathrev=cvs1-11-23#l2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/check-cvs.html": CreativeWork(
        identifier="check-cvs",
        name="check-cvs License",
        url=AnyUrl(
            "http://cvs.savannah.gnu.org/viewvc/cvs/ccvs/contrib/check_cvs.in?revision=1.1.4.3&view=markup&pathrev=cvs1-11-23#l2"
        ),
    ),  # type: ignore
    "http://cvs.savannah.gnu.org/viewvc/cvs/ccvs/contrib/check_cvs.in?revision=1.1.4.3&view=markup&pathrev=cvs1-11-23#l2": CreativeWork(
        identifier="check-cvs",
        name="check-cvs License",
        url=AnyUrl(
            "http://cvs.savannah.gnu.org/viewvc/cvs/ccvs/contrib/check_cvs.in?revision=1.1.4.3&view=markup&pathrev=cvs1-11-23#l2"
        ),
    ),  # type: ignore
    "checkmk": CreativeWork(
        identifier="checkmk",
        name="Checkmk License",
        url=AnyUrl("https://github.com/libcheck/check/blob/master/checkmk/checkmk.in"),
    ),  # type: ignore
    "https://spdx.org/licenses/checkmk": CreativeWork(
        identifier="checkmk",
        name="Checkmk License",
        url=AnyUrl("https://github.com/libcheck/check/blob/master/checkmk/checkmk.in"),
    ),  # type: ignore
    "https://spdx.org/licenses/checkmk.html": CreativeWork(
        identifier="checkmk",
        name="Checkmk License",
        url=AnyUrl("https://github.com/libcheck/check/blob/master/checkmk/checkmk.in"),
    ),  # type: ignore
    "https://github.com/libcheck/check/blob/master/checkmk/checkmk.in": CreativeWork(
        identifier="checkmk",
        name="Checkmk License",
        url=AnyUrl("https://github.com/libcheck/check/blob/master/checkmk/checkmk.in"),
    ),  # type: ignore
    "ClArtistic": CreativeWork(
        identifier="ClArtistic",
        name="Clarified Artistic License",
        url=AnyUrl(
            "http://gianluca.dellavedova.org/2011/01/03/clarified-artistic-license/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ClArtistic": CreativeWork(
        identifier="ClArtistic",
        name="Clarified Artistic License",
        url=AnyUrl(
            "http://gianluca.dellavedova.org/2011/01/03/clarified-artistic-license/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ClArtistic.html": CreativeWork(
        identifier="ClArtistic",
        name="Clarified Artistic License",
        url=AnyUrl(
            "http://gianluca.dellavedova.org/2011/01/03/clarified-artistic-license/"
        ),
    ),  # type: ignore
    "http://gianluca.dellavedova.org/2011/01/03/clarified-artistic-license/": CreativeWork(
        identifier="ClArtistic",
        name="Clarified Artistic License",
        url=AnyUrl(
            "http://gianluca.dellavedova.org/2011/01/03/clarified-artistic-license/"
        ),
    ),  # type: ignore
    "Clips": CreativeWork(
        identifier="Clips",
        name="Clips License",
        url=AnyUrl("https://github.com/DrItanium/maya/blob/master/LICENSE.CLIPS"),
    ),  # type: ignore
    "https://spdx.org/licenses/Clips": CreativeWork(
        identifier="Clips",
        name="Clips License",
        url=AnyUrl("https://github.com/DrItanium/maya/blob/master/LICENSE.CLIPS"),
    ),  # type: ignore
    "https://spdx.org/licenses/Clips.html": CreativeWork(
        identifier="Clips",
        name="Clips License",
        url=AnyUrl("https://github.com/DrItanium/maya/blob/master/LICENSE.CLIPS"),
    ),  # type: ignore
    "https://github.com/DrItanium/maya/blob/master/LICENSE.CLIPS": CreativeWork(
        identifier="Clips",
        name="Clips License",
        url=AnyUrl("https://github.com/DrItanium/maya/blob/master/LICENSE.CLIPS"),
    ),  # type: ignore
    "CMU-Mach": CreativeWork(
        identifier="CMU-Mach",
        name="CMU Mach License",
        url=AnyUrl("https://www.cs.cmu.edu/~410/licenses.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CMU-Mach": CreativeWork(
        identifier="CMU-Mach",
        name="CMU Mach License",
        url=AnyUrl("https://www.cs.cmu.edu/~410/licenses.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CMU-Mach.html": CreativeWork(
        identifier="CMU-Mach",
        name="CMU Mach License",
        url=AnyUrl("https://www.cs.cmu.edu/~410/licenses.html"),
    ),  # type: ignore
    "https://www.cs.cmu.edu/~410/licenses.html": CreativeWork(
        identifier="CMU-Mach",
        name="CMU Mach License",
        url=AnyUrl("https://www.cs.cmu.edu/~410/licenses.html"),
    ),  # type: ignore
    "CMU-Mach-nodoc": CreativeWork(
        identifier="CMU-Mach-nodoc",
        name="CMU    Mach - no notices-in-documentation variant",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L718-L728"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CMU-Mach-nodoc": CreativeWork(
        identifier="CMU-Mach-nodoc",
        name="CMU    Mach - no notices-in-documentation variant",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L718-L728"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CMU-Mach-nodoc.html": CreativeWork(
        identifier="CMU-Mach-nodoc",
        name="CMU    Mach - no notices-in-documentation variant",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L718-L728"
        ),
    ),  # type: ignore
    "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L718-L728": CreativeWork(
        identifier="CMU-Mach-nodoc",
        name="CMU    Mach - no notices-in-documentation variant",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L718-L728"
        ),
    ),  # type: ignore
    "CNRI-Jython": CreativeWork(
        identifier="CNRI-Jython",
        name="CNRI Jython License",
        url=AnyUrl("http://www.jython.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CNRI-Jython": CreativeWork(
        identifier="CNRI-Jython",
        name="CNRI Jython License",
        url=AnyUrl("http://www.jython.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/CNRI-Jython.html": CreativeWork(
        identifier="CNRI-Jython",
        name="CNRI Jython License",
        url=AnyUrl("http://www.jython.org/license.html"),
    ),  # type: ignore
    "http://www.jython.org/license.html": CreativeWork(
        identifier="CNRI-Jython",
        name="CNRI Jython License",
        url=AnyUrl("http://www.jython.org/license.html"),
    ),  # type: ignore
    "CNRI-Python": CreativeWork(
        identifier="CNRI-Python",
        name="CNRI Python License",
        url=AnyUrl("https://opensource.org/licenses/CNRI-Python"),
    ),  # type: ignore
    "https://spdx.org/licenses/CNRI-Python": CreativeWork(
        identifier="CNRI-Python",
        name="CNRI Python License",
        url=AnyUrl("https://opensource.org/licenses/CNRI-Python"),
    ),  # type: ignore
    "https://spdx.org/licenses/CNRI-Python.html": CreativeWork(
        identifier="CNRI-Python",
        name="CNRI Python License",
        url=AnyUrl("https://opensource.org/licenses/CNRI-Python"),
    ),  # type: ignore
    "https://opensource.org/licenses/CNRI-Python": CreativeWork(
        identifier="CNRI-Python",
        name="CNRI Python License",
        url=AnyUrl("https://opensource.org/licenses/CNRI-Python"),
    ),  # type: ignore
    "CNRI-Python-GPL-Compatible": CreativeWork(
        identifier="CNRI-Python-GPL-Compatible",
        name="CNRI Python Open Source GPL Compatible License Agreement",
        url=AnyUrl("http://www.python.org/download/releases/1.6.1/download_win/"),
    ),  # type: ignore
    "https://spdx.org/licenses/CNRI-Python-GPL-Compatible": CreativeWork(
        identifier="CNRI-Python-GPL-Compatible",
        name="CNRI Python Open Source GPL Compatible License Agreement",
        url=AnyUrl("http://www.python.org/download/releases/1.6.1/download_win/"),
    ),  # type: ignore
    "https://spdx.org/licenses/CNRI-Python-GPL-Compatible.html": CreativeWork(
        identifier="CNRI-Python-GPL-Compatible",
        name="CNRI Python Open Source GPL Compatible License Agreement",
        url=AnyUrl("http://www.python.org/download/releases/1.6.1/download_win/"),
    ),  # type: ignore
    "http://www.python.org/download/releases/1.6.1/download_win/": CreativeWork(
        identifier="CNRI-Python-GPL-Compatible",
        name="CNRI Python Open Source GPL Compatible License Agreement",
        url=AnyUrl("http://www.python.org/download/releases/1.6.1/download_win/"),
    ),  # type: ignore
    "COIL-1.0": CreativeWork(
        identifier="COIL-1.0",
        name="Copyfree Open Innovation License",
        url=AnyUrl("https://coil.apotheon.org/plaintext/01.0.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/COIL-1.0": CreativeWork(
        identifier="COIL-1.0",
        name="Copyfree Open Innovation License",
        url=AnyUrl("https://coil.apotheon.org/plaintext/01.0.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/COIL-1.0.html": CreativeWork(
        identifier="COIL-1.0",
        name="Copyfree Open Innovation License",
        url=AnyUrl("https://coil.apotheon.org/plaintext/01.0.txt"),
    ),  # type: ignore
    "https://coil.apotheon.org/plaintext/01.0.txt": CreativeWork(
        identifier="COIL-1.0",
        name="Copyfree Open Innovation License",
        url=AnyUrl("https://coil.apotheon.org/plaintext/01.0.txt"),
    ),  # type: ignore
    "Community-Spec-1.0": CreativeWork(
        identifier="Community-Spec-1.0",
        name="Community Specification License 1.0",
        url=AnyUrl(
            "https://github.com/CommunitySpecification/1.0/blob/master/1._Community_Specification_License-v1.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Community-Spec-1.0": CreativeWork(
        identifier="Community-Spec-1.0",
        name="Community Specification License 1.0",
        url=AnyUrl(
            "https://github.com/CommunitySpecification/1.0/blob/master/1._Community_Specification_License-v1.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Community-Spec-1.0.html": CreativeWork(
        identifier="Community-Spec-1.0",
        name="Community Specification License 1.0",
        url=AnyUrl(
            "https://github.com/CommunitySpecification/1.0/blob/master/1._Community_Specification_License-v1.md"
        ),
    ),  # type: ignore
    "https://github.com/CommunitySpecification/1.0/blob/master/1._Community_Specification_License-v1.md": CreativeWork(
        identifier="Community-Spec-1.0",
        name="Community Specification License 1.0",
        url=AnyUrl(
            "https://github.com/CommunitySpecification/1.0/blob/master/1._Community_Specification_License-v1.md"
        ),
    ),  # type: ignore
    "Condor-1.1": CreativeWork(
        identifier="Condor-1.1",
        name="Condor Public License v1.1",
        url=AnyUrl("http://research.cs.wisc.edu/condor/license.html#condor"),
    ),  # type: ignore
    "https://spdx.org/licenses/Condor-1.1": CreativeWork(
        identifier="Condor-1.1",
        name="Condor Public License v1.1",
        url=AnyUrl("http://research.cs.wisc.edu/condor/license.html#condor"),
    ),  # type: ignore
    "https://spdx.org/licenses/Condor-1.1.html": CreativeWork(
        identifier="Condor-1.1",
        name="Condor Public License v1.1",
        url=AnyUrl("http://research.cs.wisc.edu/condor/license.html#condor"),
    ),  # type: ignore
    "http://research.cs.wisc.edu/condor/license.html#condor": CreativeWork(
        identifier="Condor-1.1",
        name="Condor Public License v1.1",
        url=AnyUrl("http://research.cs.wisc.edu/condor/license.html#condor"),
    ),  # type: ignore
    "copyleft-next-0.3.0": CreativeWork(
        identifier="copyleft-next-0.3.0",
        name="copyleft-next 0.3.0",
        url=AnyUrl(
            "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.0"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/copyleft-next-0.3.0": CreativeWork(
        identifier="copyleft-next-0.3.0",
        name="copyleft-next 0.3.0",
        url=AnyUrl(
            "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.0"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/copyleft-next-0.3.0.html": CreativeWork(
        identifier="copyleft-next-0.3.0",
        name="copyleft-next 0.3.0",
        url=AnyUrl(
            "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.0"
        ),
    ),  # type: ignore
    "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.0": CreativeWork(
        identifier="copyleft-next-0.3.0",
        name="copyleft-next 0.3.0",
        url=AnyUrl(
            "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.0"
        ),
    ),  # type: ignore
    "copyleft-next-0.3.1": CreativeWork(
        identifier="copyleft-next-0.3.1",
        name="copyleft-next 0.3.1",
        url=AnyUrl(
            "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.1"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/copyleft-next-0.3.1": CreativeWork(
        identifier="copyleft-next-0.3.1",
        name="copyleft-next 0.3.1",
        url=AnyUrl(
            "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.1"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/copyleft-next-0.3.1.html": CreativeWork(
        identifier="copyleft-next-0.3.1",
        name="copyleft-next 0.3.1",
        url=AnyUrl(
            "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.1"
        ),
    ),  # type: ignore
    "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.1": CreativeWork(
        identifier="copyleft-next-0.3.1",
        name="copyleft-next 0.3.1",
        url=AnyUrl(
            "https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.1"
        ),
    ),  # type: ignore
    "Cornell-Lossless-JPEG": CreativeWork(
        identifier="Cornell-Lossless-JPEG",
        name="Cornell Lossless JPEG License",
        url=AnyUrl(
            "https://android.googlesource.com/platform/external/dng_sdk/+/refs/heads/master/source/dng_lossless_jpeg.cpp#16"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Cornell-Lossless-JPEG": CreativeWork(
        identifier="Cornell-Lossless-JPEG",
        name="Cornell Lossless JPEG License",
        url=AnyUrl(
            "https://android.googlesource.com/platform/external/dng_sdk/+/refs/heads/master/source/dng_lossless_jpeg.cpp#16"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Cornell-Lossless-JPEG.html": CreativeWork(
        identifier="Cornell-Lossless-JPEG",
        name="Cornell Lossless JPEG License",
        url=AnyUrl(
            "https://android.googlesource.com/platform/external/dng_sdk/+/refs/heads/master/source/dng_lossless_jpeg.cpp#16"
        ),
    ),  # type: ignore
    "https://android.googlesource.com/platform/external/dng_sdk/+/refs/heads/master/source/dng_lossless_jpeg.cpp#16": CreativeWork(
        identifier="Cornell-Lossless-JPEG",
        name="Cornell Lossless JPEG License",
        url=AnyUrl(
            "https://android.googlesource.com/platform/external/dng_sdk/+/refs/heads/master/source/dng_lossless_jpeg.cpp#16"
        ),
    ),  # type: ignore
    "CPAL-1.0": CreativeWork(
        identifier="CPAL-1.0",
        name="Common Public Attribution License 1.0",
        url=AnyUrl("https://opensource.org/licenses/CPAL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CPAL-1.0": CreativeWork(
        identifier="CPAL-1.0",
        name="Common Public Attribution License 1.0",
        url=AnyUrl("https://opensource.org/licenses/CPAL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CPAL-1.0.html": CreativeWork(
        identifier="CPAL-1.0",
        name="Common Public Attribution License 1.0",
        url=AnyUrl("https://opensource.org/licenses/CPAL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/CPAL-1.0": CreativeWork(
        identifier="CPAL-1.0",
        name="Common Public Attribution License 1.0",
        url=AnyUrl("https://opensource.org/licenses/CPAL-1.0"),
    ),  # type: ignore
    "CPL-1.0": CreativeWork(
        identifier="CPL-1.0",
        name="Common Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/CPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CPL-1.0": CreativeWork(
        identifier="CPL-1.0",
        name="Common Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/CPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CPL-1.0.html": CreativeWork(
        identifier="CPL-1.0",
        name="Common Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/CPL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/CPL-1.0": CreativeWork(
        identifier="CPL-1.0",
        name="Common Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/CPL-1.0"),
    ),  # type: ignore
    "CPOL-1.02": CreativeWork(
        identifier="CPOL-1.02",
        name="Code Project Open License 1.02",
        url=AnyUrl("http://www.codeproject.com/info/cpol10.aspx"),
    ),  # type: ignore
    "https://spdx.org/licenses/CPOL-1.02": CreativeWork(
        identifier="CPOL-1.02",
        name="Code Project Open License 1.02",
        url=AnyUrl("http://www.codeproject.com/info/cpol10.aspx"),
    ),  # type: ignore
    "https://spdx.org/licenses/CPOL-1.02.html": CreativeWork(
        identifier="CPOL-1.02",
        name="Code Project Open License 1.02",
        url=AnyUrl("http://www.codeproject.com/info/cpol10.aspx"),
    ),  # type: ignore
    "http://www.codeproject.com/info/cpol10.aspx": CreativeWork(
        identifier="CPOL-1.02",
        name="Code Project Open License 1.02",
        url=AnyUrl("http://www.codeproject.com/info/cpol10.aspx"),
    ),  # type: ignore
    "Cronyx": CreativeWork(
        identifier="Cronyx",
        name="Cronyx License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/alias/-/blob/master/COPYING"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Cronyx": CreativeWork(
        identifier="Cronyx",
        name="Cronyx License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/alias/-/blob/master/COPYING"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Cronyx.html": CreativeWork(
        identifier="Cronyx",
        name="Cronyx License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/alias/-/blob/master/COPYING"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/font/alias/-/blob/master/COPYING": CreativeWork(
        identifier="Cronyx",
        name="Cronyx License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/alias/-/blob/master/COPYING"
        ),
    ),  # type: ignore
    "Crossword": CreativeWork(
        identifier="Crossword",
        name="Crossword License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Crossword"),
    ),  # type: ignore
    "https://spdx.org/licenses/Crossword": CreativeWork(
        identifier="Crossword",
        name="Crossword License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Crossword"),
    ),  # type: ignore
    "https://spdx.org/licenses/Crossword.html": CreativeWork(
        identifier="Crossword",
        name="Crossword License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Crossword"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Crossword": CreativeWork(
        identifier="Crossword",
        name="Crossword License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Crossword"),
    ),  # type: ignore
    "CryptoSwift": CreativeWork(
        identifier="CryptoSwift",
        name="CryptoSwift License",
        url=AnyUrl("https://github.com/krzyzanowskim/CryptoSwift/blob/main/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/CryptoSwift": CreativeWork(
        identifier="CryptoSwift",
        name="CryptoSwift License",
        url=AnyUrl("https://github.com/krzyzanowskim/CryptoSwift/blob/main/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/CryptoSwift.html": CreativeWork(
        identifier="CryptoSwift",
        name="CryptoSwift License",
        url=AnyUrl("https://github.com/krzyzanowskim/CryptoSwift/blob/main/LICENSE"),
    ),  # type: ignore
    "https://github.com/krzyzanowskim/CryptoSwift/blob/main/LICENSE": CreativeWork(
        identifier="CryptoSwift",
        name="CryptoSwift License",
        url=AnyUrl("https://github.com/krzyzanowskim/CryptoSwift/blob/main/LICENSE"),
    ),  # type: ignore
    "CrystalStacker": CreativeWork(
        identifier="CrystalStacker",
        name="CrystalStacker License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:CrystalStacker?rd=Licensing/CrystalStacker"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CrystalStacker": CreativeWork(
        identifier="CrystalStacker",
        name="CrystalStacker License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:CrystalStacker?rd=Licensing/CrystalStacker"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/CrystalStacker.html": CreativeWork(
        identifier="CrystalStacker",
        name="CrystalStacker License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:CrystalStacker?rd=Licensing/CrystalStacker"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing:CrystalStacker?rd=Licensing/CrystalStacker": CreativeWork(
        identifier="CrystalStacker",
        name="CrystalStacker License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:CrystalStacker?rd=Licensing/CrystalStacker"
        ),
    ),  # type: ignore
    "CUA-OPL-1.0": CreativeWork(
        identifier="CUA-OPL-1.0",
        name="CUA Office Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/CUA-OPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CUA-OPL-1.0": CreativeWork(
        identifier="CUA-OPL-1.0",
        name="CUA Office Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/CUA-OPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/CUA-OPL-1.0.html": CreativeWork(
        identifier="CUA-OPL-1.0",
        name="CUA Office Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/CUA-OPL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/CUA-OPL-1.0": CreativeWork(
        identifier="CUA-OPL-1.0",
        name="CUA Office Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/CUA-OPL-1.0"),
    ),  # type: ignore
    "Cube": CreativeWork(
        identifier="Cube",
        name="Cube License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Cube"),
    ),  # type: ignore
    "https://spdx.org/licenses/Cube": CreativeWork(
        identifier="Cube",
        name="Cube License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Cube"),
    ),  # type: ignore
    "https://spdx.org/licenses/Cube.html": CreativeWork(
        identifier="Cube",
        name="Cube License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Cube"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Cube": CreativeWork(
        identifier="Cube",
        name="Cube License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Cube"),
    ),  # type: ignore
    "curl": CreativeWork(
        identifier="curl",
        name="curl License",
        url=AnyUrl("https://github.com/bagder/curl/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/curl": CreativeWork(
        identifier="curl",
        name="curl License",
        url=AnyUrl("https://github.com/bagder/curl/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/curl.html": CreativeWork(
        identifier="curl",
        name="curl License",
        url=AnyUrl("https://github.com/bagder/curl/blob/master/COPYING"),
    ),  # type: ignore
    "https://github.com/bagder/curl/blob/master/COPYING": CreativeWork(
        identifier="curl",
        name="curl License",
        url=AnyUrl("https://github.com/bagder/curl/blob/master/COPYING"),
    ),  # type: ignore
    "cve-tou": CreativeWork(
        identifier="cve-tou",
        name="Common Vulnerability Enumeration ToU License",
        url=AnyUrl("https://www.cve.org/Legal/TermsOfUse"),
    ),  # type: ignore
    "https://spdx.org/licenses/cve-tou": CreativeWork(
        identifier="cve-tou",
        name="Common Vulnerability Enumeration ToU License",
        url=AnyUrl("https://www.cve.org/Legal/TermsOfUse"),
    ),  # type: ignore
    "https://spdx.org/licenses/cve-tou.html": CreativeWork(
        identifier="cve-tou",
        name="Common Vulnerability Enumeration ToU License",
        url=AnyUrl("https://www.cve.org/Legal/TermsOfUse"),
    ),  # type: ignore
    "https://www.cve.org/Legal/TermsOfUse": CreativeWork(
        identifier="cve-tou",
        name="Common Vulnerability Enumeration ToU License",
        url=AnyUrl("https://www.cve.org/Legal/TermsOfUse"),
    ),  # type: ignore
    "D-FSL-1.0": CreativeWork(
        identifier="D-FSL-1.0",
        name="Deutsche Freie Software Lizenz",
        url=AnyUrl("http://www.dipp.nrw.de/d-fsl/lizenzen/"),
    ),  # type: ignore
    "https://spdx.org/licenses/D-FSL-1.0": CreativeWork(
        identifier="D-FSL-1.0",
        name="Deutsche Freie Software Lizenz",
        url=AnyUrl("http://www.dipp.nrw.de/d-fsl/lizenzen/"),
    ),  # type: ignore
    "https://spdx.org/licenses/D-FSL-1.0.html": CreativeWork(
        identifier="D-FSL-1.0",
        name="Deutsche Freie Software Lizenz",
        url=AnyUrl("http://www.dipp.nrw.de/d-fsl/lizenzen/"),
    ),  # type: ignore
    "http://www.dipp.nrw.de/d-fsl/lizenzen/": CreativeWork(
        identifier="D-FSL-1.0",
        name="Deutsche Freie Software Lizenz",
        url=AnyUrl("http://www.dipp.nrw.de/d-fsl/lizenzen/"),
    ),  # type: ignore
    "DEC-3-Clause": CreativeWork(
        identifier="DEC-3-Clause",
        name="DEC 3-Clause License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L239"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DEC-3-Clause": CreativeWork(
        identifier="DEC-3-Clause",
        name="DEC 3-Clause License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L239"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DEC-3-Clause.html": CreativeWork(
        identifier="DEC-3-Clause",
        name="DEC 3-Clause License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L239"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L239": CreativeWork(
        identifier="DEC-3-Clause",
        name="DEC 3-Clause License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L239"
        ),
    ),  # type: ignore
    "diffmark": CreativeWork(
        identifier="diffmark",
        name="diffmark license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/diffmark"),
    ),  # type: ignore
    "https://spdx.org/licenses/diffmark": CreativeWork(
        identifier="diffmark",
        name="diffmark license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/diffmark"),
    ),  # type: ignore
    "https://spdx.org/licenses/diffmark.html": CreativeWork(
        identifier="diffmark",
        name="diffmark license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/diffmark"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/diffmark": CreativeWork(
        identifier="diffmark",
        name="diffmark license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/diffmark"),
    ),  # type: ignore
    "DL-DE-BY-2.0": CreativeWork(
        identifier="DL-DE-BY-2.0",
        name="Data licence Germany – attribution – version 2.0",
        url=AnyUrl("https://www.govdata.de/dl-de/by-2-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/DL-DE-BY-2.0": CreativeWork(
        identifier="DL-DE-BY-2.0",
        name="Data licence Germany – attribution – version 2.0",
        url=AnyUrl("https://www.govdata.de/dl-de/by-2-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/DL-DE-BY-2.0.html": CreativeWork(
        identifier="DL-DE-BY-2.0",
        name="Data licence Germany – attribution – version 2.0",
        url=AnyUrl("https://www.govdata.de/dl-de/by-2-0"),
    ),  # type: ignore
    "https://www.govdata.de/dl-de/by-2-0": CreativeWork(
        identifier="DL-DE-BY-2.0",
        name="Data licence Germany – attribution – version 2.0",
        url=AnyUrl("https://www.govdata.de/dl-de/by-2-0"),
    ),  # type: ignore
    "DL-DE-ZERO-2.0": CreativeWork(
        identifier="DL-DE-ZERO-2.0",
        name="Data licence Germany – zero – version 2.0",
        url=AnyUrl("https://www.govdata.de/dl-de/zero-2-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/DL-DE-ZERO-2.0": CreativeWork(
        identifier="DL-DE-ZERO-2.0",
        name="Data licence Germany – zero – version 2.0",
        url=AnyUrl("https://www.govdata.de/dl-de/zero-2-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/DL-DE-ZERO-2.0.html": CreativeWork(
        identifier="DL-DE-ZERO-2.0",
        name="Data licence Germany – zero – version 2.0",
        url=AnyUrl("https://www.govdata.de/dl-de/zero-2-0"),
    ),  # type: ignore
    "https://www.govdata.de/dl-de/zero-2-0": CreativeWork(
        identifier="DL-DE-ZERO-2.0",
        name="Data licence Germany – zero – version 2.0",
        url=AnyUrl("https://www.govdata.de/dl-de/zero-2-0"),
    ),  # type: ignore
    "DOC": CreativeWork(
        identifier="DOC",
        name="DOC License",
        url=AnyUrl("http://www.cs.wustl.edu/~schmidt/ACE-copying.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/DOC": CreativeWork(
        identifier="DOC",
        name="DOC License",
        url=AnyUrl("http://www.cs.wustl.edu/~schmidt/ACE-copying.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/DOC.html": CreativeWork(
        identifier="DOC",
        name="DOC License",
        url=AnyUrl("http://www.cs.wustl.edu/~schmidt/ACE-copying.html"),
    ),  # type: ignore
    "http://www.cs.wustl.edu/~schmidt/ACE-copying.html": CreativeWork(
        identifier="DOC",
        name="DOC License",
        url=AnyUrl("http://www.cs.wustl.edu/~schmidt/ACE-copying.html"),
    ),  # type: ignore
    "DocBook-DTD": CreativeWork(
        identifier="DocBook-DTD",
        name="DocBook DTD License",
        url=AnyUrl("http://www.docbook.org/xml/simple/1.1/docbook-simple-1.1.zip"),
    ),  # type: ignore
    "https://spdx.org/licenses/DocBook-DTD": CreativeWork(
        identifier="DocBook-DTD",
        name="DocBook DTD License",
        url=AnyUrl("http://www.docbook.org/xml/simple/1.1/docbook-simple-1.1.zip"),
    ),  # type: ignore
    "https://spdx.org/licenses/DocBook-DTD.html": CreativeWork(
        identifier="DocBook-DTD",
        name="DocBook DTD License",
        url=AnyUrl("http://www.docbook.org/xml/simple/1.1/docbook-simple-1.1.zip"),
    ),  # type: ignore
    "http://www.docbook.org/xml/simple/1.1/docbook-simple-1.1.zip": CreativeWork(
        identifier="DocBook-DTD",
        name="DocBook DTD License",
        url=AnyUrl("http://www.docbook.org/xml/simple/1.1/docbook-simple-1.1.zip"),
    ),  # type: ignore
    "DocBook-Schema": CreativeWork(
        identifier="DocBook-Schema",
        name="DocBook Schema License",
        url=AnyUrl(
            "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/assembly/schema/docbook51b7.rnc"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DocBook-Schema": CreativeWork(
        identifier="DocBook-Schema",
        name="DocBook Schema License",
        url=AnyUrl(
            "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/assembly/schema/docbook51b7.rnc"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DocBook-Schema.html": CreativeWork(
        identifier="DocBook-Schema",
        name="DocBook Schema License",
        url=AnyUrl(
            "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/assembly/schema/docbook51b7.rnc"
        ),
    ),  # type: ignore
    "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/assembly/schema/docbook51b7.rnc": CreativeWork(
        identifier="DocBook-Schema",
        name="DocBook Schema License",
        url=AnyUrl(
            "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/assembly/schema/docbook51b7.rnc"
        ),
    ),  # type: ignore
    "DocBook-Stylesheet": CreativeWork(
        identifier="DocBook-Stylesheet",
        name="DocBook Stylesheet License",
        url=AnyUrl("http://www.docbook.org/xml/5.0/docbook-5.0.zip"),
    ),  # type: ignore
    "https://spdx.org/licenses/DocBook-Stylesheet": CreativeWork(
        identifier="DocBook-Stylesheet",
        name="DocBook Stylesheet License",
        url=AnyUrl("http://www.docbook.org/xml/5.0/docbook-5.0.zip"),
    ),  # type: ignore
    "https://spdx.org/licenses/DocBook-Stylesheet.html": CreativeWork(
        identifier="DocBook-Stylesheet",
        name="DocBook Stylesheet License",
        url=AnyUrl("http://www.docbook.org/xml/5.0/docbook-5.0.zip"),
    ),  # type: ignore
    "http://www.docbook.org/xml/5.0/docbook-5.0.zip": CreativeWork(
        identifier="DocBook-Stylesheet",
        name="DocBook Stylesheet License",
        url=AnyUrl("http://www.docbook.org/xml/5.0/docbook-5.0.zip"),
    ),  # type: ignore
    "DocBook-XML": CreativeWork(
        identifier="DocBook-XML",
        name="DocBook XML License",
        url=AnyUrl(
            "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/COPYING#L27"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DocBook-XML": CreativeWork(
        identifier="DocBook-XML",
        name="DocBook XML License",
        url=AnyUrl(
            "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/COPYING#L27"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DocBook-XML.html": CreativeWork(
        identifier="DocBook-XML",
        name="DocBook XML License",
        url=AnyUrl(
            "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/COPYING#L27"
        ),
    ),  # type: ignore
    "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/COPYING#L27": CreativeWork(
        identifier="DocBook-XML",
        name="DocBook XML License",
        url=AnyUrl(
            "https://github.com/docbook/xslt10-stylesheets/blob/efd62655c11cc8773708df7a843613fa1e932bf8/xsl/COPYING#L27"
        ),
    ),  # type: ignore
    "Dotseqn": CreativeWork(
        identifier="Dotseqn",
        name="Dotseqn License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Dotseqn"),
    ),  # type: ignore
    "https://spdx.org/licenses/Dotseqn": CreativeWork(
        identifier="Dotseqn",
        name="Dotseqn License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Dotseqn"),
    ),  # type: ignore
    "https://spdx.org/licenses/Dotseqn.html": CreativeWork(
        identifier="Dotseqn",
        name="Dotseqn License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Dotseqn"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Dotseqn": CreativeWork(
        identifier="Dotseqn",
        name="Dotseqn License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Dotseqn"),
    ),  # type: ignore
    "DRL-1.0": CreativeWork(
        identifier="DRL-1.0",
        name="Detection Rule License 1.0",
        url=AnyUrl(
            "https://github.com/Neo23x0/sigma/blob/master/LICENSE.Detection.Rules.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DRL-1.0": CreativeWork(
        identifier="DRL-1.0",
        name="Detection Rule License 1.0",
        url=AnyUrl(
            "https://github.com/Neo23x0/sigma/blob/master/LICENSE.Detection.Rules.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DRL-1.0.html": CreativeWork(
        identifier="DRL-1.0",
        name="Detection Rule License 1.0",
        url=AnyUrl(
            "https://github.com/Neo23x0/sigma/blob/master/LICENSE.Detection.Rules.md"
        ),
    ),  # type: ignore
    "https://github.com/Neo23x0/sigma/blob/master/LICENSE.Detection.Rules.md": CreativeWork(
        identifier="DRL-1.0",
        name="Detection Rule License 1.0",
        url=AnyUrl(
            "https://github.com/Neo23x0/sigma/blob/master/LICENSE.Detection.Rules.md"
        ),
    ),  # type: ignore
    "DRL-1.1": CreativeWork(
        identifier="DRL-1.1",
        name="Detection Rule License 1.1",
        url=AnyUrl(
            "https://github.com/SigmaHQ/Detection-Rule-License/blob/6ec7fbde6101d101b5b5d1fcb8f9b69fbc76c04a/LICENSE.Detection.Rules.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DRL-1.1": CreativeWork(
        identifier="DRL-1.1",
        name="Detection Rule License 1.1",
        url=AnyUrl(
            "https://github.com/SigmaHQ/Detection-Rule-License/blob/6ec7fbde6101d101b5b5d1fcb8f9b69fbc76c04a/LICENSE.Detection.Rules.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/DRL-1.1.html": CreativeWork(
        identifier="DRL-1.1",
        name="Detection Rule License 1.1",
        url=AnyUrl(
            "https://github.com/SigmaHQ/Detection-Rule-License/blob/6ec7fbde6101d101b5b5d1fcb8f9b69fbc76c04a/LICENSE.Detection.Rules.md"
        ),
    ),  # type: ignore
    "https://github.com/SigmaHQ/Detection-Rule-License/blob/6ec7fbde6101d101b5b5d1fcb8f9b69fbc76c04a/LICENSE.Detection.Rules.md": CreativeWork(
        identifier="DRL-1.1",
        name="Detection Rule License 1.1",
        url=AnyUrl(
            "https://github.com/SigmaHQ/Detection-Rule-License/blob/6ec7fbde6101d101b5b5d1fcb8f9b69fbc76c04a/LICENSE.Detection.Rules.md"
        ),
    ),  # type: ignore
    "DSDP": CreativeWork(
        identifier="DSDP",
        name="DSDP License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/DSDP"),
    ),  # type: ignore
    "https://spdx.org/licenses/DSDP": CreativeWork(
        identifier="DSDP",
        name="DSDP License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/DSDP"),
    ),  # type: ignore
    "https://spdx.org/licenses/DSDP.html": CreativeWork(
        identifier="DSDP",
        name="DSDP License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/DSDP"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/DSDP": CreativeWork(
        identifier="DSDP",
        name="DSDP License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/DSDP"),
    ),  # type: ignore
    "dtoa": CreativeWork(
        identifier="dtoa",
        name="David M. Gay dtoa License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/swipl-devel/blob/master/src/os/dtoa.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/dtoa": CreativeWork(
        identifier="dtoa",
        name="David M. Gay dtoa License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/swipl-devel/blob/master/src/os/dtoa.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/dtoa.html": CreativeWork(
        identifier="dtoa",
        name="David M. Gay dtoa License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/swipl-devel/blob/master/src/os/dtoa.c"
        ),
    ),  # type: ignore
    "https://github.com/SWI-Prolog/swipl-devel/blob/master/src/os/dtoa.c": CreativeWork(
        identifier="dtoa",
        name="David M. Gay dtoa License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/swipl-devel/blob/master/src/os/dtoa.c"
        ),
    ),  # type: ignore
    "dvipdfm": CreativeWork(
        identifier="dvipdfm",
        name="dvipdfm License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/dvipdfm"),
    ),  # type: ignore
    "https://spdx.org/licenses/dvipdfm": CreativeWork(
        identifier="dvipdfm",
        name="dvipdfm License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/dvipdfm"),
    ),  # type: ignore
    "https://spdx.org/licenses/dvipdfm.html": CreativeWork(
        identifier="dvipdfm",
        name="dvipdfm License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/dvipdfm"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/dvipdfm": CreativeWork(
        identifier="dvipdfm",
        name="dvipdfm License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/dvipdfm"),
    ),  # type: ignore
    "ECL-1.0": CreativeWork(
        identifier="ECL-1.0",
        name="Educational Community License v1.0",
        url=AnyUrl("https://opensource.org/licenses/ECL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/ECL-1.0": CreativeWork(
        identifier="ECL-1.0",
        name="Educational Community License v1.0",
        url=AnyUrl("https://opensource.org/licenses/ECL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/ECL-1.0.html": CreativeWork(
        identifier="ECL-1.0",
        name="Educational Community License v1.0",
        url=AnyUrl("https://opensource.org/licenses/ECL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/ECL-1.0": CreativeWork(
        identifier="ECL-1.0",
        name="Educational Community License v1.0",
        url=AnyUrl("https://opensource.org/licenses/ECL-1.0"),
    ),  # type: ignore
    "ECL-2.0": CreativeWork(
        identifier="ECL-2.0",
        name="Educational Community License v2.0",
        url=AnyUrl("https://opensource.org/licenses/ECL-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/ECL-2.0": CreativeWork(
        identifier="ECL-2.0",
        name="Educational Community License v2.0",
        url=AnyUrl("https://opensource.org/licenses/ECL-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/ECL-2.0.html": CreativeWork(
        identifier="ECL-2.0",
        name="Educational Community License v2.0",
        url=AnyUrl("https://opensource.org/licenses/ECL-2.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/ECL-2.0": CreativeWork(
        identifier="ECL-2.0",
        name="Educational Community License v2.0",
        url=AnyUrl("https://opensource.org/licenses/ECL-2.0"),
    ),  # type: ignore
    "eCos-2.0": CreativeWork(
        identifier="eCos-2.0",
        name="eCos license version 2.0",
        url=AnyUrl("https://www.gnu.org/licenses/ecos-license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/eCos-2.0": CreativeWork(
        identifier="eCos-2.0",
        name="eCos license version 2.0",
        url=AnyUrl("https://www.gnu.org/licenses/ecos-license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/eCos-2.0.html": CreativeWork(
        identifier="eCos-2.0",
        name="eCos license version 2.0",
        url=AnyUrl("https://www.gnu.org/licenses/ecos-license.html"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/ecos-license.html": CreativeWork(
        identifier="eCos-2.0",
        name="eCos license version 2.0",
        url=AnyUrl("https://www.gnu.org/licenses/ecos-license.html"),
    ),  # type: ignore
    "EFL-1.0": CreativeWork(
        identifier="EFL-1.0",
        name="Eiffel Forum License v1.0",
        url=AnyUrl("http://www.eiffel-nice.org/license/forum.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/EFL-1.0": CreativeWork(
        identifier="EFL-1.0",
        name="Eiffel Forum License v1.0",
        url=AnyUrl("http://www.eiffel-nice.org/license/forum.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/EFL-1.0.html": CreativeWork(
        identifier="EFL-1.0",
        name="Eiffel Forum License v1.0",
        url=AnyUrl("http://www.eiffel-nice.org/license/forum.txt"),
    ),  # type: ignore
    "http://www.eiffel-nice.org/license/forum.txt": CreativeWork(
        identifier="EFL-1.0",
        name="Eiffel Forum License v1.0",
        url=AnyUrl("http://www.eiffel-nice.org/license/forum.txt"),
    ),  # type: ignore
    "EFL-2.0": CreativeWork(
        identifier="EFL-2.0",
        name="Eiffel Forum License v2.0",
        url=AnyUrl("http://www.eiffel-nice.org/license/eiffel-forum-license-2.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/EFL-2.0": CreativeWork(
        identifier="EFL-2.0",
        name="Eiffel Forum License v2.0",
        url=AnyUrl("http://www.eiffel-nice.org/license/eiffel-forum-license-2.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/EFL-2.0.html": CreativeWork(
        identifier="EFL-2.0",
        name="Eiffel Forum License v2.0",
        url=AnyUrl("http://www.eiffel-nice.org/license/eiffel-forum-license-2.html"),
    ),  # type: ignore
    "http://www.eiffel-nice.org/license/eiffel-forum-license-2.html": CreativeWork(
        identifier="EFL-2.0",
        name="Eiffel Forum License v2.0",
        url=AnyUrl("http://www.eiffel-nice.org/license/eiffel-forum-license-2.html"),
    ),  # type: ignore
    "eGenix": CreativeWork(
        identifier="eGenix",
        name="eGenix.com Public License 1.1.0",
        url=AnyUrl(
            "http://www.egenix.com/products/eGenix.com-Public-License-1.1.0.pdf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/eGenix": CreativeWork(
        identifier="eGenix",
        name="eGenix.com Public License 1.1.0",
        url=AnyUrl(
            "http://www.egenix.com/products/eGenix.com-Public-License-1.1.0.pdf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/eGenix.html": CreativeWork(
        identifier="eGenix",
        name="eGenix.com Public License 1.1.0",
        url=AnyUrl(
            "http://www.egenix.com/products/eGenix.com-Public-License-1.1.0.pdf"
        ),
    ),  # type: ignore
    "http://www.egenix.com/products/eGenix.com-Public-License-1.1.0.pdf": CreativeWork(
        identifier="eGenix",
        name="eGenix.com Public License 1.1.0",
        url=AnyUrl(
            "http://www.egenix.com/products/eGenix.com-Public-License-1.1.0.pdf"
        ),
    ),  # type: ignore
    "Elastic-2.0": CreativeWork(
        identifier="Elastic-2.0",
        name="Elastic License 2.0",
        url=AnyUrl("https://www.elastic.co/licensing/elastic-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/Elastic-2.0": CreativeWork(
        identifier="Elastic-2.0",
        name="Elastic License 2.0",
        url=AnyUrl("https://www.elastic.co/licensing/elastic-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/Elastic-2.0.html": CreativeWork(
        identifier="Elastic-2.0",
        name="Elastic License 2.0",
        url=AnyUrl("https://www.elastic.co/licensing/elastic-license"),
    ),  # type: ignore
    "https://www.elastic.co/licensing/elastic-license": CreativeWork(
        identifier="Elastic-2.0",
        name="Elastic License 2.0",
        url=AnyUrl("https://www.elastic.co/licensing/elastic-license"),
    ),  # type: ignore
    "Entessa": CreativeWork(
        identifier="Entessa",
        name="Entessa Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/Entessa"),
    ),  # type: ignore
    "https://spdx.org/licenses/Entessa": CreativeWork(
        identifier="Entessa",
        name="Entessa Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/Entessa"),
    ),  # type: ignore
    "https://spdx.org/licenses/Entessa.html": CreativeWork(
        identifier="Entessa",
        name="Entessa Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/Entessa"),
    ),  # type: ignore
    "https://opensource.org/licenses/Entessa": CreativeWork(
        identifier="Entessa",
        name="Entessa Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/Entessa"),
    ),  # type: ignore
    "EPICS": CreativeWork(
        identifier="EPICS",
        name="EPICS Open License",
        url=AnyUrl("https://epics.anl.gov/license/open.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/EPICS": CreativeWork(
        identifier="EPICS",
        name="EPICS Open License",
        url=AnyUrl("https://epics.anl.gov/license/open.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/EPICS.html": CreativeWork(
        identifier="EPICS",
        name="EPICS Open License",
        url=AnyUrl("https://epics.anl.gov/license/open.php"),
    ),  # type: ignore
    "https://epics.anl.gov/license/open.php": CreativeWork(
        identifier="EPICS",
        name="EPICS Open License",
        url=AnyUrl("https://epics.anl.gov/license/open.php"),
    ),  # type: ignore
    "EPL-1.0": CreativeWork(
        identifier="EPL-1.0",
        name="Eclipse Public License 1.0",
        url=AnyUrl("http://www.eclipse.org/legal/epl-v10.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/EPL-1.0": CreativeWork(
        identifier="EPL-1.0",
        name="Eclipse Public License 1.0",
        url=AnyUrl("http://www.eclipse.org/legal/epl-v10.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/EPL-1.0.html": CreativeWork(
        identifier="EPL-1.0",
        name="Eclipse Public License 1.0",
        url=AnyUrl("http://www.eclipse.org/legal/epl-v10.html"),
    ),  # type: ignore
    "http://www.eclipse.org/legal/epl-v10.html": CreativeWork(
        identifier="EPL-1.0",
        name="Eclipse Public License 1.0",
        url=AnyUrl("http://www.eclipse.org/legal/epl-v10.html"),
    ),  # type: ignore
    "EPL-2.0": CreativeWork(
        identifier="EPL-2.0",
        name="Eclipse Public License 2.0",
        url=AnyUrl("https://www.eclipse.org/legal/epl-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/EPL-2.0": CreativeWork(
        identifier="EPL-2.0",
        name="Eclipse Public License 2.0",
        url=AnyUrl("https://www.eclipse.org/legal/epl-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/EPL-2.0.html": CreativeWork(
        identifier="EPL-2.0",
        name="Eclipse Public License 2.0",
        url=AnyUrl("https://www.eclipse.org/legal/epl-2.0"),
    ),  # type: ignore
    "https://www.eclipse.org/legal/epl-2.0": CreativeWork(
        identifier="EPL-2.0",
        name="Eclipse Public License 2.0",
        url=AnyUrl("https://www.eclipse.org/legal/epl-2.0"),
    ),  # type: ignore
    "ErlPL-1.1": CreativeWork(
        identifier="ErlPL-1.1",
        name="Erlang Public License v1.1",
        url=AnyUrl("http://www.erlang.org/EPLICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/ErlPL-1.1": CreativeWork(
        identifier="ErlPL-1.1",
        name="Erlang Public License v1.1",
        url=AnyUrl("http://www.erlang.org/EPLICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/ErlPL-1.1.html": CreativeWork(
        identifier="ErlPL-1.1",
        name="Erlang Public License v1.1",
        url=AnyUrl("http://www.erlang.org/EPLICENSE"),
    ),  # type: ignore
    "http://www.erlang.org/EPLICENSE": CreativeWork(
        identifier="ErlPL-1.1",
        name="Erlang Public License v1.1",
        url=AnyUrl("http://www.erlang.org/EPLICENSE"),
    ),  # type: ignore
    "ESA-PL-permissive-2.4": CreativeWork(
        identifier="ESA-PL-permissive-2.4",
        name="European Space Agency Public License – v2.4 – Permissive (Type 3)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-permissive-type-3"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ESA-PL-permissive-2.4": CreativeWork(
        identifier="ESA-PL-permissive-2.4",
        name="European Space Agency Public License – v2.4 – Permissive (Type 3)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-permissive-type-3"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ESA-PL-permissive-2.4.html": CreativeWork(
        identifier="ESA-PL-permissive-2.4",
        name="European Space Agency Public License – v2.4 – Permissive (Type 3)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-permissive-type-3"
        ),
    ),  # type: ignore
    "https://essr.esa.int/license/european-space-agency-public-license-v2-4-permissive-type-3": CreativeWork(
        identifier="ESA-PL-permissive-2.4",
        name="European Space Agency Public License – v2.4 – Permissive (Type 3)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-permissive-type-3"
        ),
    ),  # type: ignore
    "ESA-PL-strong-copyleft-2.4": CreativeWork(
        identifier="ESA-PL-strong-copyleft-2.4",
        name="European Space Agency Public License (ESA-PL) - V2.4 - Strong Copyleft (Type 1)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-strong-copyleft-type-1"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ESA-PL-strong-copyleft-2.4": CreativeWork(
        identifier="ESA-PL-strong-copyleft-2.4",
        name="European Space Agency Public License (ESA-PL) - V2.4 - Strong Copyleft (Type 1)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-strong-copyleft-type-1"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ESA-PL-strong-copyleft-2.4.html": CreativeWork(
        identifier="ESA-PL-strong-copyleft-2.4",
        name="European Space Agency Public License (ESA-PL) - V2.4 - Strong Copyleft (Type 1)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-strong-copyleft-type-1"
        ),
    ),  # type: ignore
    "https://essr.esa.int/license/european-space-agency-public-license-v2-4-strong-copyleft-type-1": CreativeWork(
        identifier="ESA-PL-strong-copyleft-2.4",
        name="European Space Agency Public License (ESA-PL) - V2.4 - Strong Copyleft (Type 1)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-strong-copyleft-type-1"
        ),
    ),  # type: ignore
    "ESA-PL-weak-copyleft-2.4": CreativeWork(
        identifier="ESA-PL-weak-copyleft-2.4",
        name="European Space Agency Public License – v2.4 – Weak Copyleft (Type 2)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-weak-copyleft-type-2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ESA-PL-weak-copyleft-2.4": CreativeWork(
        identifier="ESA-PL-weak-copyleft-2.4",
        name="European Space Agency Public License – v2.4 – Weak Copyleft (Type 2)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-weak-copyleft-type-2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ESA-PL-weak-copyleft-2.4.html": CreativeWork(
        identifier="ESA-PL-weak-copyleft-2.4",
        name="European Space Agency Public License – v2.4 – Weak Copyleft (Type 2)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-weak-copyleft-type-2"
        ),
    ),  # type: ignore
    "https://essr.esa.int/license/european-space-agency-public-license-v2-4-weak-copyleft-type-2": CreativeWork(
        identifier="ESA-PL-weak-copyleft-2.4",
        name="European Space Agency Public License – v2.4 – Weak Copyleft (Type 2)",
        url=AnyUrl(
            "https://essr.esa.int/license/european-space-agency-public-license-v2-4-weak-copyleft-type-2"
        ),
    ),  # type: ignore
    "etalab-2.0": CreativeWork(
        identifier="etalab-2.0",
        name="Etalab Open License 2.0",
        url=AnyUrl(
            "https://github.com/DISIC/politique-de-contribution-open-source/blob/master/LICENSE.pdf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/etalab-2.0": CreativeWork(
        identifier="etalab-2.0",
        name="Etalab Open License 2.0",
        url=AnyUrl(
            "https://github.com/DISIC/politique-de-contribution-open-source/blob/master/LICENSE.pdf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/etalab-2.0.html": CreativeWork(
        identifier="etalab-2.0",
        name="Etalab Open License 2.0",
        url=AnyUrl(
            "https://github.com/DISIC/politique-de-contribution-open-source/blob/master/LICENSE.pdf"
        ),
    ),  # type: ignore
    "https://github.com/DISIC/politique-de-contribution-open-source/blob/master/LICENSE.pdf": CreativeWork(
        identifier="etalab-2.0",
        name="Etalab Open License 2.0",
        url=AnyUrl(
            "https://github.com/DISIC/politique-de-contribution-open-source/blob/master/LICENSE.pdf"
        ),
    ),  # type: ignore
    "EUDatagrid": CreativeWork(
        identifier="EUDatagrid",
        name="EU DataGrid Software License",
        url=AnyUrl("http://eu-datagrid.web.cern.ch/eu-datagrid/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/EUDatagrid": CreativeWork(
        identifier="EUDatagrid",
        name="EU DataGrid Software License",
        url=AnyUrl("http://eu-datagrid.web.cern.ch/eu-datagrid/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/EUDatagrid.html": CreativeWork(
        identifier="EUDatagrid",
        name="EU DataGrid Software License",
        url=AnyUrl("http://eu-datagrid.web.cern.ch/eu-datagrid/license.html"),
    ),  # type: ignore
    "http://eu-datagrid.web.cern.ch/eu-datagrid/license.html": CreativeWork(
        identifier="EUDatagrid",
        name="EU DataGrid Software License",
        url=AnyUrl("http://eu-datagrid.web.cern.ch/eu-datagrid/license.html"),
    ),  # type: ignore
    "EUPL-1.0": CreativeWork(
        identifier="EUPL-1.0",
        name="European Union Public License 1.0",
        url=AnyUrl("http://ec.europa.eu/idabc/en/document/7330.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/EUPL-1.0": CreativeWork(
        identifier="EUPL-1.0",
        name="European Union Public License 1.0",
        url=AnyUrl("http://ec.europa.eu/idabc/en/document/7330.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/EUPL-1.0.html": CreativeWork(
        identifier="EUPL-1.0",
        name="European Union Public License 1.0",
        url=AnyUrl("http://ec.europa.eu/idabc/en/document/7330.html"),
    ),  # type: ignore
    "http://ec.europa.eu/idabc/en/document/7330.html": CreativeWork(
        identifier="EUPL-1.0",
        name="European Union Public License 1.0",
        url=AnyUrl("http://ec.europa.eu/idabc/en/document/7330.html"),
    ),  # type: ignore
    "EUPL-1.1": CreativeWork(
        identifier="EUPL-1.1",
        name="European Union Public License 1.1",
        url=AnyUrl("https://joinup.ec.europa.eu/software/page/eupl/licence-eupl"),
    ),  # type: ignore
    "https://spdx.org/licenses/EUPL-1.1": CreativeWork(
        identifier="EUPL-1.1",
        name="European Union Public License 1.1",
        url=AnyUrl("https://joinup.ec.europa.eu/software/page/eupl/licence-eupl"),
    ),  # type: ignore
    "https://spdx.org/licenses/EUPL-1.1.html": CreativeWork(
        identifier="EUPL-1.1",
        name="European Union Public License 1.1",
        url=AnyUrl("https://joinup.ec.europa.eu/software/page/eupl/licence-eupl"),
    ),  # type: ignore
    "https://joinup.ec.europa.eu/software/page/eupl/licence-eupl": CreativeWork(
        identifier="EUPL-1.1",
        name="European Union Public License 1.1",
        url=AnyUrl("https://joinup.ec.europa.eu/software/page/eupl/licence-eupl"),
    ),  # type: ignore
    "EUPL-1.2": CreativeWork(
        identifier="EUPL-1.2",
        name="European Union Public License 1.2",
        url=AnyUrl("https://joinup.ec.europa.eu/page/eupl-text-11-12"),
    ),  # type: ignore
    "https://spdx.org/licenses/EUPL-1.2": CreativeWork(
        identifier="EUPL-1.2",
        name="European Union Public License 1.2",
        url=AnyUrl("https://joinup.ec.europa.eu/page/eupl-text-11-12"),
    ),  # type: ignore
    "https://spdx.org/licenses/EUPL-1.2.html": CreativeWork(
        identifier="EUPL-1.2",
        name="European Union Public License 1.2",
        url=AnyUrl("https://joinup.ec.europa.eu/page/eupl-text-11-12"),
    ),  # type: ignore
    "https://joinup.ec.europa.eu/page/eupl-text-11-12": CreativeWork(
        identifier="EUPL-1.2",
        name="European Union Public License 1.2",
        url=AnyUrl("https://joinup.ec.europa.eu/page/eupl-text-11-12"),
    ),  # type: ignore
    "Eurosym": CreativeWork(
        identifier="Eurosym",
        name="Eurosym License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Eurosym"),
    ),  # type: ignore
    "https://spdx.org/licenses/Eurosym": CreativeWork(
        identifier="Eurosym",
        name="Eurosym License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Eurosym"),
    ),  # type: ignore
    "https://spdx.org/licenses/Eurosym.html": CreativeWork(
        identifier="Eurosym",
        name="Eurosym License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Eurosym"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Eurosym": CreativeWork(
        identifier="Eurosym",
        name="Eurosym License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Eurosym"),
    ),  # type: ignore
    "Fair": CreativeWork(
        identifier="Fair",
        name="Fair License",
        url=AnyUrl(
            "https://web.archive.org/web/20150926120323/http://fairlicense.org/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Fair": CreativeWork(
        identifier="Fair",
        name="Fair License",
        url=AnyUrl(
            "https://web.archive.org/web/20150926120323/http://fairlicense.org/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Fair.html": CreativeWork(
        identifier="Fair",
        name="Fair License",
        url=AnyUrl(
            "https://web.archive.org/web/20150926120323/http://fairlicense.org/"
        ),
    ),  # type: ignore
    "https://web.archive.org/web/20150926120323/http://fairlicense.org/": CreativeWork(
        identifier="Fair",
        name="Fair License",
        url=AnyUrl(
            "https://web.archive.org/web/20150926120323/http://fairlicense.org/"
        ),
    ),  # type: ignore
    "FBM": CreativeWork(
        identifier="FBM",
        name="Fuzzy Bitmap License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/packages-xpce/blob/161a40cd82004f731ba48024f9d30af388a7edf5/src/img/gifwrite.c#L21-L26"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FBM": CreativeWork(
        identifier="FBM",
        name="Fuzzy Bitmap License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/packages-xpce/blob/161a40cd82004f731ba48024f9d30af388a7edf5/src/img/gifwrite.c#L21-L26"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FBM.html": CreativeWork(
        identifier="FBM",
        name="Fuzzy Bitmap License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/packages-xpce/blob/161a40cd82004f731ba48024f9d30af388a7edf5/src/img/gifwrite.c#L21-L26"
        ),
    ),  # type: ignore
    "https://github.com/SWI-Prolog/packages-xpce/blob/161a40cd82004f731ba48024f9d30af388a7edf5/src/img/gifwrite.c#L21-L26": CreativeWork(
        identifier="FBM",
        name="Fuzzy Bitmap License",
        url=AnyUrl(
            "https://github.com/SWI-Prolog/packages-xpce/blob/161a40cd82004f731ba48024f9d30af388a7edf5/src/img/gifwrite.c#L21-L26"
        ),
    ),  # type: ignore
    "FDK-AAC": CreativeWork(
        identifier="FDK-AAC",
        name="Fraunhofer FDK AAC Codec Library",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/FDK-AAC"),
    ),  # type: ignore
    "https://spdx.org/licenses/FDK-AAC": CreativeWork(
        identifier="FDK-AAC",
        name="Fraunhofer FDK AAC Codec Library",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/FDK-AAC"),
    ),  # type: ignore
    "https://spdx.org/licenses/FDK-AAC.html": CreativeWork(
        identifier="FDK-AAC",
        name="Fraunhofer FDK AAC Codec Library",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/FDK-AAC"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/FDK-AAC": CreativeWork(
        identifier="FDK-AAC",
        name="Fraunhofer FDK AAC Codec Library",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/FDK-AAC"),
    ),  # type: ignore
    "Ferguson-Twofish": CreativeWork(
        identifier="Ferguson-Twofish",
        name="Ferguson Twofish License",
        url=AnyUrl(
            "https://github.com/wernerd/ZRTPCPP/blob/6b3cd8e6783642292bad0c21e3e5e5ce45ff3e03/cryptcommon/twofish.c#L113C3-L127"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Ferguson-Twofish": CreativeWork(
        identifier="Ferguson-Twofish",
        name="Ferguson Twofish License",
        url=AnyUrl(
            "https://github.com/wernerd/ZRTPCPP/blob/6b3cd8e6783642292bad0c21e3e5e5ce45ff3e03/cryptcommon/twofish.c#L113C3-L127"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Ferguson-Twofish.html": CreativeWork(
        identifier="Ferguson-Twofish",
        name="Ferguson Twofish License",
        url=AnyUrl(
            "https://github.com/wernerd/ZRTPCPP/blob/6b3cd8e6783642292bad0c21e3e5e5ce45ff3e03/cryptcommon/twofish.c#L113C3-L127"
        ),
    ),  # type: ignore
    "https://github.com/wernerd/ZRTPCPP/blob/6b3cd8e6783642292bad0c21e3e5e5ce45ff3e03/cryptcommon/twofish.c#L113C3-L127": CreativeWork(
        identifier="Ferguson-Twofish",
        name="Ferguson Twofish License",
        url=AnyUrl(
            "https://github.com/wernerd/ZRTPCPP/blob/6b3cd8e6783642292bad0c21e3e5e5ce45ff3e03/cryptcommon/twofish.c#L113C3-L127"
        ),
    ),  # type: ignore
    "Frameworx-1.0": CreativeWork(
        identifier="Frameworx-1.0",
        name="Frameworx Open License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Frameworx-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Frameworx-1.0": CreativeWork(
        identifier="Frameworx-1.0",
        name="Frameworx Open License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Frameworx-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Frameworx-1.0.html": CreativeWork(
        identifier="Frameworx-1.0",
        name="Frameworx Open License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Frameworx-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/Frameworx-1.0": CreativeWork(
        identifier="Frameworx-1.0",
        name="Frameworx Open License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Frameworx-1.0"),
    ),  # type: ignore
    "FreeBSD-DOC": CreativeWork(
        identifier="FreeBSD-DOC",
        name="FreeBSD Documentation License",
        url=AnyUrl("https://www.freebsd.org/copyright/freebsd-doc-license/"),
    ),  # type: ignore
    "https://spdx.org/licenses/FreeBSD-DOC": CreativeWork(
        identifier="FreeBSD-DOC",
        name="FreeBSD Documentation License",
        url=AnyUrl("https://www.freebsd.org/copyright/freebsd-doc-license/"),
    ),  # type: ignore
    "https://spdx.org/licenses/FreeBSD-DOC.html": CreativeWork(
        identifier="FreeBSD-DOC",
        name="FreeBSD Documentation License",
        url=AnyUrl("https://www.freebsd.org/copyright/freebsd-doc-license/"),
    ),  # type: ignore
    "https://www.freebsd.org/copyright/freebsd-doc-license/": CreativeWork(
        identifier="FreeBSD-DOC",
        name="FreeBSD Documentation License",
        url=AnyUrl("https://www.freebsd.org/copyright/freebsd-doc-license/"),
    ),  # type: ignore
    "FreeImage": CreativeWork(
        identifier="FreeImage",
        name="FreeImage Public License v1.0",
        url=AnyUrl("http://freeimage.sourceforge.net/freeimage-license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/FreeImage": CreativeWork(
        identifier="FreeImage",
        name="FreeImage Public License v1.0",
        url=AnyUrl("http://freeimage.sourceforge.net/freeimage-license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/FreeImage.html": CreativeWork(
        identifier="FreeImage",
        name="FreeImage Public License v1.0",
        url=AnyUrl("http://freeimage.sourceforge.net/freeimage-license.txt"),
    ),  # type: ignore
    "http://freeimage.sourceforge.net/freeimage-license.txt": CreativeWork(
        identifier="FreeImage",
        name="FreeImage Public License v1.0",
        url=AnyUrl("http://freeimage.sourceforge.net/freeimage-license.txt"),
    ),  # type: ignore
    "FSFAP": CreativeWork(
        identifier="FSFAP",
        name="FSF All Permissive License",
        url=AnyUrl(
            "https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFAP": CreativeWork(
        identifier="FSFAP",
        name="FSF All Permissive License",
        url=AnyUrl(
            "https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFAP.html": CreativeWork(
        identifier="FSFAP",
        name="FSF All Permissive License",
        url=AnyUrl(
            "https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html"
        ),
    ),  # type: ignore
    "https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html": CreativeWork(
        identifier="FSFAP",
        name="FSF All Permissive License",
        url=AnyUrl(
            "https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html"
        ),
    ),  # type: ignore
    "FSFAP-no-warranty-disclaimer": CreativeWork(
        identifier="FSFAP-no-warranty-disclaimer",
        name="FSF All Permissive License (without Warranty)",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/wget.git/tree/util/trunc.c?h=v1.21.3&id=40747a11e44ced5a8ac628a41f879ced3e2ebce9#n6"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFAP-no-warranty-disclaimer": CreativeWork(
        identifier="FSFAP-no-warranty-disclaimer",
        name="FSF All Permissive License (without Warranty)",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/wget.git/tree/util/trunc.c?h=v1.21.3&id=40747a11e44ced5a8ac628a41f879ced3e2ebce9#n6"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFAP-no-warranty-disclaimer.html": CreativeWork(
        identifier="FSFAP-no-warranty-disclaimer",
        name="FSF All Permissive License (without Warranty)",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/wget.git/tree/util/trunc.c?h=v1.21.3&id=40747a11e44ced5a8ac628a41f879ced3e2ebce9#n6"
        ),
    ),  # type: ignore
    "https://git.savannah.gnu.org/cgit/wget.git/tree/util/trunc.c?h=v1.21.3&id=40747a11e44ced5a8ac628a41f879ced3e2ebce9#n6": CreativeWork(
        identifier="FSFAP-no-warranty-disclaimer",
        name="FSF All Permissive License (without Warranty)",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/wget.git/tree/util/trunc.c?h=v1.21.3&id=40747a11e44ced5a8ac628a41f879ced3e2ebce9#n6"
        ),
    ),  # type: ignore
    "FSFUL": CreativeWork(
        identifier="FSFUL",
        name="FSF Unlimited License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFUL": CreativeWork(
        identifier="FSFUL",
        name="FSF Unlimited License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFUL.html": CreativeWork(
        identifier="FSFUL",
        name="FSF Unlimited License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License": CreativeWork(
        identifier="FSFUL",
        name="FSF Unlimited License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License"),
    ),  # type: ignore
    "FSFULLR": CreativeWork(
        identifier="FSFULLR",
        name="FSF Unlimited License (with License Retention)",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License#License_Retention_Variant"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFULLR": CreativeWork(
        identifier="FSFULLR",
        name="FSF Unlimited License (with License Retention)",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License#License_Retention_Variant"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFULLR.html": CreativeWork(
        identifier="FSFULLR",
        name="FSF Unlimited License (with License Retention)",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License#License_Retention_Variant"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License#License_Retention_Variant": CreativeWork(
        identifier="FSFULLR",
        name="FSF Unlimited License (with License Retention)",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License#License_Retention_Variant"
        ),
    ),  # type: ignore
    "FSFULLRSD": CreativeWork(
        identifier="FSFULLRSD",
        name="FSF Unlimited License (with License Retention and Short Disclaimer)",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/gnulib.git/tree/modules/COPYING?id=7b08932179d0d6b017f7df01a2ddf6e096b038e3"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFULLRSD": CreativeWork(
        identifier="FSFULLRSD",
        name="FSF Unlimited License (with License Retention and Short Disclaimer)",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/gnulib.git/tree/modules/COPYING?id=7b08932179d0d6b017f7df01a2ddf6e096b038e3"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFULLRSD.html": CreativeWork(
        identifier="FSFULLRSD",
        name="FSF Unlimited License (with License Retention and Short Disclaimer)",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/gnulib.git/tree/modules/COPYING?id=7b08932179d0d6b017f7df01a2ddf6e096b038e3"
        ),
    ),  # type: ignore
    "https://git.savannah.gnu.org/cgit/gnulib.git/tree/modules/COPYING?id=7b08932179d0d6b017f7df01a2ddf6e096b038e3": CreativeWork(
        identifier="FSFULLRSD",
        name="FSF Unlimited License (with License Retention and Short Disclaimer)",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/gnulib.git/tree/modules/COPYING?id=7b08932179d0d6b017f7df01a2ddf6e096b038e3"
        ),
    ),  # type: ignore
    "FSFULLRWD": CreativeWork(
        identifier="FSFULLRWD",
        name="FSF Unlimited License (With License Retention and Warranty Disclaimer)",
        url=AnyUrl("https://lists.gnu.org/archive/html/autoconf/2012-04/msg00061.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFULLRWD": CreativeWork(
        identifier="FSFULLRWD",
        name="FSF Unlimited License (With License Retention and Warranty Disclaimer)",
        url=AnyUrl("https://lists.gnu.org/archive/html/autoconf/2012-04/msg00061.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/FSFULLRWD.html": CreativeWork(
        identifier="FSFULLRWD",
        name="FSF Unlimited License (With License Retention and Warranty Disclaimer)",
        url=AnyUrl("https://lists.gnu.org/archive/html/autoconf/2012-04/msg00061.html"),
    ),  # type: ignore
    "https://lists.gnu.org/archive/html/autoconf/2012-04/msg00061.html": CreativeWork(
        identifier="FSFULLRWD",
        name="FSF Unlimited License (With License Retention and Warranty Disclaimer)",
        url=AnyUrl("https://lists.gnu.org/archive/html/autoconf/2012-04/msg00061.html"),
    ),  # type: ignore
    "FSL-1.1-ALv2": CreativeWork(
        identifier="FSL-1.1-ALv2",
        name="Functional Source License, Version 1.1, ALv2 Future License",
        url=AnyUrl("https://fsl.software/FSL-1.1-ALv2.template.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/FSL-1.1-ALv2": CreativeWork(
        identifier="FSL-1.1-ALv2",
        name="Functional Source License, Version 1.1, ALv2 Future License",
        url=AnyUrl("https://fsl.software/FSL-1.1-ALv2.template.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/FSL-1.1-ALv2.html": CreativeWork(
        identifier="FSL-1.1-ALv2",
        name="Functional Source License, Version 1.1, ALv2 Future License",
        url=AnyUrl("https://fsl.software/FSL-1.1-ALv2.template.md"),
    ),  # type: ignore
    "https://fsl.software/FSL-1.1-ALv2.template.md": CreativeWork(
        identifier="FSL-1.1-ALv2",
        name="Functional Source License, Version 1.1, ALv2 Future License",
        url=AnyUrl("https://fsl.software/FSL-1.1-ALv2.template.md"),
    ),  # type: ignore
    "FSL-1.1-MIT": CreativeWork(
        identifier="FSL-1.1-MIT",
        name="Functional Source License, Version 1.1, MIT Future License",
        url=AnyUrl("https://fsl.software/FSL-1.1-MIT.template.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/FSL-1.1-MIT": CreativeWork(
        identifier="FSL-1.1-MIT",
        name="Functional Source License, Version 1.1, MIT Future License",
        url=AnyUrl("https://fsl.software/FSL-1.1-MIT.template.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/FSL-1.1-MIT.html": CreativeWork(
        identifier="FSL-1.1-MIT",
        name="Functional Source License, Version 1.1, MIT Future License",
        url=AnyUrl("https://fsl.software/FSL-1.1-MIT.template.md"),
    ),  # type: ignore
    "https://fsl.software/FSL-1.1-MIT.template.md": CreativeWork(
        identifier="FSL-1.1-MIT",
        name="Functional Source License, Version 1.1, MIT Future License",
        url=AnyUrl("https://fsl.software/FSL-1.1-MIT.template.md"),
    ),  # type: ignore
    "FTL": CreativeWork(
        identifier="FTL",
        name="Freetype Project License",
        url=AnyUrl("http://freetype.fis.uniroma2.it/FTL.TXT"),
    ),  # type: ignore
    "https://spdx.org/licenses/FTL": CreativeWork(
        identifier="FTL",
        name="Freetype Project License",
        url=AnyUrl("http://freetype.fis.uniroma2.it/FTL.TXT"),
    ),  # type: ignore
    "https://spdx.org/licenses/FTL.html": CreativeWork(
        identifier="FTL",
        name="Freetype Project License",
        url=AnyUrl("http://freetype.fis.uniroma2.it/FTL.TXT"),
    ),  # type: ignore
    "http://freetype.fis.uniroma2.it/FTL.TXT": CreativeWork(
        identifier="FTL",
        name="Freetype Project License",
        url=AnyUrl("http://freetype.fis.uniroma2.it/FTL.TXT"),
    ),  # type: ignore
    "Furuseth": CreativeWork(
        identifier="Furuseth",
        name="Furuseth License",
        url=AnyUrl(
            "https://git.openldap.org/openldap/openldap/-/blob/master/COPYRIGHT?ref_type=heads#L39-51"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Furuseth": CreativeWork(
        identifier="Furuseth",
        name="Furuseth License",
        url=AnyUrl(
            "https://git.openldap.org/openldap/openldap/-/blob/master/COPYRIGHT?ref_type=heads#L39-51"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Furuseth.html": CreativeWork(
        identifier="Furuseth",
        name="Furuseth License",
        url=AnyUrl(
            "https://git.openldap.org/openldap/openldap/-/blob/master/COPYRIGHT?ref_type=heads#L39-51"
        ),
    ),  # type: ignore
    "https://git.openldap.org/openldap/openldap/-/blob/master/COPYRIGHT?ref_type=heads#L39-51": CreativeWork(
        identifier="Furuseth",
        name="Furuseth License",
        url=AnyUrl(
            "https://git.openldap.org/openldap/openldap/-/blob/master/COPYRIGHT?ref_type=heads#L39-51"
        ),
    ),  # type: ignore
    "fwlw": CreativeWork(
        identifier="fwlw",
        name="fwlw License",
        url=AnyUrl(
            "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/fwlw/README"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/fwlw": CreativeWork(
        identifier="fwlw",
        name="fwlw License",
        url=AnyUrl(
            "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/fwlw/README"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/fwlw.html": CreativeWork(
        identifier="fwlw",
        name="fwlw License",
        url=AnyUrl(
            "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/fwlw/README"
        ),
    ),  # type: ignore
    "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/fwlw/README": CreativeWork(
        identifier="fwlw",
        name="fwlw License",
        url=AnyUrl(
            "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/fwlw/README"
        ),
    ),  # type: ignore
    "Game-Programming-Gems": CreativeWork(
        identifier="Game-Programming-Gems",
        name="Game Programming Gems License",
        url=AnyUrl(
            "https://github.com/OGRECave/ogre/blob/master/OgreMain/include/OgreSingleton.h#L28C3-L35C46"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Game-Programming-Gems": CreativeWork(
        identifier="Game-Programming-Gems",
        name="Game Programming Gems License",
        url=AnyUrl(
            "https://github.com/OGRECave/ogre/blob/master/OgreMain/include/OgreSingleton.h#L28C3-L35C46"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Game-Programming-Gems.html": CreativeWork(
        identifier="Game-Programming-Gems",
        name="Game Programming Gems License",
        url=AnyUrl(
            "https://github.com/OGRECave/ogre/blob/master/OgreMain/include/OgreSingleton.h#L28C3-L35C46"
        ),
    ),  # type: ignore
    "https://github.com/OGRECave/ogre/blob/master/OgreMain/include/OgreSingleton.h#L28C3-L35C46": CreativeWork(
        identifier="Game-Programming-Gems",
        name="Game Programming Gems License",
        url=AnyUrl(
            "https://github.com/OGRECave/ogre/blob/master/OgreMain/include/OgreSingleton.h#L28C3-L35C46"
        ),
    ),  # type: ignore
    "GCR-docs": CreativeWork(
        identifier="GCR-docs",
        name="Gnome GCR Documentation License",
        url=AnyUrl("https://github.com/GNOME/gcr/blob/master/docs/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/GCR-docs": CreativeWork(
        identifier="GCR-docs",
        name="Gnome GCR Documentation License",
        url=AnyUrl("https://github.com/GNOME/gcr/blob/master/docs/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/GCR-docs.html": CreativeWork(
        identifier="GCR-docs",
        name="Gnome GCR Documentation License",
        url=AnyUrl("https://github.com/GNOME/gcr/blob/master/docs/COPYING"),
    ),  # type: ignore
    "https://github.com/GNOME/gcr/blob/master/docs/COPYING": CreativeWork(
        identifier="GCR-docs",
        name="Gnome GCR Documentation License",
        url=AnyUrl("https://github.com/GNOME/gcr/blob/master/docs/COPYING"),
    ),  # type: ignore
    "GD": CreativeWork(
        identifier="GD",
        name="GD License",
        url=AnyUrl("https://libgd.github.io/manuals/2.3.0/files/license-txt.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GD": CreativeWork(
        identifier="GD",
        name="GD License",
        url=AnyUrl("https://libgd.github.io/manuals/2.3.0/files/license-txt.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GD.html": CreativeWork(
        identifier="GD",
        name="GD License",
        url=AnyUrl("https://libgd.github.io/manuals/2.3.0/files/license-txt.html"),
    ),  # type: ignore
    "https://libgd.github.io/manuals/2.3.0/files/license-txt.html": CreativeWork(
        identifier="GD",
        name="GD License",
        url=AnyUrl("https://libgd.github.io/manuals/2.3.0/files/license-txt.html"),
    ),  # type: ignore
    "generic-xts": CreativeWork(
        identifier="generic-xts",
        name="Generic XTS License",
        url=AnyUrl(
            "https://github.com/mhogomchungu/zuluCrypt/blob/master/external_libraries/tcplay/generic_xts.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/generic-xts": CreativeWork(
        identifier="generic-xts",
        name="Generic XTS License",
        url=AnyUrl(
            "https://github.com/mhogomchungu/zuluCrypt/blob/master/external_libraries/tcplay/generic_xts.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/generic-xts.html": CreativeWork(
        identifier="generic-xts",
        name="Generic XTS License",
        url=AnyUrl(
            "https://github.com/mhogomchungu/zuluCrypt/blob/master/external_libraries/tcplay/generic_xts.c"
        ),
    ),  # type: ignore
    "https://github.com/mhogomchungu/zuluCrypt/blob/master/external_libraries/tcplay/generic_xts.c": CreativeWork(
        identifier="generic-xts",
        name="Generic XTS License",
        url=AnyUrl(
            "https://github.com/mhogomchungu/zuluCrypt/blob/master/external_libraries/tcplay/generic_xts.c"
        ),
    ),  # type: ignore
    "GFDL-1.1": CreativeWork(
        identifier="GFDL-1.1",
        name="GNU Free Documentation License v1.1",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1": CreativeWork(
        identifier="GFDL-1.1",
        name="GNU Free Documentation License v1.1",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1.html": CreativeWork(
        identifier="GFDL-1.1",
        name="GNU Free Documentation License v1.1",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt": CreativeWork(
        identifier="GFDL-1.1",
        name="GNU Free Documentation License v1.1",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "GFDL-1.1-invariants-only": CreativeWork(
        identifier="GFDL-1.1-invariants-only",
        name="GNU Free Documentation License v1.1 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-invariants-only": CreativeWork(
        identifier="GFDL-1.1-invariants-only",
        name="GNU Free Documentation License v1.1 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-invariants-only.html": CreativeWork(
        identifier="GFDL-1.1-invariants-only",
        name="GNU Free Documentation License v1.1 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "GFDL-1.1-invariants-or-later": CreativeWork(
        identifier="GFDL-1.1-invariants-or-later",
        name="GNU Free Documentation License v1.1 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-invariants-or-later": CreativeWork(
        identifier="GFDL-1.1-invariants-or-later",
        name="GNU Free Documentation License v1.1 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-invariants-or-later.html": CreativeWork(
        identifier="GFDL-1.1-invariants-or-later",
        name="GNU Free Documentation License v1.1 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "GFDL-1.1-no-invariants-only": CreativeWork(
        identifier="GFDL-1.1-no-invariants-only",
        name="GNU Free Documentation License v1.1 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-no-invariants-only": CreativeWork(
        identifier="GFDL-1.1-no-invariants-only",
        name="GNU Free Documentation License v1.1 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-no-invariants-only.html": CreativeWork(
        identifier="GFDL-1.1-no-invariants-only",
        name="GNU Free Documentation License v1.1 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "GFDL-1.1-no-invariants-or-later": CreativeWork(
        identifier="GFDL-1.1-no-invariants-or-later",
        name="GNU Free Documentation License v1.1 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-no-invariants-or-later": CreativeWork(
        identifier="GFDL-1.1-no-invariants-or-later",
        name="GNU Free Documentation License v1.1 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-no-invariants-or-later.html": CreativeWork(
        identifier="GFDL-1.1-no-invariants-or-later",
        name="GNU Free Documentation License v1.1 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "GFDL-1.1-only": CreativeWork(
        identifier="GFDL-1.1-only",
        name="GNU Free Documentation License v1.1 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-only": CreativeWork(
        identifier="GFDL-1.1-only",
        name="GNU Free Documentation License v1.1 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-only.html": CreativeWork(
        identifier="GFDL-1.1-only",
        name="GNU Free Documentation License v1.1 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "GFDL-1.1-or-later": CreativeWork(
        identifier="GFDL-1.1-or-later",
        name="GNU Free Documentation License v1.1 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-or-later": CreativeWork(
        identifier="GFDL-1.1-or-later",
        name="GNU Free Documentation License v1.1 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.1-or-later.html": CreativeWork(
        identifier="GFDL-1.1-or-later",
        name="GNU Free Documentation License v1.1 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt"),
    ),  # type: ignore
    "GFDL-1.2": CreativeWork(
        identifier="GFDL-1.2",
        name="GNU Free Documentation License v1.2",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2": CreativeWork(
        identifier="GFDL-1.2",
        name="GNU Free Documentation License v1.2",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2.html": CreativeWork(
        identifier="GFDL-1.2",
        name="GNU Free Documentation License v1.2",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt": CreativeWork(
        identifier="GFDL-1.2",
        name="GNU Free Documentation License v1.2",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "GFDL-1.2-invariants-only": CreativeWork(
        identifier="GFDL-1.2-invariants-only",
        name="GNU Free Documentation License v1.2 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-invariants-only": CreativeWork(
        identifier="GFDL-1.2-invariants-only",
        name="GNU Free Documentation License v1.2 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-invariants-only.html": CreativeWork(
        identifier="GFDL-1.2-invariants-only",
        name="GNU Free Documentation License v1.2 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "GFDL-1.2-invariants-or-later": CreativeWork(
        identifier="GFDL-1.2-invariants-or-later",
        name="GNU Free Documentation License v1.2 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-invariants-or-later": CreativeWork(
        identifier="GFDL-1.2-invariants-or-later",
        name="GNU Free Documentation License v1.2 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-invariants-or-later.html": CreativeWork(
        identifier="GFDL-1.2-invariants-or-later",
        name="GNU Free Documentation License v1.2 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "GFDL-1.2-no-invariants-only": CreativeWork(
        identifier="GFDL-1.2-no-invariants-only",
        name="GNU Free Documentation License v1.2 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-no-invariants-only": CreativeWork(
        identifier="GFDL-1.2-no-invariants-only",
        name="GNU Free Documentation License v1.2 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-no-invariants-only.html": CreativeWork(
        identifier="GFDL-1.2-no-invariants-only",
        name="GNU Free Documentation License v1.2 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "GFDL-1.2-no-invariants-or-later": CreativeWork(
        identifier="GFDL-1.2-no-invariants-or-later",
        name="GNU Free Documentation License v1.2 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-no-invariants-or-later": CreativeWork(
        identifier="GFDL-1.2-no-invariants-or-later",
        name="GNU Free Documentation License v1.2 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-no-invariants-or-later.html": CreativeWork(
        identifier="GFDL-1.2-no-invariants-or-later",
        name="GNU Free Documentation License v1.2 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "GFDL-1.2-only": CreativeWork(
        identifier="GFDL-1.2-only",
        name="GNU Free Documentation License v1.2 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-only": CreativeWork(
        identifier="GFDL-1.2-only",
        name="GNU Free Documentation License v1.2 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-only.html": CreativeWork(
        identifier="GFDL-1.2-only",
        name="GNU Free Documentation License v1.2 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "GFDL-1.2-or-later": CreativeWork(
        identifier="GFDL-1.2-or-later",
        name="GNU Free Documentation License v1.2 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-or-later": CreativeWork(
        identifier="GFDL-1.2-or-later",
        name="GNU Free Documentation License v1.2 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.2-or-later.html": CreativeWork(
        identifier="GFDL-1.2-or-later",
        name="GNU Free Documentation License v1.2 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt"),
    ),  # type: ignore
    "GFDL-1.3": CreativeWork(
        identifier="GFDL-1.3",
        name="GNU Free Documentation License v1.3",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3": CreativeWork(
        identifier="GFDL-1.3",
        name="GNU Free Documentation License v1.3",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3.html": CreativeWork(
        identifier="GFDL-1.3",
        name="GNU Free Documentation License v1.3",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/fdl-1.3.txt": CreativeWork(
        identifier="GFDL-1.3",
        name="GNU Free Documentation License v1.3",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "GFDL-1.3-invariants-only": CreativeWork(
        identifier="GFDL-1.3-invariants-only",
        name="GNU Free Documentation License v1.3 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-invariants-only": CreativeWork(
        identifier="GFDL-1.3-invariants-only",
        name="GNU Free Documentation License v1.3 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-invariants-only.html": CreativeWork(
        identifier="GFDL-1.3-invariants-only",
        name="GNU Free Documentation License v1.3 only - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "GFDL-1.3-invariants-or-later": CreativeWork(
        identifier="GFDL-1.3-invariants-or-later",
        name="GNU Free Documentation License v1.3 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-invariants-or-later": CreativeWork(
        identifier="GFDL-1.3-invariants-or-later",
        name="GNU Free Documentation License v1.3 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-invariants-or-later.html": CreativeWork(
        identifier="GFDL-1.3-invariants-or-later",
        name="GNU Free Documentation License v1.3 or later - invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "GFDL-1.3-no-invariants-only": CreativeWork(
        identifier="GFDL-1.3-no-invariants-only",
        name="GNU Free Documentation License v1.3 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-no-invariants-only": CreativeWork(
        identifier="GFDL-1.3-no-invariants-only",
        name="GNU Free Documentation License v1.3 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-no-invariants-only.html": CreativeWork(
        identifier="GFDL-1.3-no-invariants-only",
        name="GNU Free Documentation License v1.3 only - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "GFDL-1.3-no-invariants-or-later": CreativeWork(
        identifier="GFDL-1.3-no-invariants-or-later",
        name="GNU Free Documentation License v1.3 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-no-invariants-or-later": CreativeWork(
        identifier="GFDL-1.3-no-invariants-or-later",
        name="GNU Free Documentation License v1.3 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-no-invariants-or-later.html": CreativeWork(
        identifier="GFDL-1.3-no-invariants-or-later",
        name="GNU Free Documentation License v1.3 or later - no invariants",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "GFDL-1.3-only": CreativeWork(
        identifier="GFDL-1.3-only",
        name="GNU Free Documentation License v1.3 only",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-only": CreativeWork(
        identifier="GFDL-1.3-only",
        name="GNU Free Documentation License v1.3 only",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-only.html": CreativeWork(
        identifier="GFDL-1.3-only",
        name="GNU Free Documentation License v1.3 only",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "GFDL-1.3-or-later": CreativeWork(
        identifier="GFDL-1.3-or-later",
        name="GNU Free Documentation License v1.3 or later",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-or-later": CreativeWork(
        identifier="GFDL-1.3-or-later",
        name="GNU Free Documentation License v1.3 or later",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/GFDL-1.3-or-later.html": CreativeWork(
        identifier="GFDL-1.3-or-later",
        name="GNU Free Documentation License v1.3 or later",
        url=AnyUrl("https://www.gnu.org/licenses/fdl-1.3.txt"),
    ),  # type: ignore
    "Giftware": CreativeWork(
        identifier="Giftware",
        name="Giftware License",
        url=AnyUrl("http://liballeg.org/license.html#allegro-4-the-giftware-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/Giftware": CreativeWork(
        identifier="Giftware",
        name="Giftware License",
        url=AnyUrl("http://liballeg.org/license.html#allegro-4-the-giftware-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/Giftware.html": CreativeWork(
        identifier="Giftware",
        name="Giftware License",
        url=AnyUrl("http://liballeg.org/license.html#allegro-4-the-giftware-license"),
    ),  # type: ignore
    "http://liballeg.org/license.html#allegro-4-the-giftware-license": CreativeWork(
        identifier="Giftware",
        name="Giftware License",
        url=AnyUrl("http://liballeg.org/license.html#allegro-4-the-giftware-license"),
    ),  # type: ignore
    "GL2PS": CreativeWork(
        identifier="GL2PS",
        name="GL2PS License",
        url=AnyUrl("http://www.geuz.org/gl2ps/COPYING.GL2PS"),
    ),  # type: ignore
    "https://spdx.org/licenses/GL2PS": CreativeWork(
        identifier="GL2PS",
        name="GL2PS License",
        url=AnyUrl("http://www.geuz.org/gl2ps/COPYING.GL2PS"),
    ),  # type: ignore
    "https://spdx.org/licenses/GL2PS.html": CreativeWork(
        identifier="GL2PS",
        name="GL2PS License",
        url=AnyUrl("http://www.geuz.org/gl2ps/COPYING.GL2PS"),
    ),  # type: ignore
    "http://www.geuz.org/gl2ps/COPYING.GL2PS": CreativeWork(
        identifier="GL2PS",
        name="GL2PS License",
        url=AnyUrl("http://www.geuz.org/gl2ps/COPYING.GL2PS"),
    ),  # type: ignore
    "Glide": CreativeWork(
        identifier="Glide",
        name="3dfx Glide License",
        url=AnyUrl("http://www.users.on.net/~triforce/glidexp/COPYING.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Glide": CreativeWork(
        identifier="Glide",
        name="3dfx Glide License",
        url=AnyUrl("http://www.users.on.net/~triforce/glidexp/COPYING.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Glide.html": CreativeWork(
        identifier="Glide",
        name="3dfx Glide License",
        url=AnyUrl("http://www.users.on.net/~triforce/glidexp/COPYING.txt"),
    ),  # type: ignore
    "http://www.users.on.net/~triforce/glidexp/COPYING.txt": CreativeWork(
        identifier="Glide",
        name="3dfx Glide License",
        url=AnyUrl("http://www.users.on.net/~triforce/glidexp/COPYING.txt"),
    ),  # type: ignore
    "Glulxe": CreativeWork(
        identifier="Glulxe",
        name="Glulxe License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Glulxe"),
    ),  # type: ignore
    "https://spdx.org/licenses/Glulxe": CreativeWork(
        identifier="Glulxe",
        name="Glulxe License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Glulxe"),
    ),  # type: ignore
    "https://spdx.org/licenses/Glulxe.html": CreativeWork(
        identifier="Glulxe",
        name="Glulxe License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Glulxe"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Glulxe": CreativeWork(
        identifier="Glulxe",
        name="Glulxe License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Glulxe"),
    ),  # type: ignore
    "GLWTPL": CreativeWork(
        identifier="GLWTPL",
        name="Good Luck With That Public License",
        url=AnyUrl(
            "https://github.com/me-shaon/GLWTPL/commit/da5f6bc734095efbacb442c0b31e33a65b9d6e85"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/GLWTPL": CreativeWork(
        identifier="GLWTPL",
        name="Good Luck With That Public License",
        url=AnyUrl(
            "https://github.com/me-shaon/GLWTPL/commit/da5f6bc734095efbacb442c0b31e33a65b9d6e85"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/GLWTPL.html": CreativeWork(
        identifier="GLWTPL",
        name="Good Luck With That Public License",
        url=AnyUrl(
            "https://github.com/me-shaon/GLWTPL/commit/da5f6bc734095efbacb442c0b31e33a65b9d6e85"
        ),
    ),  # type: ignore
    "https://github.com/me-shaon/GLWTPL/commit/da5f6bc734095efbacb442c0b31e33a65b9d6e85": CreativeWork(
        identifier="GLWTPL",
        name="Good Luck With That Public License",
        url=AnyUrl(
            "https://github.com/me-shaon/GLWTPL/commit/da5f6bc734095efbacb442c0b31e33a65b9d6e85"
        ),
    ),  # type: ignore
    "gnuplot": CreativeWork(
        identifier="gnuplot",
        name="gnuplot License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Gnuplot"),
    ),  # type: ignore
    "https://spdx.org/licenses/gnuplot": CreativeWork(
        identifier="gnuplot",
        name="gnuplot License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Gnuplot"),
    ),  # type: ignore
    "https://spdx.org/licenses/gnuplot.html": CreativeWork(
        identifier="gnuplot",
        name="gnuplot License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Gnuplot"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Gnuplot": CreativeWork(
        identifier="gnuplot",
        name="gnuplot License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Gnuplot"),
    ),  # type: ignore
    "GPL-1.0": CreativeWork(
        identifier="GPL-1.0",
        name="GNU General Public License v1.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-1.0": CreativeWork(
        identifier="GPL-1.0",
        name="GNU General Public License v1.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-1.0.html": CreativeWork(
        identifier="GPL-1.0",
        name="GNU General Public License v1.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html": CreativeWork(
        identifier="GPL-1.0",
        name="GNU General Public License v1.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "GPL-1.0+": CreativeWork(
        identifier="GPL-1.0+",
        name="GNU General Public License v1.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-1.0+": CreativeWork(
        identifier="GPL-1.0+",
        name="GNU General Public License v1.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-1.0+.html": CreativeWork(
        identifier="GPL-1.0+",
        name="GNU General Public License v1.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "GPL-1.0-only": CreativeWork(
        identifier="GPL-1.0-only",
        name="GNU General Public License v1.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-1.0-only": CreativeWork(
        identifier="GPL-1.0-only",
        name="GNU General Public License v1.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-1.0-only.html": CreativeWork(
        identifier="GPL-1.0-only",
        name="GNU General Public License v1.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "GPL-1.0-or-later": CreativeWork(
        identifier="GPL-1.0-or-later",
        name="GNU General Public License v1.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-1.0-or-later": CreativeWork(
        identifier="GPL-1.0-or-later",
        name="GNU General Public License v1.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-1.0-or-later.html": CreativeWork(
        identifier="GPL-1.0-or-later",
        name="GNU General Public License v1.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html"),
    ),  # type: ignore
    "GPL-2.0": CreativeWork(
        identifier="GPL-2.0",
        name="GNU General Public License v2.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0": CreativeWork(
        identifier="GPL-2.0",
        name="GNU General Public License v2.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0.html": CreativeWork(
        identifier="GPL-2.0",
        name="GNU General Public License v2.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html": CreativeWork(
        identifier="GPL-2.0",
        name="GNU General Public License v2.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "GPL-2.0+": CreativeWork(
        identifier="GPL-2.0+",
        name="GNU General Public License v2.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0+": CreativeWork(
        identifier="GPL-2.0+",
        name="GNU General Public License v2.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0+.html": CreativeWork(
        identifier="GPL-2.0+",
        name="GNU General Public License v2.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "GPL-2.0-only": CreativeWork(
        identifier="GPL-2.0-only",
        name="GNU General Public License v2.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-only": CreativeWork(
        identifier="GPL-2.0-only",
        name="GNU General Public License v2.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-only.html": CreativeWork(
        identifier="GPL-2.0-only",
        name="GNU General Public License v2.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "GPL-2.0-or-later": CreativeWork(
        identifier="GPL-2.0-or-later",
        name="GNU General Public License v2.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-or-later": CreativeWork(
        identifier="GPL-2.0-or-later",
        name="GNU General Public License v2.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-or-later.html": CreativeWork(
        identifier="GPL-2.0-or-later",
        name="GNU General Public License v2.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html"),
    ),  # type: ignore
    "GPL-2.0-with-autoconf-exception": CreativeWork(
        identifier="GPL-2.0-with-autoconf-exception",
        name="GNU General Public License v2.0 w/Autoconf exception",
        url=AnyUrl("http://ac-archive.sourceforge.net/doc/copyright.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-autoconf-exception": CreativeWork(
        identifier="GPL-2.0-with-autoconf-exception",
        name="GNU General Public License v2.0 w/Autoconf exception",
        url=AnyUrl("http://ac-archive.sourceforge.net/doc/copyright.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-autoconf-exception.html": CreativeWork(
        identifier="GPL-2.0-with-autoconf-exception",
        name="GNU General Public License v2.0 w/Autoconf exception",
        url=AnyUrl("http://ac-archive.sourceforge.net/doc/copyright.html"),
    ),  # type: ignore
    "http://ac-archive.sourceforge.net/doc/copyright.html": CreativeWork(
        identifier="GPL-2.0-with-autoconf-exception",
        name="GNU General Public License v2.0 w/Autoconf exception",
        url=AnyUrl("http://ac-archive.sourceforge.net/doc/copyright.html"),
    ),  # type: ignore
    "GPL-2.0-with-bison-exception": CreativeWork(
        identifier="GPL-2.0-with-bison-exception",
        name="GNU General Public License v2.0 w/Bison exception",
        url=AnyUrl(
            "http://git.savannah.gnu.org/cgit/bison.git/tree/data/yacc.c?id=193d7c7054ba7197b0789e14965b739162319b5e#n141"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-bison-exception": CreativeWork(
        identifier="GPL-2.0-with-bison-exception",
        name="GNU General Public License v2.0 w/Bison exception",
        url=AnyUrl(
            "http://git.savannah.gnu.org/cgit/bison.git/tree/data/yacc.c?id=193d7c7054ba7197b0789e14965b739162319b5e#n141"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-bison-exception.html": CreativeWork(
        identifier="GPL-2.0-with-bison-exception",
        name="GNU General Public License v2.0 w/Bison exception",
        url=AnyUrl(
            "http://git.savannah.gnu.org/cgit/bison.git/tree/data/yacc.c?id=193d7c7054ba7197b0789e14965b739162319b5e#n141"
        ),
    ),  # type: ignore
    "http://git.savannah.gnu.org/cgit/bison.git/tree/data/yacc.c?id=193d7c7054ba7197b0789e14965b739162319b5e#n141": CreativeWork(
        identifier="GPL-2.0-with-bison-exception",
        name="GNU General Public License v2.0 w/Bison exception",
        url=AnyUrl(
            "http://git.savannah.gnu.org/cgit/bison.git/tree/data/yacc.c?id=193d7c7054ba7197b0789e14965b739162319b5e#n141"
        ),
    ),  # type: ignore
    "GPL-2.0-with-classpath-exception": CreativeWork(
        identifier="GPL-2.0-with-classpath-exception",
        name="GNU General Public License v2.0 w/Classpath exception",
        url=AnyUrl("https://www.gnu.org/software/classpath/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-classpath-exception": CreativeWork(
        identifier="GPL-2.0-with-classpath-exception",
        name="GNU General Public License v2.0 w/Classpath exception",
        url=AnyUrl("https://www.gnu.org/software/classpath/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-classpath-exception.html": CreativeWork(
        identifier="GPL-2.0-with-classpath-exception",
        name="GNU General Public License v2.0 w/Classpath exception",
        url=AnyUrl("https://www.gnu.org/software/classpath/license.html"),
    ),  # type: ignore
    "https://www.gnu.org/software/classpath/license.html": CreativeWork(
        identifier="GPL-2.0-with-classpath-exception",
        name="GNU General Public License v2.0 w/Classpath exception",
        url=AnyUrl("https://www.gnu.org/software/classpath/license.html"),
    ),  # type: ignore
    "GPL-2.0-with-font-exception": CreativeWork(
        identifier="GPL-2.0-with-font-exception",
        name="GNU General Public License v2.0 w/Font exception",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-faq.html#FontException"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-font-exception": CreativeWork(
        identifier="GPL-2.0-with-font-exception",
        name="GNU General Public License v2.0 w/Font exception",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-faq.html#FontException"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-font-exception.html": CreativeWork(
        identifier="GPL-2.0-with-font-exception",
        name="GNU General Public License v2.0 w/Font exception",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-faq.html#FontException"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/gpl-faq.html#FontException": CreativeWork(
        identifier="GPL-2.0-with-font-exception",
        name="GNU General Public License v2.0 w/Font exception",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-faq.html#FontException"),
    ),  # type: ignore
    "GPL-2.0-with-GCC-exception": CreativeWork(
        identifier="GPL-2.0-with-GCC-exception",
        name="GNU General Public License v2.0 w/GCC Runtime Library exception",
        url=AnyUrl(
            "https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=gcc/libgcc1.c;h=762f5143fc6eed57b6797c82710f3538aa52b40b;hb=cb143a3ce4fb417c68f5fa2691a1b1b1053dfba9#l10"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-GCC-exception": CreativeWork(
        identifier="GPL-2.0-with-GCC-exception",
        name="GNU General Public License v2.0 w/GCC Runtime Library exception",
        url=AnyUrl(
            "https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=gcc/libgcc1.c;h=762f5143fc6eed57b6797c82710f3538aa52b40b;hb=cb143a3ce4fb417c68f5fa2691a1b1b1053dfba9#l10"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-2.0-with-GCC-exception.html": CreativeWork(
        identifier="GPL-2.0-with-GCC-exception",
        name="GNU General Public License v2.0 w/GCC Runtime Library exception",
        url=AnyUrl(
            "https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=gcc/libgcc1.c;h=762f5143fc6eed57b6797c82710f3538aa52b40b;hb=cb143a3ce4fb417c68f5fa2691a1b1b1053dfba9#l10"
        ),
    ),  # type: ignore
    "https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=gcc/libgcc1.c;h=762f5143fc6eed57b6797c82710f3538aa52b40b;hb=cb143a3ce4fb417c68f5fa2691a1b1b1053dfba9#l10": CreativeWork(
        identifier="GPL-2.0-with-GCC-exception",
        name="GNU General Public License v2.0 w/GCC Runtime Library exception",
        url=AnyUrl(
            "https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=gcc/libgcc1.c;h=762f5143fc6eed57b6797c82710f3538aa52b40b;hb=cb143a3ce4fb417c68f5fa2691a1b1b1053dfba9#l10"
        ),
    ),  # type: ignore
    "GPL-3.0": CreativeWork(
        identifier="GPL-3.0",
        name="GNU General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0": CreativeWork(
        identifier="GPL-3.0",
        name="GNU General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0.html": CreativeWork(
        identifier="GPL-3.0",
        name="GNU General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/gpl-3.0-standalone.html": CreativeWork(
        identifier="GPL-3.0",
        name="GNU General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "GPL-3.0+": CreativeWork(
        identifier="GPL-3.0+",
        name="GNU General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0+": CreativeWork(
        identifier="GPL-3.0+",
        name="GNU General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0+.html": CreativeWork(
        identifier="GPL-3.0+",
        name="GNU General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "GPL-3.0-only": CreativeWork(
        identifier="GPL-3.0-only",
        name="GNU General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0-only": CreativeWork(
        identifier="GPL-3.0-only",
        name="GNU General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0-only.html": CreativeWork(
        identifier="GPL-3.0-only",
        name="GNU General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "GPL-3.0-or-later": CreativeWork(
        identifier="GPL-3.0-or-later",
        name="GNU General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0-or-later": CreativeWork(
        identifier="GPL-3.0-or-later",
        name="GNU General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0-or-later.html": CreativeWork(
        identifier="GPL-3.0-or-later",
        name="GNU General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/gpl-3.0-standalone.html"),
    ),  # type: ignore
    "GPL-3.0-with-autoconf-exception": CreativeWork(
        identifier="GPL-3.0-with-autoconf-exception",
        name="GNU General Public License v3.0 w/Autoconf exception",
        url=AnyUrl("https://www.gnu.org/licenses/autoconf-exception-3.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0-with-autoconf-exception": CreativeWork(
        identifier="GPL-3.0-with-autoconf-exception",
        name="GNU General Public License v3.0 w/Autoconf exception",
        url=AnyUrl("https://www.gnu.org/licenses/autoconf-exception-3.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0-with-autoconf-exception.html": CreativeWork(
        identifier="GPL-3.0-with-autoconf-exception",
        name="GNU General Public License v3.0 w/Autoconf exception",
        url=AnyUrl("https://www.gnu.org/licenses/autoconf-exception-3.0.html"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/autoconf-exception-3.0.html": CreativeWork(
        identifier="GPL-3.0-with-autoconf-exception",
        name="GNU General Public License v3.0 w/Autoconf exception",
        url=AnyUrl("https://www.gnu.org/licenses/autoconf-exception-3.0.html"),
    ),  # type: ignore
    "GPL-3.0-with-GCC-exception": CreativeWork(
        identifier="GPL-3.0-with-GCC-exception",
        name="GNU General Public License v3.0 w/GCC Runtime Library exception",
        url=AnyUrl("https://www.gnu.org/licenses/gcc-exception-3.1.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0-with-GCC-exception": CreativeWork(
        identifier="GPL-3.0-with-GCC-exception",
        name="GNU General Public License v3.0 w/GCC Runtime Library exception",
        url=AnyUrl("https://www.gnu.org/licenses/gcc-exception-3.1.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/GPL-3.0-with-GCC-exception.html": CreativeWork(
        identifier="GPL-3.0-with-GCC-exception",
        name="GNU General Public License v3.0 w/GCC Runtime Library exception",
        url=AnyUrl("https://www.gnu.org/licenses/gcc-exception-3.1.html"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/gcc-exception-3.1.html": CreativeWork(
        identifier="GPL-3.0-with-GCC-exception",
        name="GNU General Public License v3.0 w/GCC Runtime Library exception",
        url=AnyUrl("https://www.gnu.org/licenses/gcc-exception-3.1.html"),
    ),  # type: ignore
    "Graphics-Gems": CreativeWork(
        identifier="Graphics-Gems",
        name="Graphics Gems License",
        url=AnyUrl("https://github.com/erich666/GraphicsGems/blob/master/LICENSE.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/Graphics-Gems": CreativeWork(
        identifier="Graphics-Gems",
        name="Graphics Gems License",
        url=AnyUrl("https://github.com/erich666/GraphicsGems/blob/master/LICENSE.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/Graphics-Gems.html": CreativeWork(
        identifier="Graphics-Gems",
        name="Graphics Gems License",
        url=AnyUrl("https://github.com/erich666/GraphicsGems/blob/master/LICENSE.md"),
    ),  # type: ignore
    "https://github.com/erich666/GraphicsGems/blob/master/LICENSE.md": CreativeWork(
        identifier="Graphics-Gems",
        name="Graphics Gems License",
        url=AnyUrl("https://github.com/erich666/GraphicsGems/blob/master/LICENSE.md"),
    ),  # type: ignore
    "gSOAP-1.3b": CreativeWork(
        identifier="gSOAP-1.3b",
        name="gSOAP Public License v1.3b",
        url=AnyUrl("http://www.cs.fsu.edu/~engelen/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/gSOAP-1.3b": CreativeWork(
        identifier="gSOAP-1.3b",
        name="gSOAP Public License v1.3b",
        url=AnyUrl("http://www.cs.fsu.edu/~engelen/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/gSOAP-1.3b.html": CreativeWork(
        identifier="gSOAP-1.3b",
        name="gSOAP Public License v1.3b",
        url=AnyUrl("http://www.cs.fsu.edu/~engelen/license.html"),
    ),  # type: ignore
    "http://www.cs.fsu.edu/~engelen/license.html": CreativeWork(
        identifier="gSOAP-1.3b",
        name="gSOAP Public License v1.3b",
        url=AnyUrl("http://www.cs.fsu.edu/~engelen/license.html"),
    ),  # type: ignore
    "gtkbook": CreativeWork(
        identifier="gtkbook",
        name="gtkbook License",
        url=AnyUrl("https://github.com/slogan621/gtkbook"),
    ),  # type: ignore
    "https://spdx.org/licenses/gtkbook": CreativeWork(
        identifier="gtkbook",
        name="gtkbook License",
        url=AnyUrl("https://github.com/slogan621/gtkbook"),
    ),  # type: ignore
    "https://spdx.org/licenses/gtkbook.html": CreativeWork(
        identifier="gtkbook",
        name="gtkbook License",
        url=AnyUrl("https://github.com/slogan621/gtkbook"),
    ),  # type: ignore
    "https://github.com/slogan621/gtkbook": CreativeWork(
        identifier="gtkbook",
        name="gtkbook License",
        url=AnyUrl("https://github.com/slogan621/gtkbook"),
    ),  # type: ignore
    "Gutmann": CreativeWork(
        identifier="Gutmann",
        name="Gutmann License",
        url=AnyUrl("https://www.cs.auckland.ac.nz/~pgut001/dumpasn1.c"),
    ),  # type: ignore
    "https://spdx.org/licenses/Gutmann": CreativeWork(
        identifier="Gutmann",
        name="Gutmann License",
        url=AnyUrl("https://www.cs.auckland.ac.nz/~pgut001/dumpasn1.c"),
    ),  # type: ignore
    "https://spdx.org/licenses/Gutmann.html": CreativeWork(
        identifier="Gutmann",
        name="Gutmann License",
        url=AnyUrl("https://www.cs.auckland.ac.nz/~pgut001/dumpasn1.c"),
    ),  # type: ignore
    "https://www.cs.auckland.ac.nz/~pgut001/dumpasn1.c": CreativeWork(
        identifier="Gutmann",
        name="Gutmann License",
        url=AnyUrl("https://www.cs.auckland.ac.nz/~pgut001/dumpasn1.c"),
    ),  # type: ignore
    "HaskellReport": CreativeWork(
        identifier="HaskellReport",
        name="Haskell Language Report License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Haskell_Language_Report_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HaskellReport": CreativeWork(
        identifier="HaskellReport",
        name="Haskell Language Report License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Haskell_Language_Report_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HaskellReport.html": CreativeWork(
        identifier="HaskellReport",
        name="Haskell Language Report License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Haskell_Language_Report_License"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Haskell_Language_Report_License": CreativeWork(
        identifier="HaskellReport",
        name="Haskell Language Report License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Haskell_Language_Report_License"
        ),
    ),  # type: ignore
    "HDF5": CreativeWork(
        identifier="HDF5",
        name="HDF5 License",
        url=AnyUrl("https://github.com/HDFGroup/hdf5/?tab=License-1-ov-file#readme"),
    ),  # type: ignore
    "https://spdx.org/licenses/HDF5": CreativeWork(
        identifier="HDF5",
        name="HDF5 License",
        url=AnyUrl("https://github.com/HDFGroup/hdf5/?tab=License-1-ov-file#readme"),
    ),  # type: ignore
    "https://spdx.org/licenses/HDF5.html": CreativeWork(
        identifier="HDF5",
        name="HDF5 License",
        url=AnyUrl("https://github.com/HDFGroup/hdf5/?tab=License-1-ov-file#readme"),
    ),  # type: ignore
    "https://github.com/HDFGroup/hdf5/?tab=License-1-ov-file#readme": CreativeWork(
        identifier="HDF5",
        name="HDF5 License",
        url=AnyUrl("https://github.com/HDFGroup/hdf5/?tab=License-1-ov-file#readme"),
    ),  # type: ignore
    "hdparm": CreativeWork(
        identifier="hdparm",
        name="hdparm License",
        url=AnyUrl(
            "https://github.com/Distrotech/hdparm/blob/4517550db29a91420fb2b020349523b1b4512df2/LICENSE.TXT"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/hdparm": CreativeWork(
        identifier="hdparm",
        name="hdparm License",
        url=AnyUrl(
            "https://github.com/Distrotech/hdparm/blob/4517550db29a91420fb2b020349523b1b4512df2/LICENSE.TXT"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/hdparm.html": CreativeWork(
        identifier="hdparm",
        name="hdparm License",
        url=AnyUrl(
            "https://github.com/Distrotech/hdparm/blob/4517550db29a91420fb2b020349523b1b4512df2/LICENSE.TXT"
        ),
    ),  # type: ignore
    "https://github.com/Distrotech/hdparm/blob/4517550db29a91420fb2b020349523b1b4512df2/LICENSE.TXT": CreativeWork(
        identifier="hdparm",
        name="hdparm License",
        url=AnyUrl(
            "https://github.com/Distrotech/hdparm/blob/4517550db29a91420fb2b020349523b1b4512df2/LICENSE.TXT"
        ),
    ),  # type: ignore
    "HIDAPI": CreativeWork(
        identifier="HIDAPI",
        name="HIDAPI License",
        url=AnyUrl("https://github.com/signal11/hidapi/blob/master/LICENSE-orig.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/HIDAPI": CreativeWork(
        identifier="HIDAPI",
        name="HIDAPI License",
        url=AnyUrl("https://github.com/signal11/hidapi/blob/master/LICENSE-orig.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/HIDAPI.html": CreativeWork(
        identifier="HIDAPI",
        name="HIDAPI License",
        url=AnyUrl("https://github.com/signal11/hidapi/blob/master/LICENSE-orig.txt"),
    ),  # type: ignore
    "https://github.com/signal11/hidapi/blob/master/LICENSE-orig.txt": CreativeWork(
        identifier="HIDAPI",
        name="HIDAPI License",
        url=AnyUrl("https://github.com/signal11/hidapi/blob/master/LICENSE-orig.txt"),
    ),  # type: ignore
    "Hippocratic-2.1": CreativeWork(
        identifier="Hippocratic-2.1",
        name="Hippocratic License 2.1",
        url=AnyUrl("https://firstdonoharm.dev/version/2/1/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Hippocratic-2.1": CreativeWork(
        identifier="Hippocratic-2.1",
        name="Hippocratic License 2.1",
        url=AnyUrl("https://firstdonoharm.dev/version/2/1/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Hippocratic-2.1.html": CreativeWork(
        identifier="Hippocratic-2.1",
        name="Hippocratic License 2.1",
        url=AnyUrl("https://firstdonoharm.dev/version/2/1/license.html"),
    ),  # type: ignore
    "https://firstdonoharm.dev/version/2/1/license.html": CreativeWork(
        identifier="Hippocratic-2.1",
        name="Hippocratic License 2.1",
        url=AnyUrl("https://firstdonoharm.dev/version/2/1/license.html"),
    ),  # type: ignore
    "HP-1986": CreativeWork(
        identifier="HP-1986",
        name="Hewlett-Packard 1986 License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/hppa/memchr.S;h=1cca3e5e8867aa4bffef1f75a5c1bba25c0c441e;hb=HEAD#l2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HP-1986": CreativeWork(
        identifier="HP-1986",
        name="Hewlett-Packard 1986 License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/hppa/memchr.S;h=1cca3e5e8867aa4bffef1f75a5c1bba25c0c441e;hb=HEAD#l2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HP-1986.html": CreativeWork(
        identifier="HP-1986",
        name="Hewlett-Packard 1986 License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/hppa/memchr.S;h=1cca3e5e8867aa4bffef1f75a5c1bba25c0c441e;hb=HEAD#l2"
        ),
    ),  # type: ignore
    "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/hppa/memchr.S;h=1cca3e5e8867aa4bffef1f75a5c1bba25c0c441e;hb=HEAD#l2": CreativeWork(
        identifier="HP-1986",
        name="Hewlett-Packard 1986 License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/hppa/memchr.S;h=1cca3e5e8867aa4bffef1f75a5c1bba25c0c441e;hb=HEAD#l2"
        ),
    ),  # type: ignore
    "HP-1989": CreativeWork(
        identifier="HP-1989",
        name="Hewlett-Packard 1989 License",
        url=AnyUrl("https://github.com/bleargh45/Data-UUID/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/HP-1989": CreativeWork(
        identifier="HP-1989",
        name="Hewlett-Packard 1989 License",
        url=AnyUrl("https://github.com/bleargh45/Data-UUID/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/HP-1989.html": CreativeWork(
        identifier="HP-1989",
        name="Hewlett-Packard 1989 License",
        url=AnyUrl("https://github.com/bleargh45/Data-UUID/blob/master/LICENSE"),
    ),  # type: ignore
    "https://github.com/bleargh45/Data-UUID/blob/master/LICENSE": CreativeWork(
        identifier="HP-1989",
        name="Hewlett-Packard 1989 License",
        url=AnyUrl("https://github.com/bleargh45/Data-UUID/blob/master/LICENSE"),
    ),  # type: ignore
    "HPND": CreativeWork(
        identifier="HPND",
        name="Historical Permission Notice and Disclaimer",
        url=AnyUrl("https://opensource.org/licenses/HPND"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND": CreativeWork(
        identifier="HPND",
        name="Historical Permission Notice and Disclaimer",
        url=AnyUrl("https://opensource.org/licenses/HPND"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND.html": CreativeWork(
        identifier="HPND",
        name="Historical Permission Notice and Disclaimer",
        url=AnyUrl("https://opensource.org/licenses/HPND"),
    ),  # type: ignore
    "https://opensource.org/licenses/HPND": CreativeWork(
        identifier="HPND",
        name="Historical Permission Notice and Disclaimer",
        url=AnyUrl("https://opensource.org/licenses/HPND"),
    ),  # type: ignore
    "HPND-DEC": CreativeWork(
        identifier="HPND-DEC",
        name="Historical Permission Notice and Disclaimer - DEC variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/app/xkbcomp/-/blob/master/COPYING?ref_type=heads#L69"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-DEC": CreativeWork(
        identifier="HPND-DEC",
        name="Historical Permission Notice and Disclaimer - DEC variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/app/xkbcomp/-/blob/master/COPYING?ref_type=heads#L69"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-DEC.html": CreativeWork(
        identifier="HPND-DEC",
        name="Historical Permission Notice and Disclaimer - DEC variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/app/xkbcomp/-/blob/master/COPYING?ref_type=heads#L69"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/app/xkbcomp/-/blob/master/COPYING?ref_type=heads#L69": CreativeWork(
        identifier="HPND-DEC",
        name="Historical Permission Notice and Disclaimer - DEC variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/app/xkbcomp/-/blob/master/COPYING?ref_type=heads#L69"
        ),
    ),  # type: ignore
    "HPND-doc": CreativeWork(
        identifier="HPND-doc",
        name="Historical Permission Notice and Disclaimer - documentation variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxext/-/blob/master/COPYING?ref_type=heads#L185-197"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-doc": CreativeWork(
        identifier="HPND-doc",
        name="Historical Permission Notice and Disclaimer - documentation variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxext/-/blob/master/COPYING?ref_type=heads#L185-197"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-doc.html": CreativeWork(
        identifier="HPND-doc",
        name="Historical Permission Notice and Disclaimer - documentation variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxext/-/blob/master/COPYING?ref_type=heads#L185-197"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/lib/libxext/-/blob/master/COPYING?ref_type=heads#L185-197": CreativeWork(
        identifier="HPND-doc",
        name="Historical Permission Notice and Disclaimer - documentation variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxext/-/blob/master/COPYING?ref_type=heads#L185-197"
        ),
    ),  # type: ignore
    "HPND-doc-sell": CreativeWork(
        identifier="HPND-doc-sell",
        name="Historical Permission Notice and Disclaimer - documentation sell variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxtst/-/blob/master/COPYING?ref_type=heads#L108-117"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-doc-sell": CreativeWork(
        identifier="HPND-doc-sell",
        name="Historical Permission Notice and Disclaimer - documentation sell variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxtst/-/blob/master/COPYING?ref_type=heads#L108-117"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-doc-sell.html": CreativeWork(
        identifier="HPND-doc-sell",
        name="Historical Permission Notice and Disclaimer - documentation sell variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxtst/-/blob/master/COPYING?ref_type=heads#L108-117"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/lib/libxtst/-/blob/master/COPYING?ref_type=heads#L108-117": CreativeWork(
        identifier="HPND-doc-sell",
        name="Historical Permission Notice and Disclaimer - documentation sell variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxtst/-/blob/master/COPYING?ref_type=heads#L108-117"
        ),
    ),  # type: ignore
    "HPND-export-US": CreativeWork(
        identifier="HPND-export-US",
        name="HPND with US Government export control warning",
        url=AnyUrl("https://www.kermitproject.org/ck90.html#source"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-export-US": CreativeWork(
        identifier="HPND-export-US",
        name="HPND with US Government export control warning",
        url=AnyUrl("https://www.kermitproject.org/ck90.html#source"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-export-US.html": CreativeWork(
        identifier="HPND-export-US",
        name="HPND with US Government export control warning",
        url=AnyUrl("https://www.kermitproject.org/ck90.html#source"),
    ),  # type: ignore
    "https://www.kermitproject.org/ck90.html#source": CreativeWork(
        identifier="HPND-export-US",
        name="HPND with US Government export control warning",
        url=AnyUrl("https://www.kermitproject.org/ck90.html#source"),
    ),  # type: ignore
    "HPND-export-US-acknowledgement": CreativeWork(
        identifier="HPND-export-US-acknowledgement",
        name="HPND with US Government export control warning and acknowledgment",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L831-L852"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-export-US-acknowledgement": CreativeWork(
        identifier="HPND-export-US-acknowledgement",
        name="HPND with US Government export control warning and acknowledgment",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L831-L852"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-export-US-acknowledgement.html": CreativeWork(
        identifier="HPND-export-US-acknowledgement",
        name="HPND with US Government export control warning and acknowledgment",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L831-L852"
        ),
    ),  # type: ignore
    "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L831-L852": CreativeWork(
        identifier="HPND-export-US-acknowledgement",
        name="HPND with US Government export control warning and acknowledgment",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L831-L852"
        ),
    ),  # type: ignore
    "HPND-export-US-modify": CreativeWork(
        identifier="HPND-export-US-modify",
        name="HPND with US Government export control warning and modification rqmt",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L1157-L1182"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-export-US-modify": CreativeWork(
        identifier="HPND-export-US-modify",
        name="HPND with US Government export control warning and modification rqmt",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L1157-L1182"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-export-US-modify.html": CreativeWork(
        identifier="HPND-export-US-modify",
        name="HPND with US Government export control warning and modification rqmt",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L1157-L1182"
        ),
    ),  # type: ignore
    "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L1157-L1182": CreativeWork(
        identifier="HPND-export-US-modify",
        name="HPND with US Government export control warning and modification rqmt",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L1157-L1182"
        ),
    ),  # type: ignore
    "HPND-export2-US": CreativeWork(
        identifier="HPND-export2-US",
        name="HPND with US Government export control and 2 disclaimers",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L111-L133"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-export2-US": CreativeWork(
        identifier="HPND-export2-US",
        name="HPND with US Government export control and 2 disclaimers",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L111-L133"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-export2-US.html": CreativeWork(
        identifier="HPND-export2-US",
        name="HPND with US Government export control and 2 disclaimers",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L111-L133"
        ),
    ),  # type: ignore
    "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L111-L133": CreativeWork(
        identifier="HPND-export2-US",
        name="HPND with US Government export control and 2 disclaimers",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L111-L133"
        ),
    ),  # type: ignore
    "HPND-Fenneberg-Livingston": CreativeWork(
        identifier="HPND-Fenneberg-Livingston",
        name="Historical Permission Notice and Disclaimer - Fenneberg-Livingston variant",
        url=AnyUrl(
            "https://github.com/FreeRADIUS/freeradius-client/blob/master/COPYRIGHT#L32"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Fenneberg-Livingston": CreativeWork(
        identifier="HPND-Fenneberg-Livingston",
        name="Historical Permission Notice and Disclaimer - Fenneberg-Livingston variant",
        url=AnyUrl(
            "https://github.com/FreeRADIUS/freeradius-client/blob/master/COPYRIGHT#L32"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Fenneberg-Livingston.html": CreativeWork(
        identifier="HPND-Fenneberg-Livingston",
        name="Historical Permission Notice and Disclaimer - Fenneberg-Livingston variant",
        url=AnyUrl(
            "https://github.com/FreeRADIUS/freeradius-client/blob/master/COPYRIGHT#L32"
        ),
    ),  # type: ignore
    "https://github.com/FreeRADIUS/freeradius-client/blob/master/COPYRIGHT#L32": CreativeWork(
        identifier="HPND-Fenneberg-Livingston",
        name="Historical Permission Notice and Disclaimer - Fenneberg-Livingston variant",
        url=AnyUrl(
            "https://github.com/FreeRADIUS/freeradius-client/blob/master/COPYRIGHT#L32"
        ),
    ),  # type: ignore
    "HPND-INRIA-IMAG": CreativeWork(
        identifier="HPND-INRIA-IMAG",
        name="Historical Permission Notice and Disclaimer    - INRIA-IMAG variant",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/pppd/ipv6cp.c#L75-L83"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-INRIA-IMAG": CreativeWork(
        identifier="HPND-INRIA-IMAG",
        name="Historical Permission Notice and Disclaimer    - INRIA-IMAG variant",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/pppd/ipv6cp.c#L75-L83"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-INRIA-IMAG.html": CreativeWork(
        identifier="HPND-INRIA-IMAG",
        name="Historical Permission Notice and Disclaimer    - INRIA-IMAG variant",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/pppd/ipv6cp.c#L75-L83"
        ),
    ),  # type: ignore
    "https://github.com/ppp-project/ppp/blob/master/pppd/ipv6cp.c#L75-L83": CreativeWork(
        identifier="HPND-INRIA-IMAG",
        name="Historical Permission Notice and Disclaimer    - INRIA-IMAG variant",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/pppd/ipv6cp.c#L75-L83"
        ),
    ),  # type: ignore
    "HPND-Intel": CreativeWork(
        identifier="HPND-Intel",
        name="Historical Permission Notice and Disclaimer - Intel variant",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/i960/memcpy.S;hb=HEAD"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Intel": CreativeWork(
        identifier="HPND-Intel",
        name="Historical Permission Notice and Disclaimer - Intel variant",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/i960/memcpy.S;hb=HEAD"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Intel.html": CreativeWork(
        identifier="HPND-Intel",
        name="Historical Permission Notice and Disclaimer - Intel variant",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/i960/memcpy.S;hb=HEAD"
        ),
    ),  # type: ignore
    "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/i960/memcpy.S;hb=HEAD": CreativeWork(
        identifier="HPND-Intel",
        name="Historical Permission Notice and Disclaimer - Intel variant",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/i960/memcpy.S;hb=HEAD"
        ),
    ),  # type: ignore
    "HPND-Kevlin-Henney": CreativeWork(
        identifier="HPND-Kevlin-Henney",
        name="Historical Permission Notice and Disclaimer - Kevlin Henney variant",
        url=AnyUrl(
            "https://github.com/mruby/mruby/blob/83d12f8d52522cdb7c8cc46fad34821359f453e6/mrbgems/mruby-dir/src/Win/dirent.c#L127-L140"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Kevlin-Henney": CreativeWork(
        identifier="HPND-Kevlin-Henney",
        name="Historical Permission Notice and Disclaimer - Kevlin Henney variant",
        url=AnyUrl(
            "https://github.com/mruby/mruby/blob/83d12f8d52522cdb7c8cc46fad34821359f453e6/mrbgems/mruby-dir/src/Win/dirent.c#L127-L140"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Kevlin-Henney.html": CreativeWork(
        identifier="HPND-Kevlin-Henney",
        name="Historical Permission Notice and Disclaimer - Kevlin Henney variant",
        url=AnyUrl(
            "https://github.com/mruby/mruby/blob/83d12f8d52522cdb7c8cc46fad34821359f453e6/mrbgems/mruby-dir/src/Win/dirent.c#L127-L140"
        ),
    ),  # type: ignore
    "https://github.com/mruby/mruby/blob/83d12f8d52522cdb7c8cc46fad34821359f453e6/mrbgems/mruby-dir/src/Win/dirent.c#L127-L140": CreativeWork(
        identifier="HPND-Kevlin-Henney",
        name="Historical Permission Notice and Disclaimer - Kevlin Henney variant",
        url=AnyUrl(
            "https://github.com/mruby/mruby/blob/83d12f8d52522cdb7c8cc46fad34821359f453e6/mrbgems/mruby-dir/src/Win/dirent.c#L127-L140"
        ),
    ),  # type: ignore
    "HPND-Markus-Kuhn": CreativeWork(
        identifier="HPND-Markus-Kuhn",
        name="Historical Permission Notice and Disclaimer - Markus Kuhn variant",
        url=AnyUrl("https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Markus-Kuhn": CreativeWork(
        identifier="HPND-Markus-Kuhn",
        name="Historical Permission Notice and Disclaimer - Markus Kuhn variant",
        url=AnyUrl("https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Markus-Kuhn.html": CreativeWork(
        identifier="HPND-Markus-Kuhn",
        name="Historical Permission Notice and Disclaimer - Markus Kuhn variant",
        url=AnyUrl("https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c"),
    ),  # type: ignore
    "https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c": CreativeWork(
        identifier="HPND-Markus-Kuhn",
        name="Historical Permission Notice and Disclaimer - Markus Kuhn variant",
        url=AnyUrl("https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c"),
    ),  # type: ignore
    "HPND-merchantability-variant": CreativeWork(
        identifier="HPND-merchantability-variant",
        name="Historical Permission Notice and Disclaimer - merchantability variant",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/misc/fini.c;hb=HEAD"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-merchantability-variant": CreativeWork(
        identifier="HPND-merchantability-variant",
        name="Historical Permission Notice and Disclaimer - merchantability variant",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/misc/fini.c;hb=HEAD"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-merchantability-variant.html": CreativeWork(
        identifier="HPND-merchantability-variant",
        name="Historical Permission Notice and Disclaimer - merchantability variant",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/misc/fini.c;hb=HEAD"
        ),
    ),  # type: ignore
    "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/misc/fini.c;hb=HEAD": CreativeWork(
        identifier="HPND-merchantability-variant",
        name="Historical Permission Notice and Disclaimer - merchantability variant",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/misc/fini.c;hb=HEAD"
        ),
    ),  # type: ignore
    "HPND-MIT-disclaimer": CreativeWork(
        identifier="HPND-MIT-disclaimer",
        name="Historical Permission Notice and Disclaimer with MIT disclaimer",
        url=AnyUrl(
            "https://metacpan.org/release/NLNETLABS/Net-DNS-SEC-1.22/source/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-MIT-disclaimer": CreativeWork(
        identifier="HPND-MIT-disclaimer",
        name="Historical Permission Notice and Disclaimer with MIT disclaimer",
        url=AnyUrl(
            "https://metacpan.org/release/NLNETLABS/Net-DNS-SEC-1.22/source/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-MIT-disclaimer.html": CreativeWork(
        identifier="HPND-MIT-disclaimer",
        name="Historical Permission Notice and Disclaimer with MIT disclaimer",
        url=AnyUrl(
            "https://metacpan.org/release/NLNETLABS/Net-DNS-SEC-1.22/source/LICENSE"
        ),
    ),  # type: ignore
    "https://metacpan.org/release/NLNETLABS/Net-DNS-SEC-1.22/source/LICENSE": CreativeWork(
        identifier="HPND-MIT-disclaimer",
        name="Historical Permission Notice and Disclaimer with MIT disclaimer",
        url=AnyUrl(
            "https://metacpan.org/release/NLNETLABS/Net-DNS-SEC-1.22/source/LICENSE"
        ),
    ),  # type: ignore
    "HPND-Netrek": CreativeWork(
        identifier="HPND-Netrek",
        name="Historical Permission Notice and Disclaimer - Netrek variant",
        url=AnyUrl("https://spdx.org/licenses/HPND-Netrek.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Netrek": CreativeWork(
        identifier="HPND-Netrek",
        name="Historical Permission Notice and Disclaimer - Netrek variant",
        url=AnyUrl("https://spdx.org/licenses/HPND-Netrek.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Netrek.html": CreativeWork(
        identifier="HPND-Netrek",
        name="Historical Permission Notice and Disclaimer - Netrek variant",
        url=AnyUrl("https://spdx.org/licenses/HPND-Netrek.html"),
    ),  # type: ignore
    "HPND-Pbmplus": CreativeWork(
        identifier="HPND-Pbmplus",
        name="Historical Permission Notice and Disclaimer - Pbmplus variant",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/netpbm.c#l8"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Pbmplus": CreativeWork(
        identifier="HPND-Pbmplus",
        name="Historical Permission Notice and Disclaimer - Pbmplus variant",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/netpbm.c#l8"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-Pbmplus.html": CreativeWork(
        identifier="HPND-Pbmplus",
        name="Historical Permission Notice and Disclaimer - Pbmplus variant",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/netpbm.c#l8"
        ),
    ),  # type: ignore
    "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/netpbm.c#l8": CreativeWork(
        identifier="HPND-Pbmplus",
        name="Historical Permission Notice and Disclaimer - Pbmplus variant",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/netpbm.c#l8"
        ),
    ),  # type: ignore
    "HPND-sell-MIT-disclaimer-xserver": CreativeWork(
        identifier="HPND-sell-MIT-disclaimer-xserver",
        name="Historical Permission Notice and Disclaimer - sell xserver variant with MIT disclaimer",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L1781"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-MIT-disclaimer-xserver": CreativeWork(
        identifier="HPND-sell-MIT-disclaimer-xserver",
        name="Historical Permission Notice and Disclaimer - sell xserver variant with MIT disclaimer",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L1781"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-MIT-disclaimer-xserver.html": CreativeWork(
        identifier="HPND-sell-MIT-disclaimer-xserver",
        name="Historical Permission Notice and Disclaimer - sell xserver variant with MIT disclaimer",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L1781"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L1781": CreativeWork(
        identifier="HPND-sell-MIT-disclaimer-xserver",
        name="Historical Permission Notice and Disclaimer - sell xserver variant with MIT disclaimer",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L1781"
        ),
    ),  # type: ignore
    "HPND-sell-regexpr": CreativeWork(
        identifier="HPND-sell-regexpr",
        name="Historical Permission Notice and Disclaimer - sell regexpr variant",
        url=AnyUrl(
            "https://gitlab.com/bacula-org/bacula/-/blob/Branch-11.0/bacula/LICENSE-FOSS?ref_type=heads#L245"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-regexpr": CreativeWork(
        identifier="HPND-sell-regexpr",
        name="Historical Permission Notice and Disclaimer - sell regexpr variant",
        url=AnyUrl(
            "https://gitlab.com/bacula-org/bacula/-/blob/Branch-11.0/bacula/LICENSE-FOSS?ref_type=heads#L245"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-regexpr.html": CreativeWork(
        identifier="HPND-sell-regexpr",
        name="Historical Permission Notice and Disclaimer - sell regexpr variant",
        url=AnyUrl(
            "https://gitlab.com/bacula-org/bacula/-/blob/Branch-11.0/bacula/LICENSE-FOSS?ref_type=heads#L245"
        ),
    ),  # type: ignore
    "https://gitlab.com/bacula-org/bacula/-/blob/Branch-11.0/bacula/LICENSE-FOSS?ref_type=heads#L245": CreativeWork(
        identifier="HPND-sell-regexpr",
        name="Historical Permission Notice and Disclaimer - sell regexpr variant",
        url=AnyUrl(
            "https://gitlab.com/bacula-org/bacula/-/blob/Branch-11.0/bacula/LICENSE-FOSS?ref_type=heads#L245"
        ),
    ),  # type: ignore
    "HPND-sell-variant": CreativeWork(
        identifier="HPND-sell-variant",
        name="Historical Permission Notice and Disclaimer - sell variant",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/sunrpc/auth_gss/gss_generic_token.c?h=v4.19"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-variant": CreativeWork(
        identifier="HPND-sell-variant",
        name="Historical Permission Notice and Disclaimer - sell variant",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/sunrpc/auth_gss/gss_generic_token.c?h=v4.19"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-variant.html": CreativeWork(
        identifier="HPND-sell-variant",
        name="Historical Permission Notice and Disclaimer - sell variant",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/sunrpc/auth_gss/gss_generic_token.c?h=v4.19"
        ),
    ),  # type: ignore
    "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/sunrpc/auth_gss/gss_generic_token.c?h=v4.19": CreativeWork(
        identifier="HPND-sell-variant",
        name="Historical Permission Notice and Disclaimer - sell variant",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/sunrpc/auth_gss/gss_generic_token.c?h=v4.19"
        ),
    ),  # type: ignore
    "HPND-sell-variant-critical-systems": CreativeWork(
        identifier="HPND-sell-variant-critical-systems",
        name="HPND - sell variant with safety critical systems clause",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/driver/xf86-video-voodoo/-/blob/68a5b6d98ae34749cca889f4373b4043d00bfe6a/src/voodoo_dga.c#L12-33"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-variant-critical-systems": CreativeWork(
        identifier="HPND-sell-variant-critical-systems",
        name="HPND - sell variant with safety critical systems clause",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/driver/xf86-video-voodoo/-/blob/68a5b6d98ae34749cca889f4373b4043d00bfe6a/src/voodoo_dga.c#L12-33"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-variant-critical-systems.html": CreativeWork(
        identifier="HPND-sell-variant-critical-systems",
        name="HPND - sell variant with safety critical systems clause",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/driver/xf86-video-voodoo/-/blob/68a5b6d98ae34749cca889f4373b4043d00bfe6a/src/voodoo_dga.c#L12-33"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/driver/xf86-video-voodoo/-/blob/68a5b6d98ae34749cca889f4373b4043d00bfe6a/src/voodoo_dga.c#L12-33": CreativeWork(
        identifier="HPND-sell-variant-critical-systems",
        name="HPND - sell variant with safety critical systems clause",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/driver/xf86-video-voodoo/-/blob/68a5b6d98ae34749cca889f4373b4043d00bfe6a/src/voodoo_dga.c#L12-33"
        ),
    ),  # type: ignore
    "HPND-sell-variant-MIT-disclaimer": CreativeWork(
        identifier="HPND-sell-variant-MIT-disclaimer",
        name="HPND sell variant with MIT disclaimer",
        url=AnyUrl(
            "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/README"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-variant-MIT-disclaimer": CreativeWork(
        identifier="HPND-sell-variant-MIT-disclaimer",
        name="HPND sell variant with MIT disclaimer",
        url=AnyUrl(
            "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/README"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-variant-MIT-disclaimer.html": CreativeWork(
        identifier="HPND-sell-variant-MIT-disclaimer",
        name="HPND sell variant with MIT disclaimer",
        url=AnyUrl(
            "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/README"
        ),
    ),  # type: ignore
    "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/README": CreativeWork(
        identifier="HPND-sell-variant-MIT-disclaimer",
        name="HPND sell variant with MIT disclaimer",
        url=AnyUrl(
            "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/README"
        ),
    ),  # type: ignore
    "HPND-sell-variant-MIT-disclaimer-rev": CreativeWork(
        identifier="HPND-sell-variant-MIT-disclaimer-rev",
        name="HPND sell variant with MIT disclaimer - reverse",
        url=AnyUrl(
            "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/dynlist.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-variant-MIT-disclaimer-rev": CreativeWork(
        identifier="HPND-sell-variant-MIT-disclaimer-rev",
        name="HPND sell variant with MIT disclaimer - reverse",
        url=AnyUrl(
            "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/dynlist.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-sell-variant-MIT-disclaimer-rev.html": CreativeWork(
        identifier="HPND-sell-variant-MIT-disclaimer-rev",
        name="HPND sell variant with MIT disclaimer - reverse",
        url=AnyUrl(
            "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/dynlist.c"
        ),
    ),  # type: ignore
    "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/dynlist.c": CreativeWork(
        identifier="HPND-sell-variant-MIT-disclaimer-rev",
        name="HPND sell variant with MIT disclaimer - reverse",
        url=AnyUrl(
            "https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/dynlist.c"
        ),
    ),  # type: ignore
    "HPND-SMC": CreativeWork(
        identifier="HPND-SMC",
        name="Historical Permission Notice and Disclaimer - SMC variant",
        url=AnyUrl("https://docs.python.org/3/license.html#execution-tracing"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-SMC": CreativeWork(
        identifier="HPND-SMC",
        name="Historical Permission Notice and Disclaimer - SMC variant",
        url=AnyUrl("https://docs.python.org/3/license.html#execution-tracing"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-SMC.html": CreativeWork(
        identifier="HPND-SMC",
        name="Historical Permission Notice and Disclaimer - SMC variant",
        url=AnyUrl("https://docs.python.org/3/license.html#execution-tracing"),
    ),  # type: ignore
    "https://docs.python.org/3/license.html#execution-tracing": CreativeWork(
        identifier="HPND-SMC",
        name="Historical Permission Notice and Disclaimer - SMC variant",
        url=AnyUrl("https://docs.python.org/3/license.html#execution-tracing"),
    ),  # type: ignore
    "HPND-UC": CreativeWork(
        identifier="HPND-UC",
        name="Historical Permission Notice and Disclaimer - University of California variant",
        url=AnyUrl("https://core.tcl-lang.org/tk/file?name=compat/unistd.h"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-UC": CreativeWork(
        identifier="HPND-UC",
        name="Historical Permission Notice and Disclaimer - University of California variant",
        url=AnyUrl("https://core.tcl-lang.org/tk/file?name=compat/unistd.h"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-UC.html": CreativeWork(
        identifier="HPND-UC",
        name="Historical Permission Notice and Disclaimer - University of California variant",
        url=AnyUrl("https://core.tcl-lang.org/tk/file?name=compat/unistd.h"),
    ),  # type: ignore
    "https://core.tcl-lang.org/tk/file?name=compat/unistd.h": CreativeWork(
        identifier="HPND-UC",
        name="Historical Permission Notice and Disclaimer - University of California variant",
        url=AnyUrl("https://core.tcl-lang.org/tk/file?name=compat/unistd.h"),
    ),  # type: ignore
    "HPND-UC-export-US": CreativeWork(
        identifier="HPND-UC-export-US",
        name="Historical Permission Notice and Disclaimer - University of California, US export warning",
        url=AnyUrl("https://github.com/RTimothyEdwards/magic/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-UC-export-US": CreativeWork(
        identifier="HPND-UC-export-US",
        name="Historical Permission Notice and Disclaimer - University of California, US export warning",
        url=AnyUrl("https://github.com/RTimothyEdwards/magic/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/HPND-UC-export-US.html": CreativeWork(
        identifier="HPND-UC-export-US",
        name="Historical Permission Notice and Disclaimer - University of California, US export warning",
        url=AnyUrl("https://github.com/RTimothyEdwards/magic/blob/master/LICENSE"),
    ),  # type: ignore
    "https://github.com/RTimothyEdwards/magic/blob/master/LICENSE": CreativeWork(
        identifier="HPND-UC-export-US",
        name="Historical Permission Notice and Disclaimer - University of California, US export warning",
        url=AnyUrl("https://github.com/RTimothyEdwards/magic/blob/master/LICENSE"),
    ),  # type: ignore
    "HTMLTIDY": CreativeWork(
        identifier="HTMLTIDY",
        name="HTML Tidy License",
        url=AnyUrl("https://github.com/htacg/tidy-html5/blob/next/README/LICENSE.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/HTMLTIDY": CreativeWork(
        identifier="HTMLTIDY",
        name="HTML Tidy License",
        url=AnyUrl("https://github.com/htacg/tidy-html5/blob/next/README/LICENSE.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/HTMLTIDY.html": CreativeWork(
        identifier="HTMLTIDY",
        name="HTML Tidy License",
        url=AnyUrl("https://github.com/htacg/tidy-html5/blob/next/README/LICENSE.md"),
    ),  # type: ignore
    "https://github.com/htacg/tidy-html5/blob/next/README/LICENSE.md": CreativeWork(
        identifier="HTMLTIDY",
        name="HTML Tidy License",
        url=AnyUrl("https://github.com/htacg/tidy-html5/blob/next/README/LICENSE.md"),
    ),  # type: ignore
    "hyphen-bulgarian": CreativeWork(
        identifier="hyphen-bulgarian",
        name="hyphen-bulgarian License",
        url=AnyUrl(
            "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-bulgarian.tar.xz"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/hyphen-bulgarian": CreativeWork(
        identifier="hyphen-bulgarian",
        name="hyphen-bulgarian License",
        url=AnyUrl(
            "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-bulgarian.tar.xz"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/hyphen-bulgarian.html": CreativeWork(
        identifier="hyphen-bulgarian",
        name="hyphen-bulgarian License",
        url=AnyUrl(
            "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-bulgarian.tar.xz"
        ),
    ),  # type: ignore
    "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-bulgarian.tar.xz": CreativeWork(
        identifier="hyphen-bulgarian",
        name="hyphen-bulgarian License",
        url=AnyUrl(
            "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hyphen-bulgarian.tar.xz"
        ),
    ),  # type: ignore
    "IBM-pibs": CreativeWork(
        identifier="IBM-pibs",
        name="IBM PowerPC Initialization and Boot Software",
        url=AnyUrl(
            "http://git.denx.de/?p=u-boot.git;a=blob;f=arch/powerpc/cpu/ppc4xx/miiphy.c;h=297155fdafa064b955e53e9832de93bfb0cfb85b;hb=9fab4bf4cc077c21e43941866f3f2c196f28670d"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/IBM-pibs": CreativeWork(
        identifier="IBM-pibs",
        name="IBM PowerPC Initialization and Boot Software",
        url=AnyUrl(
            "http://git.denx.de/?p=u-boot.git;a=blob;f=arch/powerpc/cpu/ppc4xx/miiphy.c;h=297155fdafa064b955e53e9832de93bfb0cfb85b;hb=9fab4bf4cc077c21e43941866f3f2c196f28670d"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/IBM-pibs.html": CreativeWork(
        identifier="IBM-pibs",
        name="IBM PowerPC Initialization and Boot Software",
        url=AnyUrl(
            "http://git.denx.de/?p=u-boot.git;a=blob;f=arch/powerpc/cpu/ppc4xx/miiphy.c;h=297155fdafa064b955e53e9832de93bfb0cfb85b;hb=9fab4bf4cc077c21e43941866f3f2c196f28670d"
        ),
    ),  # type: ignore
    "http://git.denx.de/?p=u-boot.git;a=blob;f=arch/powerpc/cpu/ppc4xx/miiphy.c;h=297155fdafa064b955e53e9832de93bfb0cfb85b;hb=9fab4bf4cc077c21e43941866f3f2c196f28670d": CreativeWork(
        identifier="IBM-pibs",
        name="IBM PowerPC Initialization and Boot Software",
        url=AnyUrl(
            "http://git.denx.de/?p=u-boot.git;a=blob;f=arch/powerpc/cpu/ppc4xx/miiphy.c;h=297155fdafa064b955e53e9832de93bfb0cfb85b;hb=9fab4bf4cc077c21e43941866f3f2c196f28670d"
        ),
    ),  # type: ignore
    "ICU": CreativeWork(
        identifier="ICU",
        name="ICU License",
        url=AnyUrl("http://source.icu-project.org/repos/icu/icu/trunk/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/ICU": CreativeWork(
        identifier="ICU",
        name="ICU License",
        url=AnyUrl("http://source.icu-project.org/repos/icu/icu/trunk/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/ICU.html": CreativeWork(
        identifier="ICU",
        name="ICU License",
        url=AnyUrl("http://source.icu-project.org/repos/icu/icu/trunk/license.html"),
    ),  # type: ignore
    "http://source.icu-project.org/repos/icu/icu/trunk/license.html": CreativeWork(
        identifier="ICU",
        name="ICU License",
        url=AnyUrl("http://source.icu-project.org/repos/icu/icu/trunk/license.html"),
    ),  # type: ignore
    "IEC-Code-Components-EULA": CreativeWork(
        identifier="IEC-Code-Components-EULA",
        name="IEC    Code Components End-user licence agreement",
        url=AnyUrl("https://www.iec.ch/webstore/custserv/pdf/CC-EULA.pdf"),
    ),  # type: ignore
    "https://spdx.org/licenses/IEC-Code-Components-EULA": CreativeWork(
        identifier="IEC-Code-Components-EULA",
        name="IEC    Code Components End-user licence agreement",
        url=AnyUrl("https://www.iec.ch/webstore/custserv/pdf/CC-EULA.pdf"),
    ),  # type: ignore
    "https://spdx.org/licenses/IEC-Code-Components-EULA.html": CreativeWork(
        identifier="IEC-Code-Components-EULA",
        name="IEC    Code Components End-user licence agreement",
        url=AnyUrl("https://www.iec.ch/webstore/custserv/pdf/CC-EULA.pdf"),
    ),  # type: ignore
    "https://www.iec.ch/webstore/custserv/pdf/CC-EULA.pdf": CreativeWork(
        identifier="IEC-Code-Components-EULA",
        name="IEC    Code Components End-user licence agreement",
        url=AnyUrl("https://www.iec.ch/webstore/custserv/pdf/CC-EULA.pdf"),
    ),  # type: ignore
    "IJG": CreativeWork(
        identifier="IJG",
        name="Independent JPEG Group License",
        url=AnyUrl("http://dev.w3.org/cvsweb/Amaya/libjpeg/Attic/README?rev=1.2"),
    ),  # type: ignore
    "https://spdx.org/licenses/IJG": CreativeWork(
        identifier="IJG",
        name="Independent JPEG Group License",
        url=AnyUrl("http://dev.w3.org/cvsweb/Amaya/libjpeg/Attic/README?rev=1.2"),
    ),  # type: ignore
    "https://spdx.org/licenses/IJG.html": CreativeWork(
        identifier="IJG",
        name="Independent JPEG Group License",
        url=AnyUrl("http://dev.w3.org/cvsweb/Amaya/libjpeg/Attic/README?rev=1.2"),
    ),  # type: ignore
    "http://dev.w3.org/cvsweb/Amaya/libjpeg/Attic/README?rev=1.2": CreativeWork(
        identifier="IJG",
        name="Independent JPEG Group License",
        url=AnyUrl("http://dev.w3.org/cvsweb/Amaya/libjpeg/Attic/README?rev=1.2"),
    ),  # type: ignore
    "IJG-short": CreativeWork(
        identifier="IJG-short",
        name="Independent JPEG Group License - short",
        url=AnyUrl("https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/ljpg/"),
    ),  # type: ignore
    "https://spdx.org/licenses/IJG-short": CreativeWork(
        identifier="IJG-short",
        name="Independent JPEG Group License - short",
        url=AnyUrl("https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/ljpg/"),
    ),  # type: ignore
    "https://spdx.org/licenses/IJG-short.html": CreativeWork(
        identifier="IJG-short",
        name="Independent JPEG Group License - short",
        url=AnyUrl("https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/ljpg/"),
    ),  # type: ignore
    "https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/ljpg/": CreativeWork(
        identifier="IJG-short",
        name="Independent JPEG Group License - short",
        url=AnyUrl("https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/ljpg/"),
    ),  # type: ignore
    "ImageMagick": CreativeWork(
        identifier="ImageMagick",
        name="ImageMagick License",
        url=AnyUrl("http://www.imagemagick.org/script/license.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/ImageMagick": CreativeWork(
        identifier="ImageMagick",
        name="ImageMagick License",
        url=AnyUrl("http://www.imagemagick.org/script/license.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/ImageMagick.html": CreativeWork(
        identifier="ImageMagick",
        name="ImageMagick License",
        url=AnyUrl("http://www.imagemagick.org/script/license.php"),
    ),  # type: ignore
    "http://www.imagemagick.org/script/license.php": CreativeWork(
        identifier="ImageMagick",
        name="ImageMagick License",
        url=AnyUrl("http://www.imagemagick.org/script/license.php"),
    ),  # type: ignore
    "iMatix": CreativeWork(
        identifier="iMatix",
        name="iMatix Standard Function Library Agreement",
        url=AnyUrl("http://legacy.imatix.com/html/sfl/sfl4.htm#license"),
    ),  # type: ignore
    "https://spdx.org/licenses/iMatix": CreativeWork(
        identifier="iMatix",
        name="iMatix Standard Function Library Agreement",
        url=AnyUrl("http://legacy.imatix.com/html/sfl/sfl4.htm#license"),
    ),  # type: ignore
    "https://spdx.org/licenses/iMatix.html": CreativeWork(
        identifier="iMatix",
        name="iMatix Standard Function Library Agreement",
        url=AnyUrl("http://legacy.imatix.com/html/sfl/sfl4.htm#license"),
    ),  # type: ignore
    "http://legacy.imatix.com/html/sfl/sfl4.htm#license": CreativeWork(
        identifier="iMatix",
        name="iMatix Standard Function Library Agreement",
        url=AnyUrl("http://legacy.imatix.com/html/sfl/sfl4.htm#license"),
    ),  # type: ignore
    "Imlib2": CreativeWork(
        identifier="Imlib2",
        name="Imlib2 License",
        url=AnyUrl("http://trac.enlightenment.org/e/browser/trunk/imlib2/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/Imlib2": CreativeWork(
        identifier="Imlib2",
        name="Imlib2 License",
        url=AnyUrl("http://trac.enlightenment.org/e/browser/trunk/imlib2/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/Imlib2.html": CreativeWork(
        identifier="Imlib2",
        name="Imlib2 License",
        url=AnyUrl("http://trac.enlightenment.org/e/browser/trunk/imlib2/COPYING"),
    ),  # type: ignore
    "http://trac.enlightenment.org/e/browser/trunk/imlib2/COPYING": CreativeWork(
        identifier="Imlib2",
        name="Imlib2 License",
        url=AnyUrl("http://trac.enlightenment.org/e/browser/trunk/imlib2/COPYING"),
    ),  # type: ignore
    "Info-ZIP": CreativeWork(
        identifier="Info-ZIP",
        name="Info-ZIP License",
        url=AnyUrl("http://www.info-zip.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Info-ZIP": CreativeWork(
        identifier="Info-ZIP",
        name="Info-ZIP License",
        url=AnyUrl("http://www.info-zip.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Info-ZIP.html": CreativeWork(
        identifier="Info-ZIP",
        name="Info-ZIP License",
        url=AnyUrl("http://www.info-zip.org/license.html"),
    ),  # type: ignore
    "http://www.info-zip.org/license.html": CreativeWork(
        identifier="Info-ZIP",
        name="Info-ZIP License",
        url=AnyUrl("http://www.info-zip.org/license.html"),
    ),  # type: ignore
    "Inner-Net-2.0": CreativeWork(
        identifier="Inner-Net-2.0",
        name="Inner Net License v2.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Inner_Net_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/Inner-Net-2.0": CreativeWork(
        identifier="Inner-Net-2.0",
        name="Inner Net License v2.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Inner_Net_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/Inner-Net-2.0.html": CreativeWork(
        identifier="Inner-Net-2.0",
        name="Inner Net License v2.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Inner_Net_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Inner_Net_License": CreativeWork(
        identifier="Inner-Net-2.0",
        name="Inner Net License v2.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Inner_Net_License"),
    ),  # type: ignore
    "InnoSetup": CreativeWork(
        identifier="InnoSetup",
        name="Inno Setup License",
        url=AnyUrl("https://github.com/jrsoftware/issrc/blob/HEAD/license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/InnoSetup": CreativeWork(
        identifier="InnoSetup",
        name="Inno Setup License",
        url=AnyUrl("https://github.com/jrsoftware/issrc/blob/HEAD/license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/InnoSetup.html": CreativeWork(
        identifier="InnoSetup",
        name="Inno Setup License",
        url=AnyUrl("https://github.com/jrsoftware/issrc/blob/HEAD/license.txt"),
    ),  # type: ignore
    "https://github.com/jrsoftware/issrc/blob/HEAD/license.txt": CreativeWork(
        identifier="InnoSetup",
        name="Inno Setup License",
        url=AnyUrl("https://github.com/jrsoftware/issrc/blob/HEAD/license.txt"),
    ),  # type: ignore
    "Intel": CreativeWork(
        identifier="Intel",
        name="Intel Open Source License",
        url=AnyUrl("https://opensource.org/licenses/Intel"),
    ),  # type: ignore
    "https://spdx.org/licenses/Intel": CreativeWork(
        identifier="Intel",
        name="Intel Open Source License",
        url=AnyUrl("https://opensource.org/licenses/Intel"),
    ),  # type: ignore
    "https://spdx.org/licenses/Intel.html": CreativeWork(
        identifier="Intel",
        name="Intel Open Source License",
        url=AnyUrl("https://opensource.org/licenses/Intel"),
    ),  # type: ignore
    "https://opensource.org/licenses/Intel": CreativeWork(
        identifier="Intel",
        name="Intel Open Source License",
        url=AnyUrl("https://opensource.org/licenses/Intel"),
    ),  # type: ignore
    "Intel-ACPI": CreativeWork(
        identifier="Intel-ACPI",
        name="Intel ACPI Software License Agreement",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Intel_ACPI_Software_License_Agreement"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Intel-ACPI": CreativeWork(
        identifier="Intel-ACPI",
        name="Intel ACPI Software License Agreement",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Intel_ACPI_Software_License_Agreement"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Intel-ACPI.html": CreativeWork(
        identifier="Intel-ACPI",
        name="Intel ACPI Software License Agreement",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Intel_ACPI_Software_License_Agreement"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Intel_ACPI_Software_License_Agreement": CreativeWork(
        identifier="Intel-ACPI",
        name="Intel ACPI Software License Agreement",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Intel_ACPI_Software_License_Agreement"
        ),
    ),  # type: ignore
    "Interbase-1.0": CreativeWork(
        identifier="Interbase-1.0",
        name="Interbase Public License v1.0",
        url=AnyUrl(
            "https://web.archive.org/web/20060319014854/http://info.borland.com/devsupport/interbase/opensource/IPL.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Interbase-1.0": CreativeWork(
        identifier="Interbase-1.0",
        name="Interbase Public License v1.0",
        url=AnyUrl(
            "https://web.archive.org/web/20060319014854/http://info.borland.com/devsupport/interbase/opensource/IPL.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Interbase-1.0.html": CreativeWork(
        identifier="Interbase-1.0",
        name="Interbase Public License v1.0",
        url=AnyUrl(
            "https://web.archive.org/web/20060319014854/http://info.borland.com/devsupport/interbase/opensource/IPL.html"
        ),
    ),  # type: ignore
    "https://web.archive.org/web/20060319014854/http://info.borland.com/devsupport/interbase/opensource/IPL.html": CreativeWork(
        identifier="Interbase-1.0",
        name="Interbase Public License v1.0",
        url=AnyUrl(
            "https://web.archive.org/web/20060319014854/http://info.borland.com/devsupport/interbase/opensource/IPL.html"
        ),
    ),  # type: ignore
    "IPA": CreativeWork(
        identifier="IPA",
        name="IPA Font License",
        url=AnyUrl("https://opensource.org/licenses/IPA"),
    ),  # type: ignore
    "https://spdx.org/licenses/IPA": CreativeWork(
        identifier="IPA",
        name="IPA Font License",
        url=AnyUrl("https://opensource.org/licenses/IPA"),
    ),  # type: ignore
    "https://spdx.org/licenses/IPA.html": CreativeWork(
        identifier="IPA",
        name="IPA Font License",
        url=AnyUrl("https://opensource.org/licenses/IPA"),
    ),  # type: ignore
    "https://opensource.org/licenses/IPA": CreativeWork(
        identifier="IPA",
        name="IPA Font License",
        url=AnyUrl("https://opensource.org/licenses/IPA"),
    ),  # type: ignore
    "IPL-1.0": CreativeWork(
        identifier="IPL-1.0",
        name="IBM Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/IPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/IPL-1.0": CreativeWork(
        identifier="IPL-1.0",
        name="IBM Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/IPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/IPL-1.0.html": CreativeWork(
        identifier="IPL-1.0",
        name="IBM Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/IPL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/IPL-1.0": CreativeWork(
        identifier="IPL-1.0",
        name="IBM Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/IPL-1.0"),
    ),  # type: ignore
    "ISC": CreativeWork(
        identifier="ISC",
        name="ISC License",
        url=AnyUrl("https://www.isc.org/licenses/"),
    ),  # type: ignore
    "https://spdx.org/licenses/ISC": CreativeWork(
        identifier="ISC",
        name="ISC License",
        url=AnyUrl("https://www.isc.org/licenses/"),
    ),  # type: ignore
    "https://spdx.org/licenses/ISC.html": CreativeWork(
        identifier="ISC",
        name="ISC License",
        url=AnyUrl("https://www.isc.org/licenses/"),
    ),  # type: ignore
    "https://www.isc.org/licenses/": CreativeWork(
        identifier="ISC",
        name="ISC License",
        url=AnyUrl("https://www.isc.org/licenses/"),
    ),  # type: ignore
    "ISC-Veillard": CreativeWork(
        identifier="ISC-Veillard",
        name="ISC Veillard variant",
        url=AnyUrl(
            "https://raw.githubusercontent.com/GNOME/libxml2/4c2e7c651f6c2f0d1a74f350cbda95f7df3e7017/hash.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ISC-Veillard": CreativeWork(
        identifier="ISC-Veillard",
        name="ISC Veillard variant",
        url=AnyUrl(
            "https://raw.githubusercontent.com/GNOME/libxml2/4c2e7c651f6c2f0d1a74f350cbda95f7df3e7017/hash.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ISC-Veillard.html": CreativeWork(
        identifier="ISC-Veillard",
        name="ISC Veillard variant",
        url=AnyUrl(
            "https://raw.githubusercontent.com/GNOME/libxml2/4c2e7c651f6c2f0d1a74f350cbda95f7df3e7017/hash.c"
        ),
    ),  # type: ignore
    "https://raw.githubusercontent.com/GNOME/libxml2/4c2e7c651f6c2f0d1a74f350cbda95f7df3e7017/hash.c": CreativeWork(
        identifier="ISC-Veillard",
        name="ISC Veillard variant",
        url=AnyUrl(
            "https://raw.githubusercontent.com/GNOME/libxml2/4c2e7c651f6c2f0d1a74f350cbda95f7df3e7017/hash.c"
        ),
    ),  # type: ignore
    "ISO-permission": CreativeWork(
        identifier="ISO-permission",
        name="ISO permission notice",
        url=AnyUrl(
            "https://gitlab.com/agmartin/linuxdoc-tools/-/blob/master/iso-entities/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ISO-permission": CreativeWork(
        identifier="ISO-permission",
        name="ISO permission notice",
        url=AnyUrl(
            "https://gitlab.com/agmartin/linuxdoc-tools/-/blob/master/iso-entities/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ISO-permission.html": CreativeWork(
        identifier="ISO-permission",
        name="ISO permission notice",
        url=AnyUrl(
            "https://gitlab.com/agmartin/linuxdoc-tools/-/blob/master/iso-entities/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://gitlab.com/agmartin/linuxdoc-tools/-/blob/master/iso-entities/COPYING?ref_type=heads": CreativeWork(
        identifier="ISO-permission",
        name="ISO permission notice",
        url=AnyUrl(
            "https://gitlab.com/agmartin/linuxdoc-tools/-/blob/master/iso-entities/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "Jam": CreativeWork(
        identifier="Jam",
        name="Jam License",
        url=AnyUrl("https://www.boost.org/doc/libs/1_35_0/doc/html/jam.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Jam": CreativeWork(
        identifier="Jam",
        name="Jam License",
        url=AnyUrl("https://www.boost.org/doc/libs/1_35_0/doc/html/jam.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Jam.html": CreativeWork(
        identifier="Jam",
        name="Jam License",
        url=AnyUrl("https://www.boost.org/doc/libs/1_35_0/doc/html/jam.html"),
    ),  # type: ignore
    "https://www.boost.org/doc/libs/1_35_0/doc/html/jam.html": CreativeWork(
        identifier="Jam",
        name="Jam License",
        url=AnyUrl("https://www.boost.org/doc/libs/1_35_0/doc/html/jam.html"),
    ),  # type: ignore
    "JasPer-2.0": CreativeWork(
        identifier="JasPer-2.0",
        name="JasPer License",
        url=AnyUrl("http://www.ece.uvic.ca/~mdadams/jasper/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/JasPer-2.0": CreativeWork(
        identifier="JasPer-2.0",
        name="JasPer License",
        url=AnyUrl("http://www.ece.uvic.ca/~mdadams/jasper/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/JasPer-2.0.html": CreativeWork(
        identifier="JasPer-2.0",
        name="JasPer License",
        url=AnyUrl("http://www.ece.uvic.ca/~mdadams/jasper/LICENSE"),
    ),  # type: ignore
    "http://www.ece.uvic.ca/~mdadams/jasper/LICENSE": CreativeWork(
        identifier="JasPer-2.0",
        name="JasPer License",
        url=AnyUrl("http://www.ece.uvic.ca/~mdadams/jasper/LICENSE"),
    ),  # type: ignore
    "jove": CreativeWork(
        identifier="jove",
        name="Jove License",
        url=AnyUrl("https://github.com/jonmacs/jove/blob/4_17/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/jove": CreativeWork(
        identifier="jove",
        name="Jove License",
        url=AnyUrl("https://github.com/jonmacs/jove/blob/4_17/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/jove.html": CreativeWork(
        identifier="jove",
        name="Jove License",
        url=AnyUrl("https://github.com/jonmacs/jove/blob/4_17/LICENSE"),
    ),  # type: ignore
    "https://github.com/jonmacs/jove/blob/4_17/LICENSE": CreativeWork(
        identifier="jove",
        name="Jove License",
        url=AnyUrl("https://github.com/jonmacs/jove/blob/4_17/LICENSE"),
    ),  # type: ignore
    "JPL-image": CreativeWork(
        identifier="JPL-image",
        name="JPL Image Use Policy",
        url=AnyUrl("https://www.jpl.nasa.gov/jpl-image-use-policy"),
    ),  # type: ignore
    "https://spdx.org/licenses/JPL-image": CreativeWork(
        identifier="JPL-image",
        name="JPL Image Use Policy",
        url=AnyUrl("https://www.jpl.nasa.gov/jpl-image-use-policy"),
    ),  # type: ignore
    "https://spdx.org/licenses/JPL-image.html": CreativeWork(
        identifier="JPL-image",
        name="JPL Image Use Policy",
        url=AnyUrl("https://www.jpl.nasa.gov/jpl-image-use-policy"),
    ),  # type: ignore
    "https://www.jpl.nasa.gov/jpl-image-use-policy": CreativeWork(
        identifier="JPL-image",
        name="JPL Image Use Policy",
        url=AnyUrl("https://www.jpl.nasa.gov/jpl-image-use-policy"),
    ),  # type: ignore
    "JPNIC": CreativeWork(
        identifier="JPNIC",
        name="Japan Network Information Center License",
        url=AnyUrl(
            "https://gitlab.isc.org/isc-projects/bind9/blob/master/COPYRIGHT#L366"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/JPNIC": CreativeWork(
        identifier="JPNIC",
        name="Japan Network Information Center License",
        url=AnyUrl(
            "https://gitlab.isc.org/isc-projects/bind9/blob/master/COPYRIGHT#L366"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/JPNIC.html": CreativeWork(
        identifier="JPNIC",
        name="Japan Network Information Center License",
        url=AnyUrl(
            "https://gitlab.isc.org/isc-projects/bind9/blob/master/COPYRIGHT#L366"
        ),
    ),  # type: ignore
    "https://gitlab.isc.org/isc-projects/bind9/blob/master/COPYRIGHT#L366": CreativeWork(
        identifier="JPNIC",
        name="Japan Network Information Center License",
        url=AnyUrl(
            "https://gitlab.isc.org/isc-projects/bind9/blob/master/COPYRIGHT#L366"
        ),
    ),  # type: ignore
    "JSON": CreativeWork(
        identifier="JSON",
        name="JSON License",
        url=AnyUrl("http://www.json.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/JSON": CreativeWork(
        identifier="JSON",
        name="JSON License",
        url=AnyUrl("http://www.json.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/JSON.html": CreativeWork(
        identifier="JSON",
        name="JSON License",
        url=AnyUrl("http://www.json.org/license.html"),
    ),  # type: ignore
    "http://www.json.org/license.html": CreativeWork(
        identifier="JSON",
        name="JSON License",
        url=AnyUrl("http://www.json.org/license.html"),
    ),  # type: ignore
    "Kastrup": CreativeWork(
        identifier="Kastrup",
        name="Kastrup License",
        url=AnyUrl(
            "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/kastrup/binhex.dtx"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Kastrup": CreativeWork(
        identifier="Kastrup",
        name="Kastrup License",
        url=AnyUrl(
            "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/kastrup/binhex.dtx"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Kastrup.html": CreativeWork(
        identifier="Kastrup",
        name="Kastrup License",
        url=AnyUrl(
            "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/kastrup/binhex.dtx"
        ),
    ),  # type: ignore
    "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/kastrup/binhex.dtx": CreativeWork(
        identifier="Kastrup",
        name="Kastrup License",
        url=AnyUrl(
            "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/kastrup/binhex.dtx"
        ),
    ),  # type: ignore
    "Kazlib": CreativeWork(
        identifier="Kazlib",
        name="Kazlib License",
        url=AnyUrl(
            "http://git.savannah.gnu.org/cgit/kazlib.git/tree/except.c?id=0062df360c2d17d57f6af19b0e444c51feb99036"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Kazlib": CreativeWork(
        identifier="Kazlib",
        name="Kazlib License",
        url=AnyUrl(
            "http://git.savannah.gnu.org/cgit/kazlib.git/tree/except.c?id=0062df360c2d17d57f6af19b0e444c51feb99036"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Kazlib.html": CreativeWork(
        identifier="Kazlib",
        name="Kazlib License",
        url=AnyUrl(
            "http://git.savannah.gnu.org/cgit/kazlib.git/tree/except.c?id=0062df360c2d17d57f6af19b0e444c51feb99036"
        ),
    ),  # type: ignore
    "http://git.savannah.gnu.org/cgit/kazlib.git/tree/except.c?id=0062df360c2d17d57f6af19b0e444c51feb99036": CreativeWork(
        identifier="Kazlib",
        name="Kazlib License",
        url=AnyUrl(
            "http://git.savannah.gnu.org/cgit/kazlib.git/tree/except.c?id=0062df360c2d17d57f6af19b0e444c51feb99036"
        ),
    ),  # type: ignore
    "Knuth-CTAN": CreativeWork(
        identifier="Knuth-CTAN",
        name="Knuth CTAN License",
        url=AnyUrl("https://ctan.org/license/knuth"),
    ),  # type: ignore
    "https://spdx.org/licenses/Knuth-CTAN": CreativeWork(
        identifier="Knuth-CTAN",
        name="Knuth CTAN License",
        url=AnyUrl("https://ctan.org/license/knuth"),
    ),  # type: ignore
    "https://spdx.org/licenses/Knuth-CTAN.html": CreativeWork(
        identifier="Knuth-CTAN",
        name="Knuth CTAN License",
        url=AnyUrl("https://ctan.org/license/knuth"),
    ),  # type: ignore
    "https://ctan.org/license/knuth": CreativeWork(
        identifier="Knuth-CTAN",
        name="Knuth CTAN License",
        url=AnyUrl("https://ctan.org/license/knuth"),
    ),  # type: ignore
    "LAL-1.2": CreativeWork(
        identifier="LAL-1.2",
        name="Licence Art Libre 1.2",
        url=AnyUrl("http://artlibre.org/licence/lal/licence-art-libre-12/"),
    ),  # type: ignore
    "https://spdx.org/licenses/LAL-1.2": CreativeWork(
        identifier="LAL-1.2",
        name="Licence Art Libre 1.2",
        url=AnyUrl("http://artlibre.org/licence/lal/licence-art-libre-12/"),
    ),  # type: ignore
    "https://spdx.org/licenses/LAL-1.2.html": CreativeWork(
        identifier="LAL-1.2",
        name="Licence Art Libre 1.2",
        url=AnyUrl("http://artlibre.org/licence/lal/licence-art-libre-12/"),
    ),  # type: ignore
    "http://artlibre.org/licence/lal/licence-art-libre-12/": CreativeWork(
        identifier="LAL-1.2",
        name="Licence Art Libre 1.2",
        url=AnyUrl("http://artlibre.org/licence/lal/licence-art-libre-12/"),
    ),  # type: ignore
    "LAL-1.3": CreativeWork(
        identifier="LAL-1.3",
        name="Licence Art Libre 1.3",
        url=AnyUrl("https://artlibre.org/"),
    ),  # type: ignore
    "https://spdx.org/licenses/LAL-1.3": CreativeWork(
        identifier="LAL-1.3",
        name="Licence Art Libre 1.3",
        url=AnyUrl("https://artlibre.org/"),
    ),  # type: ignore
    "https://spdx.org/licenses/LAL-1.3.html": CreativeWork(
        identifier="LAL-1.3",
        name="Licence Art Libre 1.3",
        url=AnyUrl("https://artlibre.org/"),
    ),  # type: ignore
    "https://artlibre.org/": CreativeWork(
        identifier="LAL-1.3",
        name="Licence Art Libre 1.3",
        url=AnyUrl("https://artlibre.org/"),
    ),  # type: ignore
    "Latex2e": CreativeWork(
        identifier="Latex2e",
        name="Latex2e License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Latex2e"),
    ),  # type: ignore
    "https://spdx.org/licenses/Latex2e": CreativeWork(
        identifier="Latex2e",
        name="Latex2e License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Latex2e"),
    ),  # type: ignore
    "https://spdx.org/licenses/Latex2e.html": CreativeWork(
        identifier="Latex2e",
        name="Latex2e License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Latex2e"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Latex2e": CreativeWork(
        identifier="Latex2e",
        name="Latex2e License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Latex2e"),
    ),  # type: ignore
    "Latex2e-translated-notice": CreativeWork(
        identifier="Latex2e-translated-notice",
        name="Latex2e with translated notice permission",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/indent.git/tree/doc/indent.texi?id=a74c6b4ee49397cf330b333da1042bffa60ed14f#n74"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Latex2e-translated-notice": CreativeWork(
        identifier="Latex2e-translated-notice",
        name="Latex2e with translated notice permission",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/indent.git/tree/doc/indent.texi?id=a74c6b4ee49397cf330b333da1042bffa60ed14f#n74"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Latex2e-translated-notice.html": CreativeWork(
        identifier="Latex2e-translated-notice",
        name="Latex2e with translated notice permission",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/indent.git/tree/doc/indent.texi?id=a74c6b4ee49397cf330b333da1042bffa60ed14f#n74"
        ),
    ),  # type: ignore
    "https://git.savannah.gnu.org/cgit/indent.git/tree/doc/indent.texi?id=a74c6b4ee49397cf330b333da1042bffa60ed14f#n74": CreativeWork(
        identifier="Latex2e-translated-notice",
        name="Latex2e with translated notice permission",
        url=AnyUrl(
            "https://git.savannah.gnu.org/cgit/indent.git/tree/doc/indent.texi?id=a74c6b4ee49397cf330b333da1042bffa60ed14f#n74"
        ),
    ),  # type: ignore
    "Leptonica": CreativeWork(
        identifier="Leptonica",
        name="Leptonica License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Leptonica"),
    ),  # type: ignore
    "https://spdx.org/licenses/Leptonica": CreativeWork(
        identifier="Leptonica",
        name="Leptonica License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Leptonica"),
    ),  # type: ignore
    "https://spdx.org/licenses/Leptonica.html": CreativeWork(
        identifier="Leptonica",
        name="Leptonica License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Leptonica"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Leptonica": CreativeWork(
        identifier="Leptonica",
        name="Leptonica License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Leptonica"),
    ),  # type: ignore
    "LGPL-2.0": CreativeWork(
        identifier="LGPL-2.0",
        name="GNU Library General Public License v2 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.0": CreativeWork(
        identifier="LGPL-2.0",
        name="GNU Library General Public License v2 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.0.html": CreativeWork(
        identifier="LGPL-2.0",
        name="GNU Library General Public License v2 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html": CreativeWork(
        identifier="LGPL-2.0",
        name="GNU Library General Public License v2 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "LGPL-2.0+": CreativeWork(
        identifier="LGPL-2.0+",
        name="GNU Library General Public License v2 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.0+": CreativeWork(
        identifier="LGPL-2.0+",
        name="GNU Library General Public License v2 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.0+.html": CreativeWork(
        identifier="LGPL-2.0+",
        name="GNU Library General Public License v2 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "LGPL-2.0-only": CreativeWork(
        identifier="LGPL-2.0-only",
        name="GNU Library General Public License v2 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.0-only": CreativeWork(
        identifier="LGPL-2.0-only",
        name="GNU Library General Public License v2 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.0-only.html": CreativeWork(
        identifier="LGPL-2.0-only",
        name="GNU Library General Public License v2 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "LGPL-2.0-or-later": CreativeWork(
        identifier="LGPL-2.0-or-later",
        name="GNU Library General Public License v2 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.0-or-later": CreativeWork(
        identifier="LGPL-2.0-or-later",
        name="GNU Library General Public License v2 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.0-or-later.html": CreativeWork(
        identifier="LGPL-2.0-or-later",
        name="GNU Library General Public License v2 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html"
        ),
    ),  # type: ignore
    "LGPL-2.1": CreativeWork(
        identifier="LGPL-2.1",
        name="GNU Lesser General Public License v2.1 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.1": CreativeWork(
        identifier="LGPL-2.1",
        name="GNU Lesser General Public License v2.1 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.1.html": CreativeWork(
        identifier="LGPL-2.1",
        name="GNU Lesser General Public License v2.1 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html": CreativeWork(
        identifier="LGPL-2.1",
        name="GNU Lesser General Public License v2.1 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "LGPL-2.1+": CreativeWork(
        identifier="LGPL-2.1+",
        name="GNU Lesser General Public License v2.1 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.1+": CreativeWork(
        identifier="LGPL-2.1+",
        name="GNU Lesser General Public License v2.1 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.1+.html": CreativeWork(
        identifier="LGPL-2.1+",
        name="GNU Lesser General Public License v2.1 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "LGPL-2.1-only": CreativeWork(
        identifier="LGPL-2.1-only",
        name="GNU Lesser General Public License v2.1 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.1-only": CreativeWork(
        identifier="LGPL-2.1-only",
        name="GNU Lesser General Public License v2.1 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.1-only.html": CreativeWork(
        identifier="LGPL-2.1-only",
        name="GNU Lesser General Public License v2.1 only",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "LGPL-2.1-or-later": CreativeWork(
        identifier="LGPL-2.1-or-later",
        name="GNU Lesser General Public License v2.1 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.1-or-later": CreativeWork(
        identifier="LGPL-2.1-or-later",
        name="GNU Lesser General Public License v2.1 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-2.1-or-later.html": CreativeWork(
        identifier="LGPL-2.1-or-later",
        name="GNU Lesser General Public License v2.1 or later",
        url=AnyUrl(
            "https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html"
        ),
    ),  # type: ignore
    "LGPL-3.0": CreativeWork(
        identifier="LGPL-3.0",
        name="GNU Lesser General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-3.0": CreativeWork(
        identifier="LGPL-3.0",
        name="GNU Lesser General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-3.0.html": CreativeWork(
        identifier="LGPL-3.0",
        name="GNU Lesser General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://www.gnu.org/licenses/lgpl-3.0-standalone.html": CreativeWork(
        identifier="LGPL-3.0",
        name="GNU Lesser General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "LGPL-3.0+": CreativeWork(
        identifier="LGPL-3.0+",
        name="GNU Lesser General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-3.0+": CreativeWork(
        identifier="LGPL-3.0+",
        name="GNU Lesser General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-3.0+.html": CreativeWork(
        identifier="LGPL-3.0+",
        name="GNU Lesser General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "LGPL-3.0-only": CreativeWork(
        identifier="LGPL-3.0-only",
        name="GNU Lesser General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-3.0-only": CreativeWork(
        identifier="LGPL-3.0-only",
        name="GNU Lesser General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-3.0-only.html": CreativeWork(
        identifier="LGPL-3.0-only",
        name="GNU Lesser General Public License v3.0 only",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "LGPL-3.0-or-later": CreativeWork(
        identifier="LGPL-3.0-or-later",
        name="GNU Lesser General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-3.0-or-later": CreativeWork(
        identifier="LGPL-3.0-or-later",
        name="GNU Lesser General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPL-3.0-or-later.html": CreativeWork(
        identifier="LGPL-3.0-or-later",
        name="GNU Lesser General Public License v3.0 or later",
        url=AnyUrl("https://www.gnu.org/licenses/lgpl-3.0-standalone.html"),
    ),  # type: ignore
    "LGPLLR": CreativeWork(
        identifier="LGPLLR",
        name="Lesser General Public License For Linguistic Resources",
        url=AnyUrl("http://www-igm.univ-mlv.fr/~unitex/lgpllr.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPLLR": CreativeWork(
        identifier="LGPLLR",
        name="Lesser General Public License For Linguistic Resources",
        url=AnyUrl("http://www-igm.univ-mlv.fr/~unitex/lgpllr.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LGPLLR.html": CreativeWork(
        identifier="LGPLLR",
        name="Lesser General Public License For Linguistic Resources",
        url=AnyUrl("http://www-igm.univ-mlv.fr/~unitex/lgpllr.html"),
    ),  # type: ignore
    "http://www-igm.univ-mlv.fr/~unitex/lgpllr.html": CreativeWork(
        identifier="LGPLLR",
        name="Lesser General Public License For Linguistic Resources",
        url=AnyUrl("http://www-igm.univ-mlv.fr/~unitex/lgpllr.html"),
    ),  # type: ignore
    "Libpng": CreativeWork(
        identifier="Libpng",
        name="libpng License",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Libpng": CreativeWork(
        identifier="Libpng",
        name="libpng License",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Libpng.html": CreativeWork(
        identifier="Libpng",
        name="libpng License",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "http://www.libpng.org/pub/png/src/libpng-LICENSE.txt": CreativeWork(
        identifier="Libpng",
        name="libpng License",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "libpng-1.6.35": CreativeWork(
        identifier="libpng-1.6.35",
        name="PNG Reference Library License v1 (for libpng 0.5 through 1.6.35)",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/libpng-1.6.35": CreativeWork(
        identifier="libpng-1.6.35",
        name="PNG Reference Library License v1 (for libpng 0.5 through 1.6.35)",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/libpng-1.6.35.html": CreativeWork(
        identifier="libpng-1.6.35",
        name="PNG Reference Library License v1 (for libpng 0.5 through 1.6.35)",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "libpng-2.0": CreativeWork(
        identifier="libpng-2.0",
        name="PNG Reference Library version 2",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/libpng-2.0": CreativeWork(
        identifier="libpng-2.0",
        name="PNG Reference Library version 2",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/libpng-2.0.html": CreativeWork(
        identifier="libpng-2.0",
        name="PNG Reference Library version 2",
        url=AnyUrl("http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"),
    ),  # type: ignore
    "libselinux-1.0": CreativeWork(
        identifier="libselinux-1.0",
        name="libselinux public domain notice",
        url=AnyUrl(
            "https://github.com/SELinuxProject/selinux/blob/master/libselinux/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/libselinux-1.0": CreativeWork(
        identifier="libselinux-1.0",
        name="libselinux public domain notice",
        url=AnyUrl(
            "https://github.com/SELinuxProject/selinux/blob/master/libselinux/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/libselinux-1.0.html": CreativeWork(
        identifier="libselinux-1.0",
        name="libselinux public domain notice",
        url=AnyUrl(
            "https://github.com/SELinuxProject/selinux/blob/master/libselinux/LICENSE"
        ),
    ),  # type: ignore
    "https://github.com/SELinuxProject/selinux/blob/master/libselinux/LICENSE": CreativeWork(
        identifier="libselinux-1.0",
        name="libselinux public domain notice",
        url=AnyUrl(
            "https://github.com/SELinuxProject/selinux/blob/master/libselinux/LICENSE"
        ),
    ),  # type: ignore
    "libtiff": CreativeWork(
        identifier="libtiff",
        name="libtiff License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/libtiff"),
    ),  # type: ignore
    "https://spdx.org/licenses/libtiff": CreativeWork(
        identifier="libtiff",
        name="libtiff License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/libtiff"),
    ),  # type: ignore
    "https://spdx.org/licenses/libtiff.html": CreativeWork(
        identifier="libtiff",
        name="libtiff License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/libtiff"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/libtiff": CreativeWork(
        identifier="libtiff",
        name="libtiff License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/libtiff"),
    ),  # type: ignore
    "libutil-David-Nugent": CreativeWork(
        identifier="libutil-David-Nugent",
        name="libutil David Nugent License",
        url=AnyUrl("http://web.mit.edu/freebsd/head/lib/libutil/login_ok.3"),
    ),  # type: ignore
    "https://spdx.org/licenses/libutil-David-Nugent": CreativeWork(
        identifier="libutil-David-Nugent",
        name="libutil David Nugent License",
        url=AnyUrl("http://web.mit.edu/freebsd/head/lib/libutil/login_ok.3"),
    ),  # type: ignore
    "https://spdx.org/licenses/libutil-David-Nugent.html": CreativeWork(
        identifier="libutil-David-Nugent",
        name="libutil David Nugent License",
        url=AnyUrl("http://web.mit.edu/freebsd/head/lib/libutil/login_ok.3"),
    ),  # type: ignore
    "http://web.mit.edu/freebsd/head/lib/libutil/login_ok.3": CreativeWork(
        identifier="libutil-David-Nugent",
        name="libutil David Nugent License",
        url=AnyUrl("http://web.mit.edu/freebsd/head/lib/libutil/login_ok.3"),
    ),  # type: ignore
    "LiLiQ-P-1.1": CreativeWork(
        identifier="LiLiQ-P-1.1",
        name="Licence Libre du Québec – Permissive version 1.1",
        url=AnyUrl("https://forge.gouv.qc.ca/licence/fr/liliq-v1-1/"),
    ),  # type: ignore
    "https://spdx.org/licenses/LiLiQ-P-1.1": CreativeWork(
        identifier="LiLiQ-P-1.1",
        name="Licence Libre du Québec – Permissive version 1.1",
        url=AnyUrl("https://forge.gouv.qc.ca/licence/fr/liliq-v1-1/"),
    ),  # type: ignore
    "https://spdx.org/licenses/LiLiQ-P-1.1.html": CreativeWork(
        identifier="LiLiQ-P-1.1",
        name="Licence Libre du Québec – Permissive version 1.1",
        url=AnyUrl("https://forge.gouv.qc.ca/licence/fr/liliq-v1-1/"),
    ),  # type: ignore
    "https://forge.gouv.qc.ca/licence/fr/liliq-v1-1/": CreativeWork(
        identifier="LiLiQ-P-1.1",
        name="Licence Libre du Québec – Permissive version 1.1",
        url=AnyUrl("https://forge.gouv.qc.ca/licence/fr/liliq-v1-1/"),
    ),  # type: ignore
    "LiLiQ-R-1.1": CreativeWork(
        identifier="LiLiQ-R-1.1",
        name="Licence Libre du Québec – Réciprocité version 1.1",
        url=AnyUrl(
            "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-liliq-r-v1-1/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LiLiQ-R-1.1": CreativeWork(
        identifier="LiLiQ-R-1.1",
        name="Licence Libre du Québec – Réciprocité version 1.1",
        url=AnyUrl(
            "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-liliq-r-v1-1/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LiLiQ-R-1.1.html": CreativeWork(
        identifier="LiLiQ-R-1.1",
        name="Licence Libre du Québec – Réciprocité version 1.1",
        url=AnyUrl(
            "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-liliq-r-v1-1/"
        ),
    ),  # type: ignore
    "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-liliq-r-v1-1/": CreativeWork(
        identifier="LiLiQ-R-1.1",
        name="Licence Libre du Québec – Réciprocité version 1.1",
        url=AnyUrl(
            "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-liliq-r-v1-1/"
        ),
    ),  # type: ignore
    "LiLiQ-Rplus-1.1": CreativeWork(
        identifier="LiLiQ-Rplus-1.1",
        name="Licence Libre du Québec – Réciprocité forte version 1.1",
        url=AnyUrl(
            "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-forte-liliq-r-v1-1/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LiLiQ-Rplus-1.1": CreativeWork(
        identifier="LiLiQ-Rplus-1.1",
        name="Licence Libre du Québec – Réciprocité forte version 1.1",
        url=AnyUrl(
            "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-forte-liliq-r-v1-1/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LiLiQ-Rplus-1.1.html": CreativeWork(
        identifier="LiLiQ-Rplus-1.1",
        name="Licence Libre du Québec – Réciprocité forte version 1.1",
        url=AnyUrl(
            "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-forte-liliq-r-v1-1/"
        ),
    ),  # type: ignore
    "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-forte-liliq-r-v1-1/": CreativeWork(
        identifier="LiLiQ-Rplus-1.1",
        name="Licence Libre du Québec – Réciprocité forte version 1.1",
        url=AnyUrl(
            "https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-forte-liliq-r-v1-1/"
        ),
    ),  # type: ignore
    "Linux-man-pages-1-para": CreativeWork(
        identifier="Linux-man-pages-1-para",
        name="Linux man-pages - 1 paragraph",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/getcpu.2#n4"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-man-pages-1-para": CreativeWork(
        identifier="Linux-man-pages-1-para",
        name="Linux man-pages - 1 paragraph",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/getcpu.2#n4"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-man-pages-1-para.html": CreativeWork(
        identifier="Linux-man-pages-1-para",
        name="Linux man-pages - 1 paragraph",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/getcpu.2#n4"
        ),
    ),  # type: ignore
    "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/getcpu.2#n4": CreativeWork(
        identifier="Linux-man-pages-1-para",
        name="Linux man-pages - 1 paragraph",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/getcpu.2#n4"
        ),
    ),  # type: ignore
    "Linux-man-pages-copyleft": CreativeWork(
        identifier="Linux-man-pages-copyleft",
        name="Linux man-pages Copyleft",
        url=AnyUrl("https://www.kernel.org/doc/man-pages/licenses.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-man-pages-copyleft": CreativeWork(
        identifier="Linux-man-pages-copyleft",
        name="Linux man-pages Copyleft",
        url=AnyUrl("https://www.kernel.org/doc/man-pages/licenses.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-man-pages-copyleft.html": CreativeWork(
        identifier="Linux-man-pages-copyleft",
        name="Linux man-pages Copyleft",
        url=AnyUrl("https://www.kernel.org/doc/man-pages/licenses.html"),
    ),  # type: ignore
    "https://www.kernel.org/doc/man-pages/licenses.html": CreativeWork(
        identifier="Linux-man-pages-copyleft",
        name="Linux man-pages Copyleft",
        url=AnyUrl("https://www.kernel.org/doc/man-pages/licenses.html"),
    ),  # type: ignore
    "Linux-man-pages-copyleft-2-para": CreativeWork(
        identifier="Linux-man-pages-copyleft-2-para",
        name="Linux man-pages Copyleft - 2 paragraphs",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/move_pages.2#n5"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-man-pages-copyleft-2-para": CreativeWork(
        identifier="Linux-man-pages-copyleft-2-para",
        name="Linux man-pages Copyleft - 2 paragraphs",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/move_pages.2#n5"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-man-pages-copyleft-2-para.html": CreativeWork(
        identifier="Linux-man-pages-copyleft-2-para",
        name="Linux man-pages Copyleft - 2 paragraphs",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/move_pages.2#n5"
        ),
    ),  # type: ignore
    "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/move_pages.2#n5": CreativeWork(
        identifier="Linux-man-pages-copyleft-2-para",
        name="Linux man-pages Copyleft - 2 paragraphs",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/move_pages.2#n5"
        ),
    ),  # type: ignore
    "Linux-man-pages-copyleft-var": CreativeWork(
        identifier="Linux-man-pages-copyleft-var",
        name="Linux man-pages Copyleft Variant",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/set_mempolicy.2#n5"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-man-pages-copyleft-var": CreativeWork(
        identifier="Linux-man-pages-copyleft-var",
        name="Linux man-pages Copyleft Variant",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/set_mempolicy.2#n5"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-man-pages-copyleft-var.html": CreativeWork(
        identifier="Linux-man-pages-copyleft-var",
        name="Linux man-pages Copyleft Variant",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/set_mempolicy.2#n5"
        ),
    ),  # type: ignore
    "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/set_mempolicy.2#n5": CreativeWork(
        identifier="Linux-man-pages-copyleft-var",
        name="Linux man-pages Copyleft Variant",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/set_mempolicy.2#n5"
        ),
    ),  # type: ignore
    "Linux-OpenIB": CreativeWork(
        identifier="Linux-OpenIB",
        name="Linux Kernel Variant of OpenIB.org license",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/infiniband/core/sa.h"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-OpenIB": CreativeWork(
        identifier="Linux-OpenIB",
        name="Linux Kernel Variant of OpenIB.org license",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/infiniband/core/sa.h"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Linux-OpenIB.html": CreativeWork(
        identifier="Linux-OpenIB",
        name="Linux Kernel Variant of OpenIB.org license",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/infiniband/core/sa.h"
        ),
    ),  # type: ignore
    "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/infiniband/core/sa.h": CreativeWork(
        identifier="Linux-OpenIB",
        name="Linux Kernel Variant of OpenIB.org license",
        url=AnyUrl(
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/infiniband/core/sa.h"
        ),
    ),  # type: ignore
    "LOOP": CreativeWork(
        identifier="LOOP",
        name="Common Lisp LOOP License",
        url=AnyUrl(
            "https://gitlab.com/embeddable-common-lisp/ecl/-/blob/develop/src/lsp/loop.lsp"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LOOP": CreativeWork(
        identifier="LOOP",
        name="Common Lisp LOOP License",
        url=AnyUrl(
            "https://gitlab.com/embeddable-common-lisp/ecl/-/blob/develop/src/lsp/loop.lsp"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/LOOP.html": CreativeWork(
        identifier="LOOP",
        name="Common Lisp LOOP License",
        url=AnyUrl(
            "https://gitlab.com/embeddable-common-lisp/ecl/-/blob/develop/src/lsp/loop.lsp"
        ),
    ),  # type: ignore
    "https://gitlab.com/embeddable-common-lisp/ecl/-/blob/develop/src/lsp/loop.lsp": CreativeWork(
        identifier="LOOP",
        name="Common Lisp LOOP License",
        url=AnyUrl(
            "https://gitlab.com/embeddable-common-lisp/ecl/-/blob/develop/src/lsp/loop.lsp"
        ),
    ),  # type: ignore
    "LPD-document": CreativeWork(
        identifier="LPD-document",
        name="LPD Documentation License",
        url=AnyUrl("https://github.com/Cyan4973/xxHash/blob/dev/doc/xxhash_spec.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPD-document": CreativeWork(
        identifier="LPD-document",
        name="LPD Documentation License",
        url=AnyUrl("https://github.com/Cyan4973/xxHash/blob/dev/doc/xxhash_spec.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPD-document.html": CreativeWork(
        identifier="LPD-document",
        name="LPD Documentation License",
        url=AnyUrl("https://github.com/Cyan4973/xxHash/blob/dev/doc/xxhash_spec.md"),
    ),  # type: ignore
    "https://github.com/Cyan4973/xxHash/blob/dev/doc/xxhash_spec.md": CreativeWork(
        identifier="LPD-document",
        name="LPD Documentation License",
        url=AnyUrl("https://github.com/Cyan4973/xxHash/blob/dev/doc/xxhash_spec.md"),
    ),  # type: ignore
    "LPL-1.0": CreativeWork(
        identifier="LPL-1.0",
        name="Lucent Public License Version 1.0",
        url=AnyUrl("https://opensource.org/licenses/LPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPL-1.0": CreativeWork(
        identifier="LPL-1.0",
        name="Lucent Public License Version 1.0",
        url=AnyUrl("https://opensource.org/licenses/LPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPL-1.0.html": CreativeWork(
        identifier="LPL-1.0",
        name="Lucent Public License Version 1.0",
        url=AnyUrl("https://opensource.org/licenses/LPL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/LPL-1.0": CreativeWork(
        identifier="LPL-1.0",
        name="Lucent Public License Version 1.0",
        url=AnyUrl("https://opensource.org/licenses/LPL-1.0"),
    ),  # type: ignore
    "LPL-1.02": CreativeWork(
        identifier="LPL-1.02",
        name="Lucent Public License v1.02",
        url=AnyUrl("http://plan9.bell-labs.com/plan9/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPL-1.02": CreativeWork(
        identifier="LPL-1.02",
        name="Lucent Public License v1.02",
        url=AnyUrl("http://plan9.bell-labs.com/plan9/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPL-1.02.html": CreativeWork(
        identifier="LPL-1.02",
        name="Lucent Public License v1.02",
        url=AnyUrl("http://plan9.bell-labs.com/plan9/license.html"),
    ),  # type: ignore
    "http://plan9.bell-labs.com/plan9/license.html": CreativeWork(
        identifier="LPL-1.02",
        name="Lucent Public License v1.02",
        url=AnyUrl("http://plan9.bell-labs.com/plan9/license.html"),
    ),  # type: ignore
    "LPPL-1.0": CreativeWork(
        identifier="LPPL-1.0",
        name="LaTeX Project Public License v1.0",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-0.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.0": CreativeWork(
        identifier="LPPL-1.0",
        name="LaTeX Project Public License v1.0",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-0.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.0.html": CreativeWork(
        identifier="LPPL-1.0",
        name="LaTeX Project Public License v1.0",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-0.txt"),
    ),  # type: ignore
    "http://www.latex-project.org/lppl/lppl-1-0.txt": CreativeWork(
        identifier="LPPL-1.0",
        name="LaTeX Project Public License v1.0",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-0.txt"),
    ),  # type: ignore
    "LPPL-1.1": CreativeWork(
        identifier="LPPL-1.1",
        name="LaTeX Project Public License v1.1",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.1": CreativeWork(
        identifier="LPPL-1.1",
        name="LaTeX Project Public License v1.1",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-1.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.1.html": CreativeWork(
        identifier="LPPL-1.1",
        name="LaTeX Project Public License v1.1",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-1.txt"),
    ),  # type: ignore
    "http://www.latex-project.org/lppl/lppl-1-1.txt": CreativeWork(
        identifier="LPPL-1.1",
        name="LaTeX Project Public License v1.1",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-1.txt"),
    ),  # type: ignore
    "LPPL-1.2": CreativeWork(
        identifier="LPPL-1.2",
        name="LaTeX Project Public License v1.2",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.2": CreativeWork(
        identifier="LPPL-1.2",
        name="LaTeX Project Public License v1.2",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-2.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.2.html": CreativeWork(
        identifier="LPPL-1.2",
        name="LaTeX Project Public License v1.2",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-2.txt"),
    ),  # type: ignore
    "http://www.latex-project.org/lppl/lppl-1-2.txt": CreativeWork(
        identifier="LPPL-1.2",
        name="LaTeX Project Public License v1.2",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-2.txt"),
    ),  # type: ignore
    "LPPL-1.3a": CreativeWork(
        identifier="LPPL-1.3a",
        name="LaTeX Project Public License v1.3a",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-3a.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.3a": CreativeWork(
        identifier="LPPL-1.3a",
        name="LaTeX Project Public License v1.3a",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-3a.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.3a.html": CreativeWork(
        identifier="LPPL-1.3a",
        name="LaTeX Project Public License v1.3a",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-3a.txt"),
    ),  # type: ignore
    "http://www.latex-project.org/lppl/lppl-1-3a.txt": CreativeWork(
        identifier="LPPL-1.3a",
        name="LaTeX Project Public License v1.3a",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-3a.txt"),
    ),  # type: ignore
    "LPPL-1.3c": CreativeWork(
        identifier="LPPL-1.3c",
        name="LaTeX Project Public License v1.3c",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-3c.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.3c": CreativeWork(
        identifier="LPPL-1.3c",
        name="LaTeX Project Public License v1.3c",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-3c.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/LPPL-1.3c.html": CreativeWork(
        identifier="LPPL-1.3c",
        name="LaTeX Project Public License v1.3c",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-3c.txt"),
    ),  # type: ignore
    "http://www.latex-project.org/lppl/lppl-1-3c.txt": CreativeWork(
        identifier="LPPL-1.3c",
        name="LaTeX Project Public License v1.3c",
        url=AnyUrl("http://www.latex-project.org/lppl/lppl-1-3c.txt"),
    ),  # type: ignore
    "lsof": CreativeWork(
        identifier="lsof",
        name="lsof License",
        url=AnyUrl("https://github.com/lsof-org/lsof/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/lsof": CreativeWork(
        identifier="lsof",
        name="lsof License",
        url=AnyUrl("https://github.com/lsof-org/lsof/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/lsof.html": CreativeWork(
        identifier="lsof",
        name="lsof License",
        url=AnyUrl("https://github.com/lsof-org/lsof/blob/master/COPYING"),
    ),  # type: ignore
    "https://github.com/lsof-org/lsof/blob/master/COPYING": CreativeWork(
        identifier="lsof",
        name="lsof License",
        url=AnyUrl("https://github.com/lsof-org/lsof/blob/master/COPYING"),
    ),  # type: ignore
    "Lucida-Bitmap-Fonts": CreativeWork(
        identifier="Lucida-Bitmap-Fonts",
        name="Lucida Bitmap Fonts License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/bh-100dpi/-/blob/master/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Lucida-Bitmap-Fonts": CreativeWork(
        identifier="Lucida-Bitmap-Fonts",
        name="Lucida Bitmap Fonts License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/bh-100dpi/-/blob/master/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Lucida-Bitmap-Fonts.html": CreativeWork(
        identifier="Lucida-Bitmap-Fonts",
        name="Lucida Bitmap Fonts License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/bh-100dpi/-/blob/master/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/font/bh-100dpi/-/blob/master/COPYING?ref_type=heads": CreativeWork(
        identifier="Lucida-Bitmap-Fonts",
        name="Lucida Bitmap Fonts License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/font/bh-100dpi/-/blob/master/COPYING?ref_type=heads"
        ),
    ),  # type: ignore
    "LZMA-SDK-9.11-to-9.20": CreativeWork(
        identifier="LZMA-SDK-9.11-to-9.20",
        name="LZMA SDK License (versions 9.11 to 9.20)",
        url=AnyUrl("https://www.7-zip.org/sdk.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LZMA-SDK-9.11-to-9.20": CreativeWork(
        identifier="LZMA-SDK-9.11-to-9.20",
        name="LZMA SDK License (versions 9.11 to 9.20)",
        url=AnyUrl("https://www.7-zip.org/sdk.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LZMA-SDK-9.11-to-9.20.html": CreativeWork(
        identifier="LZMA-SDK-9.11-to-9.20",
        name="LZMA SDK License (versions 9.11 to 9.20)",
        url=AnyUrl("https://www.7-zip.org/sdk.html"),
    ),  # type: ignore
    "https://www.7-zip.org/sdk.html": CreativeWork(
        identifier="LZMA-SDK-9.11-to-9.20",
        name="LZMA SDK License (versions 9.11 to 9.20)",
        url=AnyUrl("https://www.7-zip.org/sdk.html"),
    ),  # type: ignore
    "LZMA-SDK-9.22": CreativeWork(
        identifier="LZMA-SDK-9.22",
        name="LZMA SDK License (versions 9.22 and beyond)",
        url=AnyUrl("https://www.7-zip.org/sdk.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LZMA-SDK-9.22": CreativeWork(
        identifier="LZMA-SDK-9.22",
        name="LZMA SDK License (versions 9.22 and beyond)",
        url=AnyUrl("https://www.7-zip.org/sdk.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/LZMA-SDK-9.22.html": CreativeWork(
        identifier="LZMA-SDK-9.22",
        name="LZMA SDK License (versions 9.22 and beyond)",
        url=AnyUrl("https://www.7-zip.org/sdk.html"),
    ),  # type: ignore
    "Mackerras-3-Clause": CreativeWork(
        identifier="Mackerras-3-Clause",
        name="Mackerras 3-Clause License",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/pppd/chap_ms.c#L6-L28"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Mackerras-3-Clause": CreativeWork(
        identifier="Mackerras-3-Clause",
        name="Mackerras 3-Clause License",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/pppd/chap_ms.c#L6-L28"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Mackerras-3-Clause.html": CreativeWork(
        identifier="Mackerras-3-Clause",
        name="Mackerras 3-Clause License",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/pppd/chap_ms.c#L6-L28"
        ),
    ),  # type: ignore
    "https://github.com/ppp-project/ppp/blob/master/pppd/chap_ms.c#L6-L28": CreativeWork(
        identifier="Mackerras-3-Clause",
        name="Mackerras 3-Clause License",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/pppd/chap_ms.c#L6-L28"
        ),
    ),  # type: ignore
    "Mackerras-3-Clause-acknowledgment": CreativeWork(
        identifier="Mackerras-3-Clause-acknowledgment",
        name="Mackerras 3-Clause - acknowledgment variant",
        url=AnyUrl("https://github.com/ppp-project/ppp/blob/master/pppd/auth.c#L6-L28"),
    ),  # type: ignore
    "https://spdx.org/licenses/Mackerras-3-Clause-acknowledgment": CreativeWork(
        identifier="Mackerras-3-Clause-acknowledgment",
        name="Mackerras 3-Clause - acknowledgment variant",
        url=AnyUrl("https://github.com/ppp-project/ppp/blob/master/pppd/auth.c#L6-L28"),
    ),  # type: ignore
    "https://spdx.org/licenses/Mackerras-3-Clause-acknowledgment.html": CreativeWork(
        identifier="Mackerras-3-Clause-acknowledgment",
        name="Mackerras 3-Clause - acknowledgment variant",
        url=AnyUrl("https://github.com/ppp-project/ppp/blob/master/pppd/auth.c#L6-L28"),
    ),  # type: ignore
    "https://github.com/ppp-project/ppp/blob/master/pppd/auth.c#L6-L28": CreativeWork(
        identifier="Mackerras-3-Clause-acknowledgment",
        name="Mackerras 3-Clause - acknowledgment variant",
        url=AnyUrl("https://github.com/ppp-project/ppp/blob/master/pppd/auth.c#L6-L28"),
    ),  # type: ignore
    "magaz": CreativeWork(
        identifier="magaz",
        name="magaz License",
        url=AnyUrl(
            "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/magaz/magaz.tex"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/magaz": CreativeWork(
        identifier="magaz",
        name="magaz License",
        url=AnyUrl(
            "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/magaz/magaz.tex"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/magaz.html": CreativeWork(
        identifier="magaz",
        name="magaz License",
        url=AnyUrl(
            "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/magaz/magaz.tex"
        ),
    ),  # type: ignore
    "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/magaz/magaz.tex": CreativeWork(
        identifier="magaz",
        name="magaz License",
        url=AnyUrl(
            "https://mirrors.nic.cz/tex-archive/macros/latex/contrib/magaz/magaz.tex"
        ),
    ),  # type: ignore
    "mailprio": CreativeWork(
        identifier="mailprio",
        name="mailprio License",
        url=AnyUrl("https://fossies.org/linux/sendmail/contrib/mailprio"),
    ),  # type: ignore
    "https://spdx.org/licenses/mailprio": CreativeWork(
        identifier="mailprio",
        name="mailprio License",
        url=AnyUrl("https://fossies.org/linux/sendmail/contrib/mailprio"),
    ),  # type: ignore
    "https://spdx.org/licenses/mailprio.html": CreativeWork(
        identifier="mailprio",
        name="mailprio License",
        url=AnyUrl("https://fossies.org/linux/sendmail/contrib/mailprio"),
    ),  # type: ignore
    "https://fossies.org/linux/sendmail/contrib/mailprio": CreativeWork(
        identifier="mailprio",
        name="mailprio License",
        url=AnyUrl("https://fossies.org/linux/sendmail/contrib/mailprio"),
    ),  # type: ignore
    "MakeIndex": CreativeWork(
        identifier="MakeIndex",
        name="MakeIndex License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MakeIndex"),
    ),  # type: ignore
    "https://spdx.org/licenses/MakeIndex": CreativeWork(
        identifier="MakeIndex",
        name="MakeIndex License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MakeIndex"),
    ),  # type: ignore
    "https://spdx.org/licenses/MakeIndex.html": CreativeWork(
        identifier="MakeIndex",
        name="MakeIndex License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MakeIndex"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/MakeIndex": CreativeWork(
        identifier="MakeIndex",
        name="MakeIndex License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MakeIndex"),
    ),  # type: ignore
    "man2html": CreativeWork(
        identifier="man2html",
        name="man2html License",
        url=AnyUrl("http://primates.ximian.com/~flucifredi/man/man-1.6g.tar.gz"),
    ),  # type: ignore
    "https://spdx.org/licenses/man2html": CreativeWork(
        identifier="man2html",
        name="man2html License",
        url=AnyUrl("http://primates.ximian.com/~flucifredi/man/man-1.6g.tar.gz"),
    ),  # type: ignore
    "https://spdx.org/licenses/man2html.html": CreativeWork(
        identifier="man2html",
        name="man2html License",
        url=AnyUrl("http://primates.ximian.com/~flucifredi/man/man-1.6g.tar.gz"),
    ),  # type: ignore
    "http://primates.ximian.com/~flucifredi/man/man-1.6g.tar.gz": CreativeWork(
        identifier="man2html",
        name="man2html License",
        url=AnyUrl("http://primates.ximian.com/~flucifredi/man/man-1.6g.tar.gz"),
    ),  # type: ignore
    "Martin-Birgmeier": CreativeWork(
        identifier="Martin-Birgmeier",
        name="Martin Birgmeier License",
        url=AnyUrl("https://github.com/Perl/perl5/blob/blead/util.c#L6136"),
    ),  # type: ignore
    "https://spdx.org/licenses/Martin-Birgmeier": CreativeWork(
        identifier="Martin-Birgmeier",
        name="Martin Birgmeier License",
        url=AnyUrl("https://github.com/Perl/perl5/blob/blead/util.c#L6136"),
    ),  # type: ignore
    "https://spdx.org/licenses/Martin-Birgmeier.html": CreativeWork(
        identifier="Martin-Birgmeier",
        name="Martin Birgmeier License",
        url=AnyUrl("https://github.com/Perl/perl5/blob/blead/util.c#L6136"),
    ),  # type: ignore
    "https://github.com/Perl/perl5/blob/blead/util.c#L6136": CreativeWork(
        identifier="Martin-Birgmeier",
        name="Martin Birgmeier License",
        url=AnyUrl("https://github.com/Perl/perl5/blob/blead/util.c#L6136"),
    ),  # type: ignore
    "McPhee-slideshow": CreativeWork(
        identifier="McPhee-slideshow",
        name="McPhee Slideshow License",
        url=AnyUrl(
            "https://mirror.las.iastate.edu/tex-archive/graphics/metapost/contrib/macros/slideshow/slideshow.mp"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/McPhee-slideshow": CreativeWork(
        identifier="McPhee-slideshow",
        name="McPhee Slideshow License",
        url=AnyUrl(
            "https://mirror.las.iastate.edu/tex-archive/graphics/metapost/contrib/macros/slideshow/slideshow.mp"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/McPhee-slideshow.html": CreativeWork(
        identifier="McPhee-slideshow",
        name="McPhee Slideshow License",
        url=AnyUrl(
            "https://mirror.las.iastate.edu/tex-archive/graphics/metapost/contrib/macros/slideshow/slideshow.mp"
        ),
    ),  # type: ignore
    "https://mirror.las.iastate.edu/tex-archive/graphics/metapost/contrib/macros/slideshow/slideshow.mp": CreativeWork(
        identifier="McPhee-slideshow",
        name="McPhee Slideshow License",
        url=AnyUrl(
            "https://mirror.las.iastate.edu/tex-archive/graphics/metapost/contrib/macros/slideshow/slideshow.mp"
        ),
    ),  # type: ignore
    "metamail": CreativeWork(
        identifier="metamail",
        name="metamail License",
        url=AnyUrl(
            "https://github.com/Dual-Life/mime-base64/blob/master/Base64.xs#L12"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/metamail": CreativeWork(
        identifier="metamail",
        name="metamail License",
        url=AnyUrl(
            "https://github.com/Dual-Life/mime-base64/blob/master/Base64.xs#L12"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/metamail.html": CreativeWork(
        identifier="metamail",
        name="metamail License",
        url=AnyUrl(
            "https://github.com/Dual-Life/mime-base64/blob/master/Base64.xs#L12"
        ),
    ),  # type: ignore
    "https://github.com/Dual-Life/mime-base64/blob/master/Base64.xs#L12": CreativeWork(
        identifier="metamail",
        name="metamail License",
        url=AnyUrl(
            "https://github.com/Dual-Life/mime-base64/blob/master/Base64.xs#L12"
        ),
    ),  # type: ignore
    "Minpack": CreativeWork(
        identifier="Minpack",
        name="Minpack License",
        url=AnyUrl("http://www.netlib.org/minpack/disclaimer"),
    ),  # type: ignore
    "https://spdx.org/licenses/Minpack": CreativeWork(
        identifier="Minpack",
        name="Minpack License",
        url=AnyUrl("http://www.netlib.org/minpack/disclaimer"),
    ),  # type: ignore
    "https://spdx.org/licenses/Minpack.html": CreativeWork(
        identifier="Minpack",
        name="Minpack License",
        url=AnyUrl("http://www.netlib.org/minpack/disclaimer"),
    ),  # type: ignore
    "http://www.netlib.org/minpack/disclaimer": CreativeWork(
        identifier="Minpack",
        name="Minpack License",
        url=AnyUrl("http://www.netlib.org/minpack/disclaimer"),
    ),  # type: ignore
    "MIPS": CreativeWork(
        identifier="MIPS",
        name="MIPS License",
        url=AnyUrl(
            "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/sym.h#n11"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIPS": CreativeWork(
        identifier="MIPS",
        name="MIPS License",
        url=AnyUrl(
            "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/sym.h#n11"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIPS.html": CreativeWork(
        identifier="MIPS",
        name="MIPS License",
        url=AnyUrl(
            "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/sym.h#n11"
        ),
    ),  # type: ignore
    "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/sym.h#n11": CreativeWork(
        identifier="MIPS",
        name="MIPS License",
        url=AnyUrl(
            "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/sym.h#n11"
        ),
    ),  # type: ignore
    "MirOS": CreativeWork(
        identifier="MirOS",
        name="The MirOS Licence",
        url=AnyUrl("https://opensource.org/licenses/MirOS"),
    ),  # type: ignore
    "https://spdx.org/licenses/MirOS": CreativeWork(
        identifier="MirOS",
        name="The MirOS Licence",
        url=AnyUrl("https://opensource.org/licenses/MirOS"),
    ),  # type: ignore
    "https://spdx.org/licenses/MirOS.html": CreativeWork(
        identifier="MirOS",
        name="The MirOS Licence",
        url=AnyUrl("https://opensource.org/licenses/MirOS"),
    ),  # type: ignore
    "https://opensource.org/licenses/MirOS": CreativeWork(
        identifier="MirOS",
        name="The MirOS Licence",
        url=AnyUrl("https://opensource.org/licenses/MirOS"),
    ),  # type: ignore
    "MIT": CreativeWork(
        identifier="MIT",
        name="MIT License",
        url=AnyUrl("https://opensource.org/license/mit/"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT": CreativeWork(
        identifier="MIT",
        name="MIT License",
        url=AnyUrl("https://opensource.org/license/mit/"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT.html": CreativeWork(
        identifier="MIT",
        name="MIT License",
        url=AnyUrl("https://opensource.org/license/mit/"),
    ),  # type: ignore
    "https://opensource.org/license/mit/": CreativeWork(
        identifier="MIT",
        name="MIT License",
        url=AnyUrl("https://opensource.org/license/mit/"),
    ),  # type: ignore
    "MIT-0": CreativeWork(
        identifier="MIT-0",
        name="MIT No Attribution",
        url=AnyUrl("https://github.com/aws/mit-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-0": CreativeWork(
        identifier="MIT-0",
        name="MIT No Attribution",
        url=AnyUrl("https://github.com/aws/mit-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-0.html": CreativeWork(
        identifier="MIT-0",
        name="MIT No Attribution",
        url=AnyUrl("https://github.com/aws/mit-0"),
    ),  # type: ignore
    "https://github.com/aws/mit-0": CreativeWork(
        identifier="MIT-0",
        name="MIT No Attribution",
        url=AnyUrl("https://github.com/aws/mit-0"),
    ),  # type: ignore
    "MIT-advertising": CreativeWork(
        identifier="MIT-advertising",
        name="Enlightenment License (e16)",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT_With_Advertising"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-advertising": CreativeWork(
        identifier="MIT-advertising",
        name="Enlightenment License (e16)",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT_With_Advertising"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-advertising.html": CreativeWork(
        identifier="MIT-advertising",
        name="Enlightenment License (e16)",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT_With_Advertising"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/MIT_With_Advertising": CreativeWork(
        identifier="MIT-advertising",
        name="Enlightenment License (e16)",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT_With_Advertising"),
    ),  # type: ignore
    "MIT-Click": CreativeWork(
        identifier="MIT-Click",
        name="MIT Click License",
        url=AnyUrl("https://github.com/kohler/t1utils/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Click": CreativeWork(
        identifier="MIT-Click",
        name="MIT Click License",
        url=AnyUrl("https://github.com/kohler/t1utils/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Click.html": CreativeWork(
        identifier="MIT-Click",
        name="MIT Click License",
        url=AnyUrl("https://github.com/kohler/t1utils/blob/master/LICENSE"),
    ),  # type: ignore
    "https://github.com/kohler/t1utils/blob/master/LICENSE": CreativeWork(
        identifier="MIT-Click",
        name="MIT Click License",
        url=AnyUrl("https://github.com/kohler/t1utils/blob/master/LICENSE"),
    ),  # type: ignore
    "MIT-CMU": CreativeWork(
        identifier="MIT-CMU",
        name="CMU License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#CMU_Style"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-CMU": CreativeWork(
        identifier="MIT-CMU",
        name="CMU License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#CMU_Style"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-CMU.html": CreativeWork(
        identifier="MIT-CMU",
        name="CMU License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#CMU_Style"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#CMU_Style": CreativeWork(
        identifier="MIT-CMU",
        name="CMU License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#CMU_Style"
        ),
    ),  # type: ignore
    "MIT-enna": CreativeWork(
        identifier="MIT-enna",
        name="enna License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#enna"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-enna": CreativeWork(
        identifier="MIT-enna",
        name="enna License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#enna"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-enna.html": CreativeWork(
        identifier="MIT-enna",
        name="enna License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#enna"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/MIT#enna": CreativeWork(
        identifier="MIT-enna",
        name="enna License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#enna"),
    ),  # type: ignore
    "MIT-feh": CreativeWork(
        identifier="MIT-feh",
        name="feh License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#feh"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-feh": CreativeWork(
        identifier="MIT-feh",
        name="feh License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#feh"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-feh.html": CreativeWork(
        identifier="MIT-feh",
        name="feh License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#feh"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/MIT#feh": CreativeWork(
        identifier="MIT-feh",
        name="feh License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT#feh"),
    ),  # type: ignore
    "MIT-Festival": CreativeWork(
        identifier="MIT-Festival",
        name="MIT Festival Variant",
        url=AnyUrl("https://github.com/festvox/flite/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Festival": CreativeWork(
        identifier="MIT-Festival",
        name="MIT Festival Variant",
        url=AnyUrl("https://github.com/festvox/flite/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Festival.html": CreativeWork(
        identifier="MIT-Festival",
        name="MIT Festival Variant",
        url=AnyUrl("https://github.com/festvox/flite/blob/master/COPYING"),
    ),  # type: ignore
    "https://github.com/festvox/flite/blob/master/COPYING": CreativeWork(
        identifier="MIT-Festival",
        name="MIT Festival Variant",
        url=AnyUrl("https://github.com/festvox/flite/blob/master/COPYING"),
    ),  # type: ignore
    "MIT-Khronos-old": CreativeWork(
        identifier="MIT-Khronos-old",
        name="MIT Khronos - old variant",
        url=AnyUrl(
            "https://github.com/KhronosGroup/SPIRV-Cross/blob/main/LICENSES/LicenseRef-KhronosFreeUse.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Khronos-old": CreativeWork(
        identifier="MIT-Khronos-old",
        name="MIT Khronos - old variant",
        url=AnyUrl(
            "https://github.com/KhronosGroup/SPIRV-Cross/blob/main/LICENSES/LicenseRef-KhronosFreeUse.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Khronos-old.html": CreativeWork(
        identifier="MIT-Khronos-old",
        name="MIT Khronos - old variant",
        url=AnyUrl(
            "https://github.com/KhronosGroup/SPIRV-Cross/blob/main/LICENSES/LicenseRef-KhronosFreeUse.txt"
        ),
    ),  # type: ignore
    "https://github.com/KhronosGroup/SPIRV-Cross/blob/main/LICENSES/LicenseRef-KhronosFreeUse.txt": CreativeWork(
        identifier="MIT-Khronos-old",
        name="MIT Khronos - old variant",
        url=AnyUrl(
            "https://github.com/KhronosGroup/SPIRV-Cross/blob/main/LICENSES/LicenseRef-KhronosFreeUse.txt"
        ),
    ),  # type: ignore
    "MIT-Modern-Variant": CreativeWork(
        identifier="MIT-Modern-Variant",
        name="MIT License Modern Variant",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:MIT#Modern_Variants"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Modern-Variant": CreativeWork(
        identifier="MIT-Modern-Variant",
        name="MIT License Modern Variant",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:MIT#Modern_Variants"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Modern-Variant.html": CreativeWork(
        identifier="MIT-Modern-Variant",
        name="MIT License Modern Variant",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:MIT#Modern_Variants"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing:MIT#Modern_Variants": CreativeWork(
        identifier="MIT-Modern-Variant",
        name="MIT License Modern Variant",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:MIT#Modern_Variants"),
    ),  # type: ignore
    "MIT-open-group": CreativeWork(
        identifier="MIT-open-group",
        name="MIT Open Group variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/app/iceauth/-/blob/master/COPYING"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-open-group": CreativeWork(
        identifier="MIT-open-group",
        name="MIT Open Group variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/app/iceauth/-/blob/master/COPYING"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-open-group.html": CreativeWork(
        identifier="MIT-open-group",
        name="MIT Open Group variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/app/iceauth/-/blob/master/COPYING"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/app/iceauth/-/blob/master/COPYING": CreativeWork(
        identifier="MIT-open-group",
        name="MIT Open Group variant",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/app/iceauth/-/blob/master/COPYING"
        ),
    ),  # type: ignore
    "MIT-STK": CreativeWork(
        identifier="MIT-STK",
        name="MIT-STK License",
        url=AnyUrl(
            "https://github.com/thestk/stk/blob/6aacd357d76250bb7da2b1ddf675651828784bbc/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-STK": CreativeWork(
        identifier="MIT-STK",
        name="MIT-STK License",
        url=AnyUrl(
            "https://github.com/thestk/stk/blob/6aacd357d76250bb7da2b1ddf675651828784bbc/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-STK.html": CreativeWork(
        identifier="MIT-STK",
        name="MIT-STK License",
        url=AnyUrl(
            "https://github.com/thestk/stk/blob/6aacd357d76250bb7da2b1ddf675651828784bbc/LICENSE"
        ),
    ),  # type: ignore
    "https://github.com/thestk/stk/blob/6aacd357d76250bb7da2b1ddf675651828784bbc/LICENSE": CreativeWork(
        identifier="MIT-STK",
        name="MIT-STK License",
        url=AnyUrl(
            "https://github.com/thestk/stk/blob/6aacd357d76250bb7da2b1ddf675651828784bbc/LICENSE"
        ),
    ),  # type: ignore
    "MIT-testregex": CreativeWork(
        identifier="MIT-testregex",
        name="MIT testregex Variant",
        url=AnyUrl(
            "https://github.com/dotnet/runtime/blob/55e1ac7c07df62c4108d4acedf78f77574470ce5/src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/AttRegexTests.cs#L12-L28"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-testregex": CreativeWork(
        identifier="MIT-testregex",
        name="MIT testregex Variant",
        url=AnyUrl(
            "https://github.com/dotnet/runtime/blob/55e1ac7c07df62c4108d4acedf78f77574470ce5/src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/AttRegexTests.cs#L12-L28"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-testregex.html": CreativeWork(
        identifier="MIT-testregex",
        name="MIT testregex Variant",
        url=AnyUrl(
            "https://github.com/dotnet/runtime/blob/55e1ac7c07df62c4108d4acedf78f77574470ce5/src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/AttRegexTests.cs#L12-L28"
        ),
    ),  # type: ignore
    "https://github.com/dotnet/runtime/blob/55e1ac7c07df62c4108d4acedf78f77574470ce5/src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/AttRegexTests.cs#L12-L28": CreativeWork(
        identifier="MIT-testregex",
        name="MIT testregex Variant",
        url=AnyUrl(
            "https://github.com/dotnet/runtime/blob/55e1ac7c07df62c4108d4acedf78f77574470ce5/src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/AttRegexTests.cs#L12-L28"
        ),
    ),  # type: ignore
    "MIT-Wu": CreativeWork(
        identifier="MIT-Wu",
        name="MIT Tom Wu Variant",
        url=AnyUrl("https://github.com/chromium/octane/blob/master/crypto.js"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Wu": CreativeWork(
        identifier="MIT-Wu",
        name="MIT Tom Wu Variant",
        url=AnyUrl("https://github.com/chromium/octane/blob/master/crypto.js"),
    ),  # type: ignore
    "https://spdx.org/licenses/MIT-Wu.html": CreativeWork(
        identifier="MIT-Wu",
        name="MIT Tom Wu Variant",
        url=AnyUrl("https://github.com/chromium/octane/blob/master/crypto.js"),
    ),  # type: ignore
    "https://github.com/chromium/octane/blob/master/crypto.js": CreativeWork(
        identifier="MIT-Wu",
        name="MIT Tom Wu Variant",
        url=AnyUrl("https://github.com/chromium/octane/blob/master/crypto.js"),
    ),  # type: ignore
    "MITNFA": CreativeWork(
        identifier="MITNFA",
        name="MIT +no-false-attribs license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MITNFA"),
    ),  # type: ignore
    "https://spdx.org/licenses/MITNFA": CreativeWork(
        identifier="MITNFA",
        name="MIT +no-false-attribs license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MITNFA"),
    ),  # type: ignore
    "https://spdx.org/licenses/MITNFA.html": CreativeWork(
        identifier="MITNFA",
        name="MIT +no-false-attribs license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MITNFA"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/MITNFA": CreativeWork(
        identifier="MITNFA",
        name="MIT +no-false-attribs license",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MITNFA"),
    ),  # type: ignore
    "MMIXware": CreativeWork(
        identifier="MMIXware",
        name="MMIXware License",
        url=AnyUrl("https://gitlab.lrz.de/mmix/mmixware/-/blob/master/boilerplate.w"),
    ),  # type: ignore
    "https://spdx.org/licenses/MMIXware": CreativeWork(
        identifier="MMIXware",
        name="MMIXware License",
        url=AnyUrl("https://gitlab.lrz.de/mmix/mmixware/-/blob/master/boilerplate.w"),
    ),  # type: ignore
    "https://spdx.org/licenses/MMIXware.html": CreativeWork(
        identifier="MMIXware",
        name="MMIXware License",
        url=AnyUrl("https://gitlab.lrz.de/mmix/mmixware/-/blob/master/boilerplate.w"),
    ),  # type: ignore
    "https://gitlab.lrz.de/mmix/mmixware/-/blob/master/boilerplate.w": CreativeWork(
        identifier="MMIXware",
        name="MMIXware License",
        url=AnyUrl("https://gitlab.lrz.de/mmix/mmixware/-/blob/master/boilerplate.w"),
    ),  # type: ignore
    "MMPL-1.0.1": CreativeWork(
        identifier="MMPL-1.0.1",
        name="Minecraft Mod Public License v1.0.1",
        url=AnyUrl(
            "https://github.com/BuildCraft/BuildCraft/blob/623d323b1868712f29f4a8b0979a02e8d1835131/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MMPL-1.0.1": CreativeWork(
        identifier="MMPL-1.0.1",
        name="Minecraft Mod Public License v1.0.1",
        url=AnyUrl(
            "https://github.com/BuildCraft/BuildCraft/blob/623d323b1868712f29f4a8b0979a02e8d1835131/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MMPL-1.0.1.html": CreativeWork(
        identifier="MMPL-1.0.1",
        name="Minecraft Mod Public License v1.0.1",
        url=AnyUrl(
            "https://github.com/BuildCraft/BuildCraft/blob/623d323b1868712f29f4a8b0979a02e8d1835131/LICENSE"
        ),
    ),  # type: ignore
    "https://github.com/BuildCraft/BuildCraft/blob/623d323b1868712f29f4a8b0979a02e8d1835131/LICENSE": CreativeWork(
        identifier="MMPL-1.0.1",
        name="Minecraft Mod Public License v1.0.1",
        url=AnyUrl(
            "https://github.com/BuildCraft/BuildCraft/blob/623d323b1868712f29f4a8b0979a02e8d1835131/LICENSE"
        ),
    ),  # type: ignore
    "Motosoto": CreativeWork(
        identifier="Motosoto",
        name="Motosoto License",
        url=AnyUrl("https://opensource.org/licenses/Motosoto"),
    ),  # type: ignore
    "https://spdx.org/licenses/Motosoto": CreativeWork(
        identifier="Motosoto",
        name="Motosoto License",
        url=AnyUrl("https://opensource.org/licenses/Motosoto"),
    ),  # type: ignore
    "https://spdx.org/licenses/Motosoto.html": CreativeWork(
        identifier="Motosoto",
        name="Motosoto License",
        url=AnyUrl("https://opensource.org/licenses/Motosoto"),
    ),  # type: ignore
    "https://opensource.org/licenses/Motosoto": CreativeWork(
        identifier="Motosoto",
        name="Motosoto License",
        url=AnyUrl("https://opensource.org/licenses/Motosoto"),
    ),  # type: ignore
    "MPEG-SSG": CreativeWork(
        identifier="MPEG-SSG",
        name="MPEG Software Simulation",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/ppm/ppmtompeg/jrevdct.c#l1189"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MPEG-SSG": CreativeWork(
        identifier="MPEG-SSG",
        name="MPEG Software Simulation",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/ppm/ppmtompeg/jrevdct.c#l1189"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MPEG-SSG.html": CreativeWork(
        identifier="MPEG-SSG",
        name="MPEG Software Simulation",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/ppm/ppmtompeg/jrevdct.c#l1189"
        ),
    ),  # type: ignore
    "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/ppm/ppmtompeg/jrevdct.c#l1189": CreativeWork(
        identifier="MPEG-SSG",
        name="MPEG Software Simulation",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/ppm/ppmtompeg/jrevdct.c#l1189"
        ),
    ),  # type: ignore
    "mpi-permissive": CreativeWork(
        identifier="mpi-permissive",
        name="mpi Permissive License",
        url=AnyUrl(
            "https://sources.debian.org/src/openmpi/4.1.0-10/ompi/debuggers/msgq_interface.h/?hl=19#L19"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/mpi-permissive": CreativeWork(
        identifier="mpi-permissive",
        name="mpi Permissive License",
        url=AnyUrl(
            "https://sources.debian.org/src/openmpi/4.1.0-10/ompi/debuggers/msgq_interface.h/?hl=19#L19"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/mpi-permissive.html": CreativeWork(
        identifier="mpi-permissive",
        name="mpi Permissive License",
        url=AnyUrl(
            "https://sources.debian.org/src/openmpi/4.1.0-10/ompi/debuggers/msgq_interface.h/?hl=19#L19"
        ),
    ),  # type: ignore
    "https://sources.debian.org/src/openmpi/4.1.0-10/ompi/debuggers/msgq_interface.h/?hl=19#L19": CreativeWork(
        identifier="mpi-permissive",
        name="mpi Permissive License",
        url=AnyUrl(
            "https://sources.debian.org/src/openmpi/4.1.0-10/ompi/debuggers/msgq_interface.h/?hl=19#L19"
        ),
    ),  # type: ignore
    "mpich2": CreativeWork(
        identifier="mpich2",
        name="mpich2 License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT"),
    ),  # type: ignore
    "https://spdx.org/licenses/mpich2": CreativeWork(
        identifier="mpich2",
        name="mpich2 License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT"),
    ),  # type: ignore
    "https://spdx.org/licenses/mpich2.html": CreativeWork(
        identifier="mpich2",
        name="mpich2 License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/MIT": CreativeWork(
        identifier="mpich2",
        name="mpich2 License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/MIT"),
    ),  # type: ignore
    "MPL-1.0": CreativeWork(
        identifier="MPL-1.0",
        name="Mozilla Public License 1.0",
        url=AnyUrl("http://www.mozilla.org/MPL/MPL-1.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/MPL-1.0": CreativeWork(
        identifier="MPL-1.0",
        name="Mozilla Public License 1.0",
        url=AnyUrl("http://www.mozilla.org/MPL/MPL-1.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/MPL-1.0.html": CreativeWork(
        identifier="MPL-1.0",
        name="Mozilla Public License 1.0",
        url=AnyUrl("http://www.mozilla.org/MPL/MPL-1.0.html"),
    ),  # type: ignore
    "http://www.mozilla.org/MPL/MPL-1.0.html": CreativeWork(
        identifier="MPL-1.0",
        name="Mozilla Public License 1.0",
        url=AnyUrl("http://www.mozilla.org/MPL/MPL-1.0.html"),
    ),  # type: ignore
    "MPL-1.1": CreativeWork(
        identifier="MPL-1.1",
        name="Mozilla Public License 1.1",
        url=AnyUrl("http://www.mozilla.org/MPL/MPL-1.1.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/MPL-1.1": CreativeWork(
        identifier="MPL-1.1",
        name="Mozilla Public License 1.1",
        url=AnyUrl("http://www.mozilla.org/MPL/MPL-1.1.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/MPL-1.1.html": CreativeWork(
        identifier="MPL-1.1",
        name="Mozilla Public License 1.1",
        url=AnyUrl("http://www.mozilla.org/MPL/MPL-1.1.html"),
    ),  # type: ignore
    "http://www.mozilla.org/MPL/MPL-1.1.html": CreativeWork(
        identifier="MPL-1.1",
        name="Mozilla Public License 1.1",
        url=AnyUrl("http://www.mozilla.org/MPL/MPL-1.1.html"),
    ),  # type: ignore
    "MPL-2.0": CreativeWork(
        identifier="MPL-2.0",
        name="Mozilla Public License 2.0",
        url=AnyUrl("https://www.mozilla.org/MPL/2.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/MPL-2.0": CreativeWork(
        identifier="MPL-2.0",
        name="Mozilla Public License 2.0",
        url=AnyUrl("https://www.mozilla.org/MPL/2.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/MPL-2.0.html": CreativeWork(
        identifier="MPL-2.0",
        name="Mozilla Public License 2.0",
        url=AnyUrl("https://www.mozilla.org/MPL/2.0/"),
    ),  # type: ignore
    "https://www.mozilla.org/MPL/2.0/": CreativeWork(
        identifier="MPL-2.0",
        name="Mozilla Public License 2.0",
        url=AnyUrl("https://www.mozilla.org/MPL/2.0/"),
    ),  # type: ignore
    "MPL-2.0-no-copyleft-exception": CreativeWork(
        identifier="MPL-2.0-no-copyleft-exception",
        name="Mozilla Public License 2.0 (no copyleft exception)",
        url=AnyUrl("https://www.mozilla.org/MPL/2.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/MPL-2.0-no-copyleft-exception": CreativeWork(
        identifier="MPL-2.0-no-copyleft-exception",
        name="Mozilla Public License 2.0 (no copyleft exception)",
        url=AnyUrl("https://www.mozilla.org/MPL/2.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/MPL-2.0-no-copyleft-exception.html": CreativeWork(
        identifier="MPL-2.0-no-copyleft-exception",
        name="Mozilla Public License 2.0 (no copyleft exception)",
        url=AnyUrl("https://www.mozilla.org/MPL/2.0/"),
    ),  # type: ignore
    "mplus": CreativeWork(
        identifier="mplus",
        name="mplus Font License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:Mplus?rd=Licensing/mplus"),
    ),  # type: ignore
    "https://spdx.org/licenses/mplus": CreativeWork(
        identifier="mplus",
        name="mplus Font License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:Mplus?rd=Licensing/mplus"),
    ),  # type: ignore
    "https://spdx.org/licenses/mplus.html": CreativeWork(
        identifier="mplus",
        name="mplus Font License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:Mplus?rd=Licensing/mplus"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing:Mplus?rd=Licensing/mplus": CreativeWork(
        identifier="mplus",
        name="mplus Font License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:Mplus?rd=Licensing/mplus"),
    ),  # type: ignore
    "MS-LPL": CreativeWork(
        identifier="MS-LPL",
        name="Microsoft Limited Public License",
        url=AnyUrl("https://www.openhub.net/licenses/mslpl"),
    ),  # type: ignore
    "https://spdx.org/licenses/MS-LPL": CreativeWork(
        identifier="MS-LPL",
        name="Microsoft Limited Public License",
        url=AnyUrl("https://www.openhub.net/licenses/mslpl"),
    ),  # type: ignore
    "https://spdx.org/licenses/MS-LPL.html": CreativeWork(
        identifier="MS-LPL",
        name="Microsoft Limited Public License",
        url=AnyUrl("https://www.openhub.net/licenses/mslpl"),
    ),  # type: ignore
    "https://www.openhub.net/licenses/mslpl": CreativeWork(
        identifier="MS-LPL",
        name="Microsoft Limited Public License",
        url=AnyUrl("https://www.openhub.net/licenses/mslpl"),
    ),  # type: ignore
    "MS-PL": CreativeWork(
        identifier="MS-PL",
        name="Microsoft Public License",
        url=AnyUrl("http://www.microsoft.com/opensource/licenses.mspx"),
    ),  # type: ignore
    "https://spdx.org/licenses/MS-PL": CreativeWork(
        identifier="MS-PL",
        name="Microsoft Public License",
        url=AnyUrl("http://www.microsoft.com/opensource/licenses.mspx"),
    ),  # type: ignore
    "https://spdx.org/licenses/MS-PL.html": CreativeWork(
        identifier="MS-PL",
        name="Microsoft Public License",
        url=AnyUrl("http://www.microsoft.com/opensource/licenses.mspx"),
    ),  # type: ignore
    "http://www.microsoft.com/opensource/licenses.mspx": CreativeWork(
        identifier="MS-PL",
        name="Microsoft Public License",
        url=AnyUrl("http://www.microsoft.com/opensource/licenses.mspx"),
    ),  # type: ignore
    "MS-RL": CreativeWork(
        identifier="MS-RL",
        name="Microsoft Reciprocal License",
        url=AnyUrl("http://www.microsoft.com/opensource/licenses.mspx"),
    ),  # type: ignore
    "https://spdx.org/licenses/MS-RL": CreativeWork(
        identifier="MS-RL",
        name="Microsoft Reciprocal License",
        url=AnyUrl("http://www.microsoft.com/opensource/licenses.mspx"),
    ),  # type: ignore
    "https://spdx.org/licenses/MS-RL.html": CreativeWork(
        identifier="MS-RL",
        name="Microsoft Reciprocal License",
        url=AnyUrl("http://www.microsoft.com/opensource/licenses.mspx"),
    ),  # type: ignore
    "MTLL": CreativeWork(
        identifier="MTLL",
        name="Matrix Template Library License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Matrix_Template_Library_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MTLL": CreativeWork(
        identifier="MTLL",
        name="Matrix Template Library License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Matrix_Template_Library_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/MTLL.html": CreativeWork(
        identifier="MTLL",
        name="Matrix Template Library License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Matrix_Template_Library_License"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Matrix_Template_Library_License": CreativeWork(
        identifier="MTLL",
        name="Matrix Template Library License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Matrix_Template_Library_License"
        ),
    ),  # type: ignore
    "MulanPSL-1.0": CreativeWork(
        identifier="MulanPSL-1.0",
        name="Mulan Permissive Software License, Version 1",
        url=AnyUrl("https://license.coscl.org.cn/MulanPSL/"),
    ),  # type: ignore
    "https://spdx.org/licenses/MulanPSL-1.0": CreativeWork(
        identifier="MulanPSL-1.0",
        name="Mulan Permissive Software License, Version 1",
        url=AnyUrl("https://license.coscl.org.cn/MulanPSL/"),
    ),  # type: ignore
    "https://spdx.org/licenses/MulanPSL-1.0.html": CreativeWork(
        identifier="MulanPSL-1.0",
        name="Mulan Permissive Software License, Version 1",
        url=AnyUrl("https://license.coscl.org.cn/MulanPSL/"),
    ),  # type: ignore
    "https://license.coscl.org.cn/MulanPSL/": CreativeWork(
        identifier="MulanPSL-1.0",
        name="Mulan Permissive Software License, Version 1",
        url=AnyUrl("https://license.coscl.org.cn/MulanPSL/"),
    ),  # type: ignore
    "MulanPSL-2.0": CreativeWork(
        identifier="MulanPSL-2.0",
        name="Mulan Permissive Software License, Version 2",
        url=AnyUrl("https://license.coscl.org.cn/MulanPSL2"),
    ),  # type: ignore
    "https://spdx.org/licenses/MulanPSL-2.0": CreativeWork(
        identifier="MulanPSL-2.0",
        name="Mulan Permissive Software License, Version 2",
        url=AnyUrl("https://license.coscl.org.cn/MulanPSL2"),
    ),  # type: ignore
    "https://spdx.org/licenses/MulanPSL-2.0.html": CreativeWork(
        identifier="MulanPSL-2.0",
        name="Mulan Permissive Software License, Version 2",
        url=AnyUrl("https://license.coscl.org.cn/MulanPSL2"),
    ),  # type: ignore
    "https://license.coscl.org.cn/MulanPSL2": CreativeWork(
        identifier="MulanPSL-2.0",
        name="Mulan Permissive Software License, Version 2",
        url=AnyUrl("https://license.coscl.org.cn/MulanPSL2"),
    ),  # type: ignore
    "Multics": CreativeWork(
        identifier="Multics",
        name="Multics License",
        url=AnyUrl("https://opensource.org/licenses/Multics"),
    ),  # type: ignore
    "https://spdx.org/licenses/Multics": CreativeWork(
        identifier="Multics",
        name="Multics License",
        url=AnyUrl("https://opensource.org/licenses/Multics"),
    ),  # type: ignore
    "https://spdx.org/licenses/Multics.html": CreativeWork(
        identifier="Multics",
        name="Multics License",
        url=AnyUrl("https://opensource.org/licenses/Multics"),
    ),  # type: ignore
    "https://opensource.org/licenses/Multics": CreativeWork(
        identifier="Multics",
        name="Multics License",
        url=AnyUrl("https://opensource.org/licenses/Multics"),
    ),  # type: ignore
    "Mup": CreativeWork(
        identifier="Mup",
        name="Mup License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Mup"),
    ),  # type: ignore
    "https://spdx.org/licenses/Mup": CreativeWork(
        identifier="Mup",
        name="Mup License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Mup"),
    ),  # type: ignore
    "https://spdx.org/licenses/Mup.html": CreativeWork(
        identifier="Mup",
        name="Mup License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Mup"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Mup": CreativeWork(
        identifier="Mup",
        name="Mup License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Mup"),
    ),  # type: ignore
    "NAIST-2003": CreativeWork(
        identifier="NAIST-2003",
        name="Nara Institute of Science and Technology License (2003)",
        url=AnyUrl(
            "https://enterprise.dejacode.com/licenses/public/naist-2003/#license-text"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NAIST-2003": CreativeWork(
        identifier="NAIST-2003",
        name="Nara Institute of Science and Technology License (2003)",
        url=AnyUrl(
            "https://enterprise.dejacode.com/licenses/public/naist-2003/#license-text"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NAIST-2003.html": CreativeWork(
        identifier="NAIST-2003",
        name="Nara Institute of Science and Technology License (2003)",
        url=AnyUrl(
            "https://enterprise.dejacode.com/licenses/public/naist-2003/#license-text"
        ),
    ),  # type: ignore
    "https://enterprise.dejacode.com/licenses/public/naist-2003/#license-text": CreativeWork(
        identifier="NAIST-2003",
        name="Nara Institute of Science and Technology License (2003)",
        url=AnyUrl(
            "https://enterprise.dejacode.com/licenses/public/naist-2003/#license-text"
        ),
    ),  # type: ignore
    "NASA-1.3": CreativeWork(
        identifier="NASA-1.3",
        name="NASA Open Source Agreement 1.3",
        url=AnyUrl("http://ti.arc.nasa.gov/opensource/nosa/"),
    ),  # type: ignore
    "https://spdx.org/licenses/NASA-1.3": CreativeWork(
        identifier="NASA-1.3",
        name="NASA Open Source Agreement 1.3",
        url=AnyUrl("http://ti.arc.nasa.gov/opensource/nosa/"),
    ),  # type: ignore
    "https://spdx.org/licenses/NASA-1.3.html": CreativeWork(
        identifier="NASA-1.3",
        name="NASA Open Source Agreement 1.3",
        url=AnyUrl("http://ti.arc.nasa.gov/opensource/nosa/"),
    ),  # type: ignore
    "http://ti.arc.nasa.gov/opensource/nosa/": CreativeWork(
        identifier="NASA-1.3",
        name="NASA Open Source Agreement 1.3",
        url=AnyUrl("http://ti.arc.nasa.gov/opensource/nosa/"),
    ),  # type: ignore
    "Naumen": CreativeWork(
        identifier="Naumen",
        name="Naumen Public License",
        url=AnyUrl("https://opensource.org/licenses/Naumen"),
    ),  # type: ignore
    "https://spdx.org/licenses/Naumen": CreativeWork(
        identifier="Naumen",
        name="Naumen Public License",
        url=AnyUrl("https://opensource.org/licenses/Naumen"),
    ),  # type: ignore
    "https://spdx.org/licenses/Naumen.html": CreativeWork(
        identifier="Naumen",
        name="Naumen Public License",
        url=AnyUrl("https://opensource.org/licenses/Naumen"),
    ),  # type: ignore
    "https://opensource.org/licenses/Naumen": CreativeWork(
        identifier="Naumen",
        name="Naumen Public License",
        url=AnyUrl("https://opensource.org/licenses/Naumen"),
    ),  # type: ignore
    "NBPL-1.0": CreativeWork(
        identifier="NBPL-1.0",
        name="Net Boolean Public License v1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=37b4b3f6cc4bf34e1d3dec61e69914b9819d8894"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NBPL-1.0": CreativeWork(
        identifier="NBPL-1.0",
        name="Net Boolean Public License v1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=37b4b3f6cc4bf34e1d3dec61e69914b9819d8894"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NBPL-1.0.html": CreativeWork(
        identifier="NBPL-1.0",
        name="Net Boolean Public License v1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=37b4b3f6cc4bf34e1d3dec61e69914b9819d8894"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=37b4b3f6cc4bf34e1d3dec61e69914b9819d8894": CreativeWork(
        identifier="NBPL-1.0",
        name="Net Boolean Public License v1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=37b4b3f6cc4bf34e1d3dec61e69914b9819d8894"
        ),
    ),  # type: ignore
    "NCBI-PD": CreativeWork(
        identifier="NCBI-PD",
        name="NCBI Public Domain Notice",
        url=AnyUrl(
            "https://github.com/ncbi/sra-tools/blob/e8e5b6af4edc460156ad9ce5902d0779cffbf685/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NCBI-PD": CreativeWork(
        identifier="NCBI-PD",
        name="NCBI Public Domain Notice",
        url=AnyUrl(
            "https://github.com/ncbi/sra-tools/blob/e8e5b6af4edc460156ad9ce5902d0779cffbf685/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NCBI-PD.html": CreativeWork(
        identifier="NCBI-PD",
        name="NCBI Public Domain Notice",
        url=AnyUrl(
            "https://github.com/ncbi/sra-tools/blob/e8e5b6af4edc460156ad9ce5902d0779cffbf685/LICENSE"
        ),
    ),  # type: ignore
    "https://github.com/ncbi/sra-tools/blob/e8e5b6af4edc460156ad9ce5902d0779cffbf685/LICENSE": CreativeWork(
        identifier="NCBI-PD",
        name="NCBI Public Domain Notice",
        url=AnyUrl(
            "https://github.com/ncbi/sra-tools/blob/e8e5b6af4edc460156ad9ce5902d0779cffbf685/LICENSE"
        ),
    ),  # type: ignore
    "NCGL-UK-2.0": CreativeWork(
        identifier="NCGL-UK-2.0",
        name="Non-Commercial Government Licence",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NCGL-UK-2.0": CreativeWork(
        identifier="NCGL-UK-2.0",
        name="Non-Commercial Government Licence",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NCGL-UK-2.0.html": CreativeWork(
        identifier="NCGL-UK-2.0",
        name="Non-Commercial Government Licence",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/"
        ),
    ),  # type: ignore
    "http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/": CreativeWork(
        identifier="NCGL-UK-2.0",
        name="Non-Commercial Government Licence",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/"
        ),
    ),  # type: ignore
    "NCL": CreativeWork(
        identifier="NCL",
        name="NCL Source Code License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/master/src/modules/module-filter-chain/pffft.c?ref_type=heads#L1-52"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NCL": CreativeWork(
        identifier="NCL",
        name="NCL Source Code License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/master/src/modules/module-filter-chain/pffft.c?ref_type=heads#L1-52"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NCL.html": CreativeWork(
        identifier="NCL",
        name="NCL Source Code License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/master/src/modules/module-filter-chain/pffft.c?ref_type=heads#L1-52"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/master/src/modules/module-filter-chain/pffft.c?ref_type=heads#L1-52": CreativeWork(
        identifier="NCL",
        name="NCL Source Code License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/master/src/modules/module-filter-chain/pffft.c?ref_type=heads#L1-52"
        ),
    ),  # type: ignore
    "NCSA": CreativeWork(
        identifier="NCSA",
        name="University of Illinois/NCSA Open Source License",
        url=AnyUrl("http://otm.illinois.edu/uiuc_openSource"),
    ),  # type: ignore
    "https://spdx.org/licenses/NCSA": CreativeWork(
        identifier="NCSA",
        name="University of Illinois/NCSA Open Source License",
        url=AnyUrl("http://otm.illinois.edu/uiuc_openSource"),
    ),  # type: ignore
    "https://spdx.org/licenses/NCSA.html": CreativeWork(
        identifier="NCSA",
        name="University of Illinois/NCSA Open Source License",
        url=AnyUrl("http://otm.illinois.edu/uiuc_openSource"),
    ),  # type: ignore
    "http://otm.illinois.edu/uiuc_openSource": CreativeWork(
        identifier="NCSA",
        name="University of Illinois/NCSA Open Source License",
        url=AnyUrl("http://otm.illinois.edu/uiuc_openSource"),
    ),  # type: ignore
    "Net-SNMP": CreativeWork(
        identifier="Net-SNMP",
        name="Net-SNMP License",
        url=AnyUrl("http://net-snmp.sourceforge.net/about/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Net-SNMP": CreativeWork(
        identifier="Net-SNMP",
        name="Net-SNMP License",
        url=AnyUrl("http://net-snmp.sourceforge.net/about/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Net-SNMP.html": CreativeWork(
        identifier="Net-SNMP",
        name="Net-SNMP License",
        url=AnyUrl("http://net-snmp.sourceforge.net/about/license.html"),
    ),  # type: ignore
    "http://net-snmp.sourceforge.net/about/license.html": CreativeWork(
        identifier="Net-SNMP",
        name="Net-SNMP License",
        url=AnyUrl("http://net-snmp.sourceforge.net/about/license.html"),
    ),  # type: ignore
    "NetCDF": CreativeWork(
        identifier="NetCDF",
        name="NetCDF license",
        url=AnyUrl("http://www.unidata.ucar.edu/software/netcdf/copyright.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/NetCDF": CreativeWork(
        identifier="NetCDF",
        name="NetCDF license",
        url=AnyUrl("http://www.unidata.ucar.edu/software/netcdf/copyright.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/NetCDF.html": CreativeWork(
        identifier="NetCDF",
        name="NetCDF license",
        url=AnyUrl("http://www.unidata.ucar.edu/software/netcdf/copyright.html"),
    ),  # type: ignore
    "http://www.unidata.ucar.edu/software/netcdf/copyright.html": CreativeWork(
        identifier="NetCDF",
        name="NetCDF license",
        url=AnyUrl("http://www.unidata.ucar.edu/software/netcdf/copyright.html"),
    ),  # type: ignore
    "Newsletr": CreativeWork(
        identifier="Newsletr",
        name="Newsletr License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Newsletr"),
    ),  # type: ignore
    "https://spdx.org/licenses/Newsletr": CreativeWork(
        identifier="Newsletr",
        name="Newsletr License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Newsletr"),
    ),  # type: ignore
    "https://spdx.org/licenses/Newsletr.html": CreativeWork(
        identifier="Newsletr",
        name="Newsletr License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Newsletr"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Newsletr": CreativeWork(
        identifier="Newsletr",
        name="Newsletr License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Newsletr"),
    ),  # type: ignore
    "NGPL": CreativeWork(
        identifier="NGPL",
        name="Nethack General Public License",
        url=AnyUrl("https://opensource.org/licenses/NGPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/NGPL": CreativeWork(
        identifier="NGPL",
        name="Nethack General Public License",
        url=AnyUrl("https://opensource.org/licenses/NGPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/NGPL.html": CreativeWork(
        identifier="NGPL",
        name="Nethack General Public License",
        url=AnyUrl("https://opensource.org/licenses/NGPL"),
    ),  # type: ignore
    "https://opensource.org/licenses/NGPL": CreativeWork(
        identifier="NGPL",
        name="Nethack General Public License",
        url=AnyUrl("https://opensource.org/licenses/NGPL"),
    ),  # type: ignore
    "ngrep": CreativeWork(
        identifier="ngrep",
        name="ngrep License",
        url=AnyUrl("https://github.com/jpr5/ngrep/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/ngrep": CreativeWork(
        identifier="ngrep",
        name="ngrep License",
        url=AnyUrl("https://github.com/jpr5/ngrep/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/ngrep.html": CreativeWork(
        identifier="ngrep",
        name="ngrep License",
        url=AnyUrl("https://github.com/jpr5/ngrep/blob/master/LICENSE"),
    ),  # type: ignore
    "https://github.com/jpr5/ngrep/blob/master/LICENSE": CreativeWork(
        identifier="ngrep",
        name="ngrep License",
        url=AnyUrl("https://github.com/jpr5/ngrep/blob/master/LICENSE"),
    ),  # type: ignore
    "NICTA-1.0": CreativeWork(
        identifier="NICTA-1.0",
        name="NICTA Public Software License, Version 1.0",
        url=AnyUrl(
            "https://opensource.apple.com/source/mDNSResponder/mDNSResponder-320.10/mDNSPosix/nss_ReadMe.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NICTA-1.0": CreativeWork(
        identifier="NICTA-1.0",
        name="NICTA Public Software License, Version 1.0",
        url=AnyUrl(
            "https://opensource.apple.com/source/mDNSResponder/mDNSResponder-320.10/mDNSPosix/nss_ReadMe.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NICTA-1.0.html": CreativeWork(
        identifier="NICTA-1.0",
        name="NICTA Public Software License, Version 1.0",
        url=AnyUrl(
            "https://opensource.apple.com/source/mDNSResponder/mDNSResponder-320.10/mDNSPosix/nss_ReadMe.txt"
        ),
    ),  # type: ignore
    "https://opensource.apple.com/source/mDNSResponder/mDNSResponder-320.10/mDNSPosix/nss_ReadMe.txt": CreativeWork(
        identifier="NICTA-1.0",
        name="NICTA Public Software License, Version 1.0",
        url=AnyUrl(
            "https://opensource.apple.com/source/mDNSResponder/mDNSResponder-320.10/mDNSPosix/nss_ReadMe.txt"
        ),
    ),  # type: ignore
    "NIST-PD": CreativeWork(
        identifier="NIST-PD",
        name="NIST Public Domain Notice",
        url=AnyUrl(
            "https://github.com/tcheneau/simpleRPL/blob/e645e69e38dd4e3ccfeceb2db8cba05b7c2e0cd3/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NIST-PD": CreativeWork(
        identifier="NIST-PD",
        name="NIST Public Domain Notice",
        url=AnyUrl(
            "https://github.com/tcheneau/simpleRPL/blob/e645e69e38dd4e3ccfeceb2db8cba05b7c2e0cd3/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NIST-PD.html": CreativeWork(
        identifier="NIST-PD",
        name="NIST Public Domain Notice",
        url=AnyUrl(
            "https://github.com/tcheneau/simpleRPL/blob/e645e69e38dd4e3ccfeceb2db8cba05b7c2e0cd3/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://github.com/tcheneau/simpleRPL/blob/e645e69e38dd4e3ccfeceb2db8cba05b7c2e0cd3/LICENSE.txt": CreativeWork(
        identifier="NIST-PD",
        name="NIST Public Domain Notice",
        url=AnyUrl(
            "https://github.com/tcheneau/simpleRPL/blob/e645e69e38dd4e3ccfeceb2db8cba05b7c2e0cd3/LICENSE.txt"
        ),
    ),  # type: ignore
    "NIST-PD-fallback": CreativeWork(
        identifier="NIST-PD-fallback",
        name="NIST Public Domain Notice with license fallback",
        url=AnyUrl(
            "https://github.com/usnistgov/jsip/blob/59700e6926cbe96c5cdae897d9a7d2656b42abe3/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NIST-PD-fallback": CreativeWork(
        identifier="NIST-PD-fallback",
        name="NIST Public Domain Notice with license fallback",
        url=AnyUrl(
            "https://github.com/usnistgov/jsip/blob/59700e6926cbe96c5cdae897d9a7d2656b42abe3/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NIST-PD-fallback.html": CreativeWork(
        identifier="NIST-PD-fallback",
        name="NIST Public Domain Notice with license fallback",
        url=AnyUrl(
            "https://github.com/usnistgov/jsip/blob/59700e6926cbe96c5cdae897d9a7d2656b42abe3/LICENSE"
        ),
    ),  # type: ignore
    "https://github.com/usnistgov/jsip/blob/59700e6926cbe96c5cdae897d9a7d2656b42abe3/LICENSE": CreativeWork(
        identifier="NIST-PD-fallback",
        name="NIST Public Domain Notice with license fallback",
        url=AnyUrl(
            "https://github.com/usnistgov/jsip/blob/59700e6926cbe96c5cdae897d9a7d2656b42abe3/LICENSE"
        ),
    ),  # type: ignore
    "NIST-PD-TNT": CreativeWork(
        identifier="NIST-PD-TNT",
        name="NIST    Public Domain Notice TNT variant",
        url=AnyUrl("https://math.nist.gov/tnt/download.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/NIST-PD-TNT": CreativeWork(
        identifier="NIST-PD-TNT",
        name="NIST    Public Domain Notice TNT variant",
        url=AnyUrl("https://math.nist.gov/tnt/download.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/NIST-PD-TNT.html": CreativeWork(
        identifier="NIST-PD-TNT",
        name="NIST    Public Domain Notice TNT variant",
        url=AnyUrl("https://math.nist.gov/tnt/download.html"),
    ),  # type: ignore
    "https://math.nist.gov/tnt/download.html": CreativeWork(
        identifier="NIST-PD-TNT",
        name="NIST    Public Domain Notice TNT variant",
        url=AnyUrl("https://math.nist.gov/tnt/download.html"),
    ),  # type: ignore
    "NIST-Software": CreativeWork(
        identifier="NIST-Software",
        name="NIST Software License",
        url=AnyUrl(
            "https://github.com/open-quantum-safe/liboqs/blob/40b01fdbb270f8614fde30e65d30e9da18c02393/src/common/rand/rand_nist.c#L1-L15"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NIST-Software": CreativeWork(
        identifier="NIST-Software",
        name="NIST Software License",
        url=AnyUrl(
            "https://github.com/open-quantum-safe/liboqs/blob/40b01fdbb270f8614fde30e65d30e9da18c02393/src/common/rand/rand_nist.c#L1-L15"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NIST-Software.html": CreativeWork(
        identifier="NIST-Software",
        name="NIST Software License",
        url=AnyUrl(
            "https://github.com/open-quantum-safe/liboqs/blob/40b01fdbb270f8614fde30e65d30e9da18c02393/src/common/rand/rand_nist.c#L1-L15"
        ),
    ),  # type: ignore
    "https://github.com/open-quantum-safe/liboqs/blob/40b01fdbb270f8614fde30e65d30e9da18c02393/src/common/rand/rand_nist.c#L1-L15": CreativeWork(
        identifier="NIST-Software",
        name="NIST Software License",
        url=AnyUrl(
            "https://github.com/open-quantum-safe/liboqs/blob/40b01fdbb270f8614fde30e65d30e9da18c02393/src/common/rand/rand_nist.c#L1-L15"
        ),
    ),  # type: ignore
    "NLOD-1.0": CreativeWork(
        identifier="NLOD-1.0",
        name="Norwegian Licence for Open Government Data (NLOD) 1.0",
        url=AnyUrl("http://data.norge.no/nlod/en/1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/NLOD-1.0": CreativeWork(
        identifier="NLOD-1.0",
        name="Norwegian Licence for Open Government Data (NLOD) 1.0",
        url=AnyUrl("http://data.norge.no/nlod/en/1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/NLOD-1.0.html": CreativeWork(
        identifier="NLOD-1.0",
        name="Norwegian Licence for Open Government Data (NLOD) 1.0",
        url=AnyUrl("http://data.norge.no/nlod/en/1.0"),
    ),  # type: ignore
    "http://data.norge.no/nlod/en/1.0": CreativeWork(
        identifier="NLOD-1.0",
        name="Norwegian Licence for Open Government Data (NLOD) 1.0",
        url=AnyUrl("http://data.norge.no/nlod/en/1.0"),
    ),  # type: ignore
    "NLOD-2.0": CreativeWork(
        identifier="NLOD-2.0",
        name="Norwegian Licence for Open Government Data (NLOD) 2.0",
        url=AnyUrl("http://data.norge.no/nlod/en/2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/NLOD-2.0": CreativeWork(
        identifier="NLOD-2.0",
        name="Norwegian Licence for Open Government Data (NLOD) 2.0",
        url=AnyUrl("http://data.norge.no/nlod/en/2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/NLOD-2.0.html": CreativeWork(
        identifier="NLOD-2.0",
        name="Norwegian Licence for Open Government Data (NLOD) 2.0",
        url=AnyUrl("http://data.norge.no/nlod/en/2.0"),
    ),  # type: ignore
    "http://data.norge.no/nlod/en/2.0": CreativeWork(
        identifier="NLOD-2.0",
        name="Norwegian Licence for Open Government Data (NLOD) 2.0",
        url=AnyUrl("http://data.norge.no/nlod/en/2.0"),
    ),  # type: ignore
    "NLPL": CreativeWork(
        identifier="NLPL",
        name="No Limit Public License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/NLPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/NLPL": CreativeWork(
        identifier="NLPL",
        name="No Limit Public License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/NLPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/NLPL.html": CreativeWork(
        identifier="NLPL",
        name="No Limit Public License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/NLPL"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/NLPL": CreativeWork(
        identifier="NLPL",
        name="No Limit Public License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/NLPL"),
    ),  # type: ignore
    "Nokia": CreativeWork(
        identifier="Nokia",
        name="Nokia Open Source License",
        url=AnyUrl("https://opensource.org/licenses/nokia"),
    ),  # type: ignore
    "https://spdx.org/licenses/Nokia": CreativeWork(
        identifier="Nokia",
        name="Nokia Open Source License",
        url=AnyUrl("https://opensource.org/licenses/nokia"),
    ),  # type: ignore
    "https://spdx.org/licenses/Nokia.html": CreativeWork(
        identifier="Nokia",
        name="Nokia Open Source License",
        url=AnyUrl("https://opensource.org/licenses/nokia"),
    ),  # type: ignore
    "https://opensource.org/licenses/nokia": CreativeWork(
        identifier="Nokia",
        name="Nokia Open Source License",
        url=AnyUrl("https://opensource.org/licenses/nokia"),
    ),  # type: ignore
    "NOSL": CreativeWork(
        identifier="NOSL",
        name="Netizen Open Source License",
        url=AnyUrl("http://bits.netizen.com.au/licenses/NOSL/nosl.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/NOSL": CreativeWork(
        identifier="NOSL",
        name="Netizen Open Source License",
        url=AnyUrl("http://bits.netizen.com.au/licenses/NOSL/nosl.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/NOSL.html": CreativeWork(
        identifier="NOSL",
        name="Netizen Open Source License",
        url=AnyUrl("http://bits.netizen.com.au/licenses/NOSL/nosl.txt"),
    ),  # type: ignore
    "http://bits.netizen.com.au/licenses/NOSL/nosl.txt": CreativeWork(
        identifier="NOSL",
        name="Netizen Open Source License",
        url=AnyUrl("http://bits.netizen.com.au/licenses/NOSL/nosl.txt"),
    ),  # type: ignore
    "Noweb": CreativeWork(
        identifier="Noweb",
        name="Noweb License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Noweb"),
    ),  # type: ignore
    "https://spdx.org/licenses/Noweb": CreativeWork(
        identifier="Noweb",
        name="Noweb License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Noweb"),
    ),  # type: ignore
    "https://spdx.org/licenses/Noweb.html": CreativeWork(
        identifier="Noweb",
        name="Noweb License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Noweb"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Noweb": CreativeWork(
        identifier="Noweb",
        name="Noweb License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Noweb"),
    ),  # type: ignore
    "NPL-1.0": CreativeWork(
        identifier="NPL-1.0",
        name="Netscape Public License v1.0",
        url=AnyUrl("http://www.mozilla.org/MPL/NPL/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/NPL-1.0": CreativeWork(
        identifier="NPL-1.0",
        name="Netscape Public License v1.0",
        url=AnyUrl("http://www.mozilla.org/MPL/NPL/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/NPL-1.0.html": CreativeWork(
        identifier="NPL-1.0",
        name="Netscape Public License v1.0",
        url=AnyUrl("http://www.mozilla.org/MPL/NPL/1.0/"),
    ),  # type: ignore
    "http://www.mozilla.org/MPL/NPL/1.0/": CreativeWork(
        identifier="NPL-1.0",
        name="Netscape Public License v1.0",
        url=AnyUrl("http://www.mozilla.org/MPL/NPL/1.0/"),
    ),  # type: ignore
    "NPL-1.1": CreativeWork(
        identifier="NPL-1.1",
        name="Netscape Public License v1.1",
        url=AnyUrl("http://www.mozilla.org/MPL/NPL/1.1/"),
    ),  # type: ignore
    "https://spdx.org/licenses/NPL-1.1": CreativeWork(
        identifier="NPL-1.1",
        name="Netscape Public License v1.1",
        url=AnyUrl("http://www.mozilla.org/MPL/NPL/1.1/"),
    ),  # type: ignore
    "https://spdx.org/licenses/NPL-1.1.html": CreativeWork(
        identifier="NPL-1.1",
        name="Netscape Public License v1.1",
        url=AnyUrl("http://www.mozilla.org/MPL/NPL/1.1/"),
    ),  # type: ignore
    "http://www.mozilla.org/MPL/NPL/1.1/": CreativeWork(
        identifier="NPL-1.1",
        name="Netscape Public License v1.1",
        url=AnyUrl("http://www.mozilla.org/MPL/NPL/1.1/"),
    ),  # type: ignore
    "NPOSL-3.0": CreativeWork(
        identifier="NPOSL-3.0",
        name="Non-Profit Open Software License 3.0",
        url=AnyUrl("https://opensource.org/licenses/NOSL3.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/NPOSL-3.0": CreativeWork(
        identifier="NPOSL-3.0",
        name="Non-Profit Open Software License 3.0",
        url=AnyUrl("https://opensource.org/licenses/NOSL3.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/NPOSL-3.0.html": CreativeWork(
        identifier="NPOSL-3.0",
        name="Non-Profit Open Software License 3.0",
        url=AnyUrl("https://opensource.org/licenses/NOSL3.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/NOSL3.0": CreativeWork(
        identifier="NPOSL-3.0",
        name="Non-Profit Open Software License 3.0",
        url=AnyUrl("https://opensource.org/licenses/NOSL3.0"),
    ),  # type: ignore
    "NRL": CreativeWork(
        identifier="NRL",
        name="NRL License",
        url=AnyUrl("http://web.mit.edu/network/isakmp/nrllicense.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/NRL": CreativeWork(
        identifier="NRL",
        name="NRL License",
        url=AnyUrl("http://web.mit.edu/network/isakmp/nrllicense.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/NRL.html": CreativeWork(
        identifier="NRL",
        name="NRL License",
        url=AnyUrl("http://web.mit.edu/network/isakmp/nrllicense.html"),
    ),  # type: ignore
    "http://web.mit.edu/network/isakmp/nrllicense.html": CreativeWork(
        identifier="NRL",
        name="NRL License",
        url=AnyUrl("http://web.mit.edu/network/isakmp/nrllicense.html"),
    ),  # type: ignore
    "NTIA-PD": CreativeWork(
        identifier="NTIA-PD",
        name="NTIA Public Domain Notice",
        url=AnyUrl(
            "https://raw.githubusercontent.com/NTIA/itm/refs/heads/master/LICENSE.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NTIA-PD": CreativeWork(
        identifier="NTIA-PD",
        name="NTIA Public Domain Notice",
        url=AnyUrl(
            "https://raw.githubusercontent.com/NTIA/itm/refs/heads/master/LICENSE.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/NTIA-PD.html": CreativeWork(
        identifier="NTIA-PD",
        name="NTIA Public Domain Notice",
        url=AnyUrl(
            "https://raw.githubusercontent.com/NTIA/itm/refs/heads/master/LICENSE.md"
        ),
    ),  # type: ignore
    "https://raw.githubusercontent.com/NTIA/itm/refs/heads/master/LICENSE.md": CreativeWork(
        identifier="NTIA-PD",
        name="NTIA Public Domain Notice",
        url=AnyUrl(
            "https://raw.githubusercontent.com/NTIA/itm/refs/heads/master/LICENSE.md"
        ),
    ),  # type: ignore
    "NTP": CreativeWork(
        identifier="NTP",
        name="NTP License",
        url=AnyUrl("https://opensource.org/licenses/NTP"),
    ),  # type: ignore
    "https://spdx.org/licenses/NTP": CreativeWork(
        identifier="NTP",
        name="NTP License",
        url=AnyUrl("https://opensource.org/licenses/NTP"),
    ),  # type: ignore
    "https://spdx.org/licenses/NTP.html": CreativeWork(
        identifier="NTP",
        name="NTP License",
        url=AnyUrl("https://opensource.org/licenses/NTP"),
    ),  # type: ignore
    "https://opensource.org/licenses/NTP": CreativeWork(
        identifier="NTP",
        name="NTP License",
        url=AnyUrl("https://opensource.org/licenses/NTP"),
    ),  # type: ignore
    "NTP-0": CreativeWork(
        identifier="NTP-0",
        name="NTP No Attribution",
        url=AnyUrl("https://github.com/tytso/e2fsprogs/blob/master/lib/et/et_name.c"),
    ),  # type: ignore
    "https://spdx.org/licenses/NTP-0": CreativeWork(
        identifier="NTP-0",
        name="NTP No Attribution",
        url=AnyUrl("https://github.com/tytso/e2fsprogs/blob/master/lib/et/et_name.c"),
    ),  # type: ignore
    "https://spdx.org/licenses/NTP-0.html": CreativeWork(
        identifier="NTP-0",
        name="NTP No Attribution",
        url=AnyUrl("https://github.com/tytso/e2fsprogs/blob/master/lib/et/et_name.c"),
    ),  # type: ignore
    "https://github.com/tytso/e2fsprogs/blob/master/lib/et/et_name.c": CreativeWork(
        identifier="NTP-0",
        name="NTP No Attribution",
        url=AnyUrl("https://github.com/tytso/e2fsprogs/blob/master/lib/et/et_name.c"),
    ),  # type: ignore
    "Nunit": CreativeWork(
        identifier="Nunit",
        name="Nunit License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Nunit"),
    ),  # type: ignore
    "https://spdx.org/licenses/Nunit": CreativeWork(
        identifier="Nunit",
        name="Nunit License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Nunit"),
    ),  # type: ignore
    "https://spdx.org/licenses/Nunit.html": CreativeWork(
        identifier="Nunit",
        name="Nunit License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Nunit"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Nunit": CreativeWork(
        identifier="Nunit",
        name="Nunit License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Nunit"),
    ),  # type: ignore
    "O-UDA-1.0": CreativeWork(
        identifier="O-UDA-1.0",
        name="Open Use of Data Agreement v1.0",
        url=AnyUrl(
            "https://github.com/microsoft/Open-Use-of-Data-Agreement/blob/v1.0/O-UDA-1.0.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/O-UDA-1.0": CreativeWork(
        identifier="O-UDA-1.0",
        name="Open Use of Data Agreement v1.0",
        url=AnyUrl(
            "https://github.com/microsoft/Open-Use-of-Data-Agreement/blob/v1.0/O-UDA-1.0.md"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/O-UDA-1.0.html": CreativeWork(
        identifier="O-UDA-1.0",
        name="Open Use of Data Agreement v1.0",
        url=AnyUrl(
            "https://github.com/microsoft/Open-Use-of-Data-Agreement/blob/v1.0/O-UDA-1.0.md"
        ),
    ),  # type: ignore
    "https://github.com/microsoft/Open-Use-of-Data-Agreement/blob/v1.0/O-UDA-1.0.md": CreativeWork(
        identifier="O-UDA-1.0",
        name="Open Use of Data Agreement v1.0",
        url=AnyUrl(
            "https://github.com/microsoft/Open-Use-of-Data-Agreement/blob/v1.0/O-UDA-1.0.md"
        ),
    ),  # type: ignore
    "OAR": CreativeWork(
        identifier="OAR",
        name="OAR License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/string/strsignal.c;hb=HEAD#l35"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OAR": CreativeWork(
        identifier="OAR",
        name="OAR License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/string/strsignal.c;hb=HEAD#l35"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OAR.html": CreativeWork(
        identifier="OAR",
        name="OAR License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/string/strsignal.c;hb=HEAD#l35"
        ),
    ),  # type: ignore
    "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/string/strsignal.c;hb=HEAD#l35": CreativeWork(
        identifier="OAR",
        name="OAR License",
        url=AnyUrl(
            "https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/string/strsignal.c;hb=HEAD#l35"
        ),
    ),  # type: ignore
    "OCCT-PL": CreativeWork(
        identifier="OCCT-PL",
        name="Open CASCADE Technology Public License",
        url=AnyUrl("http://www.opencascade.com/content/occt-public-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/OCCT-PL": CreativeWork(
        identifier="OCCT-PL",
        name="Open CASCADE Technology Public License",
        url=AnyUrl("http://www.opencascade.com/content/occt-public-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/OCCT-PL.html": CreativeWork(
        identifier="OCCT-PL",
        name="Open CASCADE Technology Public License",
        url=AnyUrl("http://www.opencascade.com/content/occt-public-license"),
    ),  # type: ignore
    "http://www.opencascade.com/content/occt-public-license": CreativeWork(
        identifier="OCCT-PL",
        name="Open CASCADE Technology Public License",
        url=AnyUrl("http://www.opencascade.com/content/occt-public-license"),
    ),  # type: ignore
    "OCLC-2.0": CreativeWork(
        identifier="OCLC-2.0",
        name="OCLC Research Public License 2.0",
        url=AnyUrl(
            "http://www.oclc.org/research/activities/software/license/v2final.htm"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OCLC-2.0": CreativeWork(
        identifier="OCLC-2.0",
        name="OCLC Research Public License 2.0",
        url=AnyUrl(
            "http://www.oclc.org/research/activities/software/license/v2final.htm"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OCLC-2.0.html": CreativeWork(
        identifier="OCLC-2.0",
        name="OCLC Research Public License 2.0",
        url=AnyUrl(
            "http://www.oclc.org/research/activities/software/license/v2final.htm"
        ),
    ),  # type: ignore
    "http://www.oclc.org/research/activities/software/license/v2final.htm": CreativeWork(
        identifier="OCLC-2.0",
        name="OCLC Research Public License 2.0",
        url=AnyUrl(
            "http://www.oclc.org/research/activities/software/license/v2final.htm"
        ),
    ),  # type: ignore
    "ODbL-1.0": CreativeWork(
        identifier="ODbL-1.0",
        name="Open Data Commons Open Database License v1.0",
        url=AnyUrl("http://www.opendatacommons.org/licenses/odbl/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/ODbL-1.0": CreativeWork(
        identifier="ODbL-1.0",
        name="Open Data Commons Open Database License v1.0",
        url=AnyUrl("http://www.opendatacommons.org/licenses/odbl/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/ODbL-1.0.html": CreativeWork(
        identifier="ODbL-1.0",
        name="Open Data Commons Open Database License v1.0",
        url=AnyUrl("http://www.opendatacommons.org/licenses/odbl/1.0/"),
    ),  # type: ignore
    "http://www.opendatacommons.org/licenses/odbl/1.0/": CreativeWork(
        identifier="ODbL-1.0",
        name="Open Data Commons Open Database License v1.0",
        url=AnyUrl("http://www.opendatacommons.org/licenses/odbl/1.0/"),
    ),  # type: ignore
    "ODC-By-1.0": CreativeWork(
        identifier="ODC-By-1.0",
        name="Open Data Commons Attribution License v1.0",
        url=AnyUrl("https://opendatacommons.org/licenses/by/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/ODC-By-1.0": CreativeWork(
        identifier="ODC-By-1.0",
        name="Open Data Commons Attribution License v1.0",
        url=AnyUrl("https://opendatacommons.org/licenses/by/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/ODC-By-1.0.html": CreativeWork(
        identifier="ODC-By-1.0",
        name="Open Data Commons Attribution License v1.0",
        url=AnyUrl("https://opendatacommons.org/licenses/by/1.0/"),
    ),  # type: ignore
    "https://opendatacommons.org/licenses/by/1.0/": CreativeWork(
        identifier="ODC-By-1.0",
        name="Open Data Commons Attribution License v1.0",
        url=AnyUrl("https://opendatacommons.org/licenses/by/1.0/"),
    ),  # type: ignore
    "OFFIS": CreativeWork(
        identifier="OFFIS",
        name="OFFIS License",
        url=AnyUrl(
            "https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/dicom/README"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OFFIS": CreativeWork(
        identifier="OFFIS",
        name="OFFIS License",
        url=AnyUrl(
            "https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/dicom/README"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OFFIS.html": CreativeWork(
        identifier="OFFIS",
        name="OFFIS License",
        url=AnyUrl(
            "https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/dicom/README"
        ),
    ),  # type: ignore
    "https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/dicom/README": CreativeWork(
        identifier="OFFIS",
        name="OFFIS License",
        url=AnyUrl(
            "https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/dicom/README"
        ),
    ),  # type: ignore
    "OFL-1.0": CreativeWork(
        identifier="OFL-1.0",
        name="SIL Open Font License 1.0",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.0": CreativeWork(
        identifier="OFL-1.0",
        name="SIL Open Font License 1.0",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.0.html": CreativeWork(
        identifier="OFL-1.0",
        name="SIL Open Font License 1.0",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web": CreativeWork(
        identifier="OFL-1.0",
        name="SIL Open Font License 1.0",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "OFL-1.0-no-RFN": CreativeWork(
        identifier="OFL-1.0-no-RFN",
        name="SIL Open Font License 1.0 with no Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.0-no-RFN": CreativeWork(
        identifier="OFL-1.0-no-RFN",
        name="SIL Open Font License 1.0 with no Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.0-no-RFN.html": CreativeWork(
        identifier="OFL-1.0-no-RFN",
        name="SIL Open Font License 1.0 with no Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "OFL-1.0-RFN": CreativeWork(
        identifier="OFL-1.0-RFN",
        name="SIL Open Font License 1.0 with Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.0-RFN": CreativeWork(
        identifier="OFL-1.0-RFN",
        name="SIL Open Font License 1.0 with Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.0-RFN.html": CreativeWork(
        identifier="OFL-1.0-RFN",
        name="SIL Open Font License 1.0 with Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web"),
    ),  # type: ignore
    "OFL-1.1": CreativeWork(
        identifier="OFL-1.1",
        name="SIL Open Font License 1.1",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.1": CreativeWork(
        identifier="OFL-1.1",
        name="SIL Open Font License 1.1",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.1.html": CreativeWork(
        identifier="OFL-1.1",
        name="SIL Open Font License 1.1",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web": CreativeWork(
        identifier="OFL-1.1",
        name="SIL Open Font License 1.1",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "OFL-1.1-no-RFN": CreativeWork(
        identifier="OFL-1.1-no-RFN",
        name="SIL Open Font License 1.1 with no Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.1-no-RFN": CreativeWork(
        identifier="OFL-1.1-no-RFN",
        name="SIL Open Font License 1.1 with no Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.1-no-RFN.html": CreativeWork(
        identifier="OFL-1.1-no-RFN",
        name="SIL Open Font License 1.1 with no Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "OFL-1.1-RFN": CreativeWork(
        identifier="OFL-1.1-RFN",
        name="SIL Open Font License 1.1 with Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.1-RFN": CreativeWork(
        identifier="OFL-1.1-RFN",
        name="SIL Open Font License 1.1 with Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "https://spdx.org/licenses/OFL-1.1-RFN.html": CreativeWork(
        identifier="OFL-1.1-RFN",
        name="SIL Open Font License 1.1 with Reserved Font Name",
        url=AnyUrl("http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web"),
    ),  # type: ignore
    "OGC-1.0": CreativeWork(
        identifier="OGC-1.0",
        name="OGC Software License, Version 1.0",
        url=AnyUrl("https://www.ogc.org/ogc/software/1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/OGC-1.0": CreativeWork(
        identifier="OGC-1.0",
        name="OGC Software License, Version 1.0",
        url=AnyUrl("https://www.ogc.org/ogc/software/1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/OGC-1.0.html": CreativeWork(
        identifier="OGC-1.0",
        name="OGC Software License, Version 1.0",
        url=AnyUrl("https://www.ogc.org/ogc/software/1.0"),
    ),  # type: ignore
    "https://www.ogc.org/ogc/software/1.0": CreativeWork(
        identifier="OGC-1.0",
        name="OGC Software License, Version 1.0",
        url=AnyUrl("https://www.ogc.org/ogc/software/1.0"),
    ),  # type: ignore
    "OGDL-Taiwan-1.0": CreativeWork(
        identifier="OGDL-Taiwan-1.0",
        name="Taiwan Open Government Data License, version 1.0",
        url=AnyUrl("https://data.gov.tw/license"),
    ),  # type: ignore
    "https://spdx.org/licenses/OGDL-Taiwan-1.0": CreativeWork(
        identifier="OGDL-Taiwan-1.0",
        name="Taiwan Open Government Data License, version 1.0",
        url=AnyUrl("https://data.gov.tw/license"),
    ),  # type: ignore
    "https://spdx.org/licenses/OGDL-Taiwan-1.0.html": CreativeWork(
        identifier="OGDL-Taiwan-1.0",
        name="Taiwan Open Government Data License, version 1.0",
        url=AnyUrl("https://data.gov.tw/license"),
    ),  # type: ignore
    "https://data.gov.tw/license": CreativeWork(
        identifier="OGDL-Taiwan-1.0",
        name="Taiwan Open Government Data License, version 1.0",
        url=AnyUrl("https://data.gov.tw/license"),
    ),  # type: ignore
    "OGL-Canada-2.0": CreativeWork(
        identifier="OGL-Canada-2.0",
        name="Open Government Licence - Canada",
        url=AnyUrl("https://open.canada.ca/en/open-government-licence-canada"),
    ),  # type: ignore
    "https://spdx.org/licenses/OGL-Canada-2.0": CreativeWork(
        identifier="OGL-Canada-2.0",
        name="Open Government Licence - Canada",
        url=AnyUrl("https://open.canada.ca/en/open-government-licence-canada"),
    ),  # type: ignore
    "https://spdx.org/licenses/OGL-Canada-2.0.html": CreativeWork(
        identifier="OGL-Canada-2.0",
        name="Open Government Licence - Canada",
        url=AnyUrl("https://open.canada.ca/en/open-government-licence-canada"),
    ),  # type: ignore
    "https://open.canada.ca/en/open-government-licence-canada": CreativeWork(
        identifier="OGL-Canada-2.0",
        name="Open Government Licence - Canada",
        url=AnyUrl("https://open.canada.ca/en/open-government-licence-canada"),
    ),  # type: ignore
    "OGL-UK-1.0": CreativeWork(
        identifier="OGL-UK-1.0",
        name="Open Government Licence v1.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OGL-UK-1.0": CreativeWork(
        identifier="OGL-UK-1.0",
        name="Open Government Licence v1.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OGL-UK-1.0.html": CreativeWork(
        identifier="OGL-UK-1.0",
        name="Open Government Licence v1.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/"
        ),
    ),  # type: ignore
    "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/": CreativeWork(
        identifier="OGL-UK-1.0",
        name="Open Government Licence v1.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/"
        ),
    ),  # type: ignore
    "OGL-UK-2.0": CreativeWork(
        identifier="OGL-UK-2.0",
        name="Open Government Licence v2.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OGL-UK-2.0": CreativeWork(
        identifier="OGL-UK-2.0",
        name="Open Government Licence v2.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OGL-UK-2.0.html": CreativeWork(
        identifier="OGL-UK-2.0",
        name="Open Government Licence v2.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/"
        ),
    ),  # type: ignore
    "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/": CreativeWork(
        identifier="OGL-UK-2.0",
        name="Open Government Licence v2.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/"
        ),
    ),  # type: ignore
    "OGL-UK-3.0": CreativeWork(
        identifier="OGL-UK-3.0",
        name="Open Government Licence v3.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OGL-UK-3.0": CreativeWork(
        identifier="OGL-UK-3.0",
        name="Open Government Licence v3.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OGL-UK-3.0.html": CreativeWork(
        identifier="OGL-UK-3.0",
        name="Open Government Licence v3.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
        ),
    ),  # type: ignore
    "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/": CreativeWork(
        identifier="OGL-UK-3.0",
        name="Open Government Licence v3.0",
        url=AnyUrl(
            "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
        ),
    ),  # type: ignore
    "OGTSL": CreativeWork(
        identifier="OGTSL",
        name="Open Group Test Suite License",
        url=AnyUrl("http://www.opengroup.org/testing/downloads/The_Open_Group_TSL.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/OGTSL": CreativeWork(
        identifier="OGTSL",
        name="Open Group Test Suite License",
        url=AnyUrl("http://www.opengroup.org/testing/downloads/The_Open_Group_TSL.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/OGTSL.html": CreativeWork(
        identifier="OGTSL",
        name="Open Group Test Suite License",
        url=AnyUrl("http://www.opengroup.org/testing/downloads/The_Open_Group_TSL.txt"),
    ),  # type: ignore
    "http://www.opengroup.org/testing/downloads/The_Open_Group_TSL.txt": CreativeWork(
        identifier="OGTSL",
        name="Open Group Test Suite License",
        url=AnyUrl("http://www.opengroup.org/testing/downloads/The_Open_Group_TSL.txt"),
    ),  # type: ignore
    "OLDAP-1.1": CreativeWork(
        identifier="OLDAP-1.1",
        name="Open LDAP Public License v1.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=806557a5ad59804ef3a44d5abfbe91d706b0791f"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-1.1": CreativeWork(
        identifier="OLDAP-1.1",
        name="Open LDAP Public License v1.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=806557a5ad59804ef3a44d5abfbe91d706b0791f"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-1.1.html": CreativeWork(
        identifier="OLDAP-1.1",
        name="Open LDAP Public License v1.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=806557a5ad59804ef3a44d5abfbe91d706b0791f"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=806557a5ad59804ef3a44d5abfbe91d706b0791f": CreativeWork(
        identifier="OLDAP-1.1",
        name="Open LDAP Public License v1.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=806557a5ad59804ef3a44d5abfbe91d706b0791f"
        ),
    ),  # type: ignore
    "OLDAP-1.2": CreativeWork(
        identifier="OLDAP-1.2",
        name="Open LDAP Public License v1.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=42b0383c50c299977b5893ee695cf4e486fb0dc7"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-1.2": CreativeWork(
        identifier="OLDAP-1.2",
        name="Open LDAP Public License v1.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=42b0383c50c299977b5893ee695cf4e486fb0dc7"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-1.2.html": CreativeWork(
        identifier="OLDAP-1.2",
        name="Open LDAP Public License v1.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=42b0383c50c299977b5893ee695cf4e486fb0dc7"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=42b0383c50c299977b5893ee695cf4e486fb0dc7": CreativeWork(
        identifier="OLDAP-1.2",
        name="Open LDAP Public License v1.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=42b0383c50c299977b5893ee695cf4e486fb0dc7"
        ),
    ),  # type: ignore
    "OLDAP-1.3": CreativeWork(
        identifier="OLDAP-1.3",
        name="Open LDAP Public License v1.3",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=e5f8117f0ce088d0bd7a8e18ddf37eaa40eb09b1"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-1.3": CreativeWork(
        identifier="OLDAP-1.3",
        name="Open LDAP Public License v1.3",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=e5f8117f0ce088d0bd7a8e18ddf37eaa40eb09b1"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-1.3.html": CreativeWork(
        identifier="OLDAP-1.3",
        name="Open LDAP Public License v1.3",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=e5f8117f0ce088d0bd7a8e18ddf37eaa40eb09b1"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=e5f8117f0ce088d0bd7a8e18ddf37eaa40eb09b1": CreativeWork(
        identifier="OLDAP-1.3",
        name="Open LDAP Public License v1.3",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=e5f8117f0ce088d0bd7a8e18ddf37eaa40eb09b1"
        ),
    ),  # type: ignore
    "OLDAP-1.4": CreativeWork(
        identifier="OLDAP-1.4",
        name="Open LDAP Public License v1.4",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=c9f95c2f3f2ffb5e0ae55fe7388af75547660941"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-1.4": CreativeWork(
        identifier="OLDAP-1.4",
        name="Open LDAP Public License v1.4",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=c9f95c2f3f2ffb5e0ae55fe7388af75547660941"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-1.4.html": CreativeWork(
        identifier="OLDAP-1.4",
        name="Open LDAP Public License v1.4",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=c9f95c2f3f2ffb5e0ae55fe7388af75547660941"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=c9f95c2f3f2ffb5e0ae55fe7388af75547660941": CreativeWork(
        identifier="OLDAP-1.4",
        name="Open LDAP Public License v1.4",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=c9f95c2f3f2ffb5e0ae55fe7388af75547660941"
        ),
    ),  # type: ignore
    "OLDAP-2.0": CreativeWork(
        identifier="OLDAP-2.0",
        name="Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cbf50f4e1185a21abd4c0a54d3f4341fe28f36ea"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.0": CreativeWork(
        identifier="OLDAP-2.0",
        name="Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cbf50f4e1185a21abd4c0a54d3f4341fe28f36ea"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.0.html": CreativeWork(
        identifier="OLDAP-2.0",
        name="Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cbf50f4e1185a21abd4c0a54d3f4341fe28f36ea"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cbf50f4e1185a21abd4c0a54d3f4341fe28f36ea": CreativeWork(
        identifier="OLDAP-2.0",
        name="Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cbf50f4e1185a21abd4c0a54d3f4341fe28f36ea"
        ),
    ),  # type: ignore
    "OLDAP-2.0.1": CreativeWork(
        identifier="OLDAP-2.0.1",
        name="Open LDAP Public License v2.0.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b6d68acd14e51ca3aab4428bf26522aa74873f0e"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.0.1": CreativeWork(
        identifier="OLDAP-2.0.1",
        name="Open LDAP Public License v2.0.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b6d68acd14e51ca3aab4428bf26522aa74873f0e"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.0.1.html": CreativeWork(
        identifier="OLDAP-2.0.1",
        name="Open LDAP Public License v2.0.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b6d68acd14e51ca3aab4428bf26522aa74873f0e"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b6d68acd14e51ca3aab4428bf26522aa74873f0e": CreativeWork(
        identifier="OLDAP-2.0.1",
        name="Open LDAP Public License v2.0.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b6d68acd14e51ca3aab4428bf26522aa74873f0e"
        ),
    ),  # type: ignore
    "OLDAP-2.1": CreativeWork(
        identifier="OLDAP-2.1",
        name="Open LDAP Public License v2.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b0d176738e96a0d3b9f85cb51e140a86f21be715"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.1": CreativeWork(
        identifier="OLDAP-2.1",
        name="Open LDAP Public License v2.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b0d176738e96a0d3b9f85cb51e140a86f21be715"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.1.html": CreativeWork(
        identifier="OLDAP-2.1",
        name="Open LDAP Public License v2.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b0d176738e96a0d3b9f85cb51e140a86f21be715"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b0d176738e96a0d3b9f85cb51e140a86f21be715": CreativeWork(
        identifier="OLDAP-2.1",
        name="Open LDAP Public License v2.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b0d176738e96a0d3b9f85cb51e140a86f21be715"
        ),
    ),  # type: ignore
    "OLDAP-2.2": CreativeWork(
        identifier="OLDAP-2.2",
        name="Open LDAP Public License v2.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=470b0c18ec67621c85881b2733057fecf4a1acc3"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.2": CreativeWork(
        identifier="OLDAP-2.2",
        name="Open LDAP Public License v2.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=470b0c18ec67621c85881b2733057fecf4a1acc3"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.2.html": CreativeWork(
        identifier="OLDAP-2.2",
        name="Open LDAP Public License v2.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=470b0c18ec67621c85881b2733057fecf4a1acc3"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=470b0c18ec67621c85881b2733057fecf4a1acc3": CreativeWork(
        identifier="OLDAP-2.2",
        name="Open LDAP Public License v2.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=470b0c18ec67621c85881b2733057fecf4a1acc3"
        ),
    ),  # type: ignore
    "OLDAP-2.2.1": CreativeWork(
        identifier="OLDAP-2.2.1",
        name="Open LDAP Public License v2.2.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=4bc786f34b50aa301be6f5600f58a980070f481e"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.2.1": CreativeWork(
        identifier="OLDAP-2.2.1",
        name="Open LDAP Public License v2.2.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=4bc786f34b50aa301be6f5600f58a980070f481e"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.2.1.html": CreativeWork(
        identifier="OLDAP-2.2.1",
        name="Open LDAP Public License v2.2.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=4bc786f34b50aa301be6f5600f58a980070f481e"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=4bc786f34b50aa301be6f5600f58a980070f481e": CreativeWork(
        identifier="OLDAP-2.2.1",
        name="Open LDAP Public License v2.2.1",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=4bc786f34b50aa301be6f5600f58a980070f481e"
        ),
    ),  # type: ignore
    "OLDAP-2.2.2": CreativeWork(
        identifier="OLDAP-2.2.2",
        name="Open LDAP Public License 2.2.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=df2cc1e21eb7c160695f5b7cffd6296c151ba188"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.2.2": CreativeWork(
        identifier="OLDAP-2.2.2",
        name="Open LDAP Public License 2.2.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=df2cc1e21eb7c160695f5b7cffd6296c151ba188"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.2.2.html": CreativeWork(
        identifier="OLDAP-2.2.2",
        name="Open LDAP Public License 2.2.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=df2cc1e21eb7c160695f5b7cffd6296c151ba188"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=df2cc1e21eb7c160695f5b7cffd6296c151ba188": CreativeWork(
        identifier="OLDAP-2.2.2",
        name="Open LDAP Public License 2.2.2",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=df2cc1e21eb7c160695f5b7cffd6296c151ba188"
        ),
    ),  # type: ignore
    "OLDAP-2.3": CreativeWork(
        identifier="OLDAP-2.3",
        name="Open LDAP Public License v2.3",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=d32cf54a32d581ab475d23c810b0a7fbaf8d63c3"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.3": CreativeWork(
        identifier="OLDAP-2.3",
        name="Open LDAP Public License v2.3",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=d32cf54a32d581ab475d23c810b0a7fbaf8d63c3"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.3.html": CreativeWork(
        identifier="OLDAP-2.3",
        name="Open LDAP Public License v2.3",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=d32cf54a32d581ab475d23c810b0a7fbaf8d63c3"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=d32cf54a32d581ab475d23c810b0a7fbaf8d63c3": CreativeWork(
        identifier="OLDAP-2.3",
        name="Open LDAP Public License v2.3",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=d32cf54a32d581ab475d23c810b0a7fbaf8d63c3"
        ),
    ),  # type: ignore
    "OLDAP-2.4": CreativeWork(
        identifier="OLDAP-2.4",
        name="Open LDAP Public License v2.4",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cd1284c4a91a8a380d904eee68d1583f989ed386"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.4": CreativeWork(
        identifier="OLDAP-2.4",
        name="Open LDAP Public License v2.4",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cd1284c4a91a8a380d904eee68d1583f989ed386"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.4.html": CreativeWork(
        identifier="OLDAP-2.4",
        name="Open LDAP Public License v2.4",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cd1284c4a91a8a380d904eee68d1583f989ed386"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cd1284c4a91a8a380d904eee68d1583f989ed386": CreativeWork(
        identifier="OLDAP-2.4",
        name="Open LDAP Public License v2.4",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cd1284c4a91a8a380d904eee68d1583f989ed386"
        ),
    ),  # type: ignore
    "OLDAP-2.5": CreativeWork(
        identifier="OLDAP-2.5",
        name="Open LDAP Public License v2.5",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=6852b9d90022e8593c98205413380536b1b5a7cf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.5": CreativeWork(
        identifier="OLDAP-2.5",
        name="Open LDAP Public License v2.5",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=6852b9d90022e8593c98205413380536b1b5a7cf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.5.html": CreativeWork(
        identifier="OLDAP-2.5",
        name="Open LDAP Public License v2.5",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=6852b9d90022e8593c98205413380536b1b5a7cf"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=6852b9d90022e8593c98205413380536b1b5a7cf": CreativeWork(
        identifier="OLDAP-2.5",
        name="Open LDAP Public License v2.5",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=6852b9d90022e8593c98205413380536b1b5a7cf"
        ),
    ),  # type: ignore
    "OLDAP-2.6": CreativeWork(
        identifier="OLDAP-2.6",
        name="Open LDAP Public License v2.6",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=1cae062821881f41b73012ba816434897abf4205"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.6": CreativeWork(
        identifier="OLDAP-2.6",
        name="Open LDAP Public License v2.6",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=1cae062821881f41b73012ba816434897abf4205"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.6.html": CreativeWork(
        identifier="OLDAP-2.6",
        name="Open LDAP Public License v2.6",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=1cae062821881f41b73012ba816434897abf4205"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=1cae062821881f41b73012ba816434897abf4205": CreativeWork(
        identifier="OLDAP-2.6",
        name="Open LDAP Public License v2.6",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=1cae062821881f41b73012ba816434897abf4205"
        ),
    ),  # type: ignore
    "OLDAP-2.7": CreativeWork(
        identifier="OLDAP-2.7",
        name="Open LDAP Public License v2.7",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=47c2415c1df81556eeb39be6cad458ef87c534a2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.7": CreativeWork(
        identifier="OLDAP-2.7",
        name="Open LDAP Public License v2.7",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=47c2415c1df81556eeb39be6cad458ef87c534a2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.7.html": CreativeWork(
        identifier="OLDAP-2.7",
        name="Open LDAP Public License v2.7",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=47c2415c1df81556eeb39be6cad458ef87c534a2"
        ),
    ),  # type: ignore
    "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=47c2415c1df81556eeb39be6cad458ef87c534a2": CreativeWork(
        identifier="OLDAP-2.7",
        name="Open LDAP Public License v2.7",
        url=AnyUrl(
            "http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=47c2415c1df81556eeb39be6cad458ef87c534a2"
        ),
    ),  # type: ignore
    "OLDAP-2.8": CreativeWork(
        identifier="OLDAP-2.8",
        name="Open LDAP Public License v2.8",
        url=AnyUrl("http://www.openldap.org/software/release/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.8": CreativeWork(
        identifier="OLDAP-2.8",
        name="Open LDAP Public License v2.8",
        url=AnyUrl("http://www.openldap.org/software/release/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/OLDAP-2.8.html": CreativeWork(
        identifier="OLDAP-2.8",
        name="Open LDAP Public License v2.8",
        url=AnyUrl("http://www.openldap.org/software/release/license.html"),
    ),  # type: ignore
    "http://www.openldap.org/software/release/license.html": CreativeWork(
        identifier="OLDAP-2.8",
        name="Open LDAP Public License v2.8",
        url=AnyUrl("http://www.openldap.org/software/release/license.html"),
    ),  # type: ignore
    "OLFL-1.3": CreativeWork(
        identifier="OLFL-1.3",
        name="Open Logistics Foundation License Version 1.3",
        url=AnyUrl("https://openlogisticsfoundation.org/licenses/"),
    ),  # type: ignore
    "https://spdx.org/licenses/OLFL-1.3": CreativeWork(
        identifier="OLFL-1.3",
        name="Open Logistics Foundation License Version 1.3",
        url=AnyUrl("https://openlogisticsfoundation.org/licenses/"),
    ),  # type: ignore
    "https://spdx.org/licenses/OLFL-1.3.html": CreativeWork(
        identifier="OLFL-1.3",
        name="Open Logistics Foundation License Version 1.3",
        url=AnyUrl("https://openlogisticsfoundation.org/licenses/"),
    ),  # type: ignore
    "https://openlogisticsfoundation.org/licenses/": CreativeWork(
        identifier="OLFL-1.3",
        name="Open Logistics Foundation License Version 1.3",
        url=AnyUrl("https://openlogisticsfoundation.org/licenses/"),
    ),  # type: ignore
    "OML": CreativeWork(
        identifier="OML",
        name="Open Market License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Open_Market_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/OML": CreativeWork(
        identifier="OML",
        name="Open Market License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Open_Market_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/OML.html": CreativeWork(
        identifier="OML",
        name="Open Market License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Open_Market_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Open_Market_License": CreativeWork(
        identifier="OML",
        name="Open Market License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Open_Market_License"),
    ),  # type: ignore
    "OpenMDW-1.0": CreativeWork(
        identifier="OpenMDW-1.0",
        name="OpenMDW License Agreement v1.0",
        url=AnyUrl(
            "https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.0/LICENSE.openmdw"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenMDW-1.0": CreativeWork(
        identifier="OpenMDW-1.0",
        name="OpenMDW License Agreement v1.0",
        url=AnyUrl(
            "https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.0/LICENSE.openmdw"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenMDW-1.0.html": CreativeWork(
        identifier="OpenMDW-1.0",
        name="OpenMDW License Agreement v1.0",
        url=AnyUrl(
            "https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.0/LICENSE.openmdw"
        ),
    ),  # type: ignore
    "https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.0/LICENSE.openmdw": CreativeWork(
        identifier="OpenMDW-1.0",
        name="OpenMDW License Agreement v1.0",
        url=AnyUrl(
            "https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.0/LICENSE.openmdw"
        ),
    ),  # type: ignore
    "OpenPBS-2.3": CreativeWork(
        identifier="OpenPBS-2.3",
        name="OpenPBS v2.3 Software License",
        url=AnyUrl(
            "https://github.com/adaptivecomputing/torque/blob/master/PBS_License.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenPBS-2.3": CreativeWork(
        identifier="OpenPBS-2.3",
        name="OpenPBS v2.3 Software License",
        url=AnyUrl(
            "https://github.com/adaptivecomputing/torque/blob/master/PBS_License.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenPBS-2.3.html": CreativeWork(
        identifier="OpenPBS-2.3",
        name="OpenPBS v2.3 Software License",
        url=AnyUrl(
            "https://github.com/adaptivecomputing/torque/blob/master/PBS_License.txt"
        ),
    ),  # type: ignore
    "https://github.com/adaptivecomputing/torque/blob/master/PBS_License.txt": CreativeWork(
        identifier="OpenPBS-2.3",
        name="OpenPBS v2.3 Software License",
        url=AnyUrl(
            "https://github.com/adaptivecomputing/torque/blob/master/PBS_License.txt"
        ),
    ),  # type: ignore
    "OpenSSL": CreativeWork(
        identifier="OpenSSL",
        name="OpenSSL License",
        url=AnyUrl("http://www.openssl.org/source/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenSSL": CreativeWork(
        identifier="OpenSSL",
        name="OpenSSL License",
        url=AnyUrl("http://www.openssl.org/source/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenSSL.html": CreativeWork(
        identifier="OpenSSL",
        name="OpenSSL License",
        url=AnyUrl("http://www.openssl.org/source/license.html"),
    ),  # type: ignore
    "http://www.openssl.org/source/license.html": CreativeWork(
        identifier="OpenSSL",
        name="OpenSSL License",
        url=AnyUrl("http://www.openssl.org/source/license.html"),
    ),  # type: ignore
    "OpenSSL-standalone": CreativeWork(
        identifier="OpenSSL-standalone",
        name="OpenSSL License - standalone",
        url=AnyUrl("https://library.netapp.com/ecm/ecm_download_file/ECMP1196395"),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenSSL-standalone": CreativeWork(
        identifier="OpenSSL-standalone",
        name="OpenSSL License - standalone",
        url=AnyUrl("https://library.netapp.com/ecm/ecm_download_file/ECMP1196395"),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenSSL-standalone.html": CreativeWork(
        identifier="OpenSSL-standalone",
        name="OpenSSL License - standalone",
        url=AnyUrl("https://library.netapp.com/ecm/ecm_download_file/ECMP1196395"),
    ),  # type: ignore
    "https://library.netapp.com/ecm/ecm_download_file/ECMP1196395": CreativeWork(
        identifier="OpenSSL-standalone",
        name="OpenSSL License - standalone",
        url=AnyUrl("https://library.netapp.com/ecm/ecm_download_file/ECMP1196395"),
    ),  # type: ignore
    "OpenVision": CreativeWork(
        identifier="OpenVision",
        name="OpenVision License",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L66-L98"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenVision": CreativeWork(
        identifier="OpenVision",
        name="OpenVision License",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L66-L98"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OpenVision.html": CreativeWork(
        identifier="OpenVision",
        name="OpenVision License",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L66-L98"
        ),
    ),  # type: ignore
    "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L66-L98": CreativeWork(
        identifier="OpenVision",
        name="OpenVision License",
        url=AnyUrl(
            "https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L66-L98"
        ),
    ),  # type: ignore
    "OPL-1.0": CreativeWork(
        identifier="OPL-1.0",
        name="Open Public License v1.0",
        url=AnyUrl("http://old.koalateam.com/jackaroo/OPL_1_0.TXT"),
    ),  # type: ignore
    "https://spdx.org/licenses/OPL-1.0": CreativeWork(
        identifier="OPL-1.0",
        name="Open Public License v1.0",
        url=AnyUrl("http://old.koalateam.com/jackaroo/OPL_1_0.TXT"),
    ),  # type: ignore
    "https://spdx.org/licenses/OPL-1.0.html": CreativeWork(
        identifier="OPL-1.0",
        name="Open Public License v1.0",
        url=AnyUrl("http://old.koalateam.com/jackaroo/OPL_1_0.TXT"),
    ),  # type: ignore
    "http://old.koalateam.com/jackaroo/OPL_1_0.TXT": CreativeWork(
        identifier="OPL-1.0",
        name="Open Public License v1.0",
        url=AnyUrl("http://old.koalateam.com/jackaroo/OPL_1_0.TXT"),
    ),  # type: ignore
    "OPL-UK-3.0": CreativeWork(
        identifier="OPL-UK-3.0",
        name="United    Kingdom Open Parliament Licence v3.0",
        url=AnyUrl(
            "https://www.parliament.uk/site-information/copyright-parliament/open-parliament-licence/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OPL-UK-3.0": CreativeWork(
        identifier="OPL-UK-3.0",
        name="United    Kingdom Open Parliament Licence v3.0",
        url=AnyUrl(
            "https://www.parliament.uk/site-information/copyright-parliament/open-parliament-licence/"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OPL-UK-3.0.html": CreativeWork(
        identifier="OPL-UK-3.0",
        name="United    Kingdom Open Parliament Licence v3.0",
        url=AnyUrl(
            "https://www.parliament.uk/site-information/copyright-parliament/open-parliament-licence/"
        ),
    ),  # type: ignore
    "https://www.parliament.uk/site-information/copyright-parliament/open-parliament-licence/": CreativeWork(
        identifier="OPL-UK-3.0",
        name="United    Kingdom Open Parliament Licence v3.0",
        url=AnyUrl(
            "https://www.parliament.uk/site-information/copyright-parliament/open-parliament-licence/"
        ),
    ),  # type: ignore
    "OPUBL-1.0": CreativeWork(
        identifier="OPUBL-1.0",
        name="Open Publication License v1.0",
        url=AnyUrl("http://opencontent.org/openpub/"),
    ),  # type: ignore
    "https://spdx.org/licenses/OPUBL-1.0": CreativeWork(
        identifier="OPUBL-1.0",
        name="Open Publication License v1.0",
        url=AnyUrl("http://opencontent.org/openpub/"),
    ),  # type: ignore
    "https://spdx.org/licenses/OPUBL-1.0.html": CreativeWork(
        identifier="OPUBL-1.0",
        name="Open Publication License v1.0",
        url=AnyUrl("http://opencontent.org/openpub/"),
    ),  # type: ignore
    "http://opencontent.org/openpub/": CreativeWork(
        identifier="OPUBL-1.0",
        name="Open Publication License v1.0",
        url=AnyUrl("http://opencontent.org/openpub/"),
    ),  # type: ignore
    "OSC-1.0": CreativeWork(
        identifier="OSC-1.0",
        name="OSC License 1.0",
        url=AnyUrl("https://opensource.org/license/osc-license-1-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSC-1.0": CreativeWork(
        identifier="OSC-1.0",
        name="OSC License 1.0",
        url=AnyUrl("https://opensource.org/license/osc-license-1-0"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSC-1.0.html": CreativeWork(
        identifier="OSC-1.0",
        name="OSC License 1.0",
        url=AnyUrl("https://opensource.org/license/osc-license-1-0"),
    ),  # type: ignore
    "https://opensource.org/license/osc-license-1-0": CreativeWork(
        identifier="OSC-1.0",
        name="OSC License 1.0",
        url=AnyUrl("https://opensource.org/license/osc-license-1-0"),
    ),  # type: ignore
    "OSET-PL-2.1": CreativeWork(
        identifier="OSET-PL-2.1",
        name="OSET Public License version 2.1",
        url=AnyUrl("http://www.osetfoundation.org/public-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSET-PL-2.1": CreativeWork(
        identifier="OSET-PL-2.1",
        name="OSET Public License version 2.1",
        url=AnyUrl("http://www.osetfoundation.org/public-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSET-PL-2.1.html": CreativeWork(
        identifier="OSET-PL-2.1",
        name="OSET Public License version 2.1",
        url=AnyUrl("http://www.osetfoundation.org/public-license"),
    ),  # type: ignore
    "http://www.osetfoundation.org/public-license": CreativeWork(
        identifier="OSET-PL-2.1",
        name="OSET Public License version 2.1",
        url=AnyUrl("http://www.osetfoundation.org/public-license"),
    ),  # type: ignore
    "OSL-1.0": CreativeWork(
        identifier="OSL-1.0",
        name="Open Software License 1.0",
        url=AnyUrl("https://opensource.org/licenses/OSL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-1.0": CreativeWork(
        identifier="OSL-1.0",
        name="Open Software License 1.0",
        url=AnyUrl("https://opensource.org/licenses/OSL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-1.0.html": CreativeWork(
        identifier="OSL-1.0",
        name="Open Software License 1.0",
        url=AnyUrl("https://opensource.org/licenses/OSL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/OSL-1.0": CreativeWork(
        identifier="OSL-1.0",
        name="Open Software License 1.0",
        url=AnyUrl("https://opensource.org/licenses/OSL-1.0"),
    ),  # type: ignore
    "OSL-1.1": CreativeWork(
        identifier="OSL-1.1",
        name="Open Software License 1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/OSL1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-1.1": CreativeWork(
        identifier="OSL-1.1",
        name="Open Software License 1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/OSL1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-1.1.html": CreativeWork(
        identifier="OSL-1.1",
        name="Open Software License 1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/OSL1.1"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/OSL1.1": CreativeWork(
        identifier="OSL-1.1",
        name="Open Software License 1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/OSL1.1"),
    ),  # type: ignore
    "OSL-2.0": CreativeWork(
        identifier="OSL-2.0",
        name="Open Software License 2.0",
        url=AnyUrl(
            "http://web.archive.org/web/20041020171434/http://www.rosenlaw.com/osl2.0.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-2.0": CreativeWork(
        identifier="OSL-2.0",
        name="Open Software License 2.0",
        url=AnyUrl(
            "http://web.archive.org/web/20041020171434/http://www.rosenlaw.com/osl2.0.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-2.0.html": CreativeWork(
        identifier="OSL-2.0",
        name="Open Software License 2.0",
        url=AnyUrl(
            "http://web.archive.org/web/20041020171434/http://www.rosenlaw.com/osl2.0.html"
        ),
    ),  # type: ignore
    "http://web.archive.org/web/20041020171434/http://www.rosenlaw.com/osl2.0.html": CreativeWork(
        identifier="OSL-2.0",
        name="Open Software License 2.0",
        url=AnyUrl(
            "http://web.archive.org/web/20041020171434/http://www.rosenlaw.com/osl2.0.html"
        ),
    ),  # type: ignore
    "OSL-2.1": CreativeWork(
        identifier="OSL-2.1",
        name="Open Software License 2.1",
        url=AnyUrl(
            "http://web.archive.org/web/20050212003940/http://www.rosenlaw.com/osl21.htm"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-2.1": CreativeWork(
        identifier="OSL-2.1",
        name="Open Software License 2.1",
        url=AnyUrl(
            "http://web.archive.org/web/20050212003940/http://www.rosenlaw.com/osl21.htm"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-2.1.html": CreativeWork(
        identifier="OSL-2.1",
        name="Open Software License 2.1",
        url=AnyUrl(
            "http://web.archive.org/web/20050212003940/http://www.rosenlaw.com/osl21.htm"
        ),
    ),  # type: ignore
    "http://web.archive.org/web/20050212003940/http://www.rosenlaw.com/osl21.htm": CreativeWork(
        identifier="OSL-2.1",
        name="Open Software License 2.1",
        url=AnyUrl(
            "http://web.archive.org/web/20050212003940/http://www.rosenlaw.com/osl21.htm"
        ),
    ),  # type: ignore
    "OSL-3.0": CreativeWork(
        identifier="OSL-3.0",
        name="Open Software License 3.0",
        url=AnyUrl(
            "https://web.archive.org/web/20120101081418/http://rosenlaw.com:80/OSL3.0.htm"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-3.0": CreativeWork(
        identifier="OSL-3.0",
        name="Open Software License 3.0",
        url=AnyUrl(
            "https://web.archive.org/web/20120101081418/http://rosenlaw.com:80/OSL3.0.htm"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/OSL-3.0.html": CreativeWork(
        identifier="OSL-3.0",
        name="Open Software License 3.0",
        url=AnyUrl(
            "https://web.archive.org/web/20120101081418/http://rosenlaw.com:80/OSL3.0.htm"
        ),
    ),  # type: ignore
    "https://web.archive.org/web/20120101081418/http://rosenlaw.com:80/OSL3.0.htm": CreativeWork(
        identifier="OSL-3.0",
        name="Open Software License 3.0",
        url=AnyUrl(
            "https://web.archive.org/web/20120101081418/http://rosenlaw.com:80/OSL3.0.htm"
        ),
    ),  # type: ignore
    "OSSP": CreativeWork(
        identifier="OSSP",
        name="OSSP License",
        url=AnyUrl("https://git.sr.ht/~nabijaczleweli/ossp-var"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSSP": CreativeWork(
        identifier="OSSP",
        name="OSSP License",
        url=AnyUrl("https://git.sr.ht/~nabijaczleweli/ossp-var"),
    ),  # type: ignore
    "https://spdx.org/licenses/OSSP.html": CreativeWork(
        identifier="OSSP",
        name="OSSP License",
        url=AnyUrl("https://git.sr.ht/~nabijaczleweli/ossp-var"),
    ),  # type: ignore
    "https://git.sr.ht/~nabijaczleweli/ossp-var": CreativeWork(
        identifier="OSSP",
        name="OSSP License",
        url=AnyUrl("https://git.sr.ht/~nabijaczleweli/ossp-var"),
    ),  # type: ignore
    "PADL": CreativeWork(
        identifier="PADL",
        name="PADL License",
        url=AnyUrl(
            "https://git.openldap.org/openldap/openldap/-/blob/master/libraries/libldap/os-local.c?ref_type=heads#L19-23"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/PADL": CreativeWork(
        identifier="PADL",
        name="PADL License",
        url=AnyUrl(
            "https://git.openldap.org/openldap/openldap/-/blob/master/libraries/libldap/os-local.c?ref_type=heads#L19-23"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/PADL.html": CreativeWork(
        identifier="PADL",
        name="PADL License",
        url=AnyUrl(
            "https://git.openldap.org/openldap/openldap/-/blob/master/libraries/libldap/os-local.c?ref_type=heads#L19-23"
        ),
    ),  # type: ignore
    "https://git.openldap.org/openldap/openldap/-/blob/master/libraries/libldap/os-local.c?ref_type=heads#L19-23": CreativeWork(
        identifier="PADL",
        name="PADL License",
        url=AnyUrl(
            "https://git.openldap.org/openldap/openldap/-/blob/master/libraries/libldap/os-local.c?ref_type=heads#L19-23"
        ),
    ),  # type: ignore
    "ParaType-Free-Font-1.3": CreativeWork(
        identifier="ParaType-Free-Font-1.3",
        name="ParaType Free Font Licensing Agreement v1.3",
        url=AnyUrl(
            "https://web.archive.org/web/20161209023955/http://www.paratype.ru/public/pt_openlicense_eng.asp"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ParaType-Free-Font-1.3": CreativeWork(
        identifier="ParaType-Free-Font-1.3",
        name="ParaType Free Font Licensing Agreement v1.3",
        url=AnyUrl(
            "https://web.archive.org/web/20161209023955/http://www.paratype.ru/public/pt_openlicense_eng.asp"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ParaType-Free-Font-1.3.html": CreativeWork(
        identifier="ParaType-Free-Font-1.3",
        name="ParaType Free Font Licensing Agreement v1.3",
        url=AnyUrl(
            "https://web.archive.org/web/20161209023955/http://www.paratype.ru/public/pt_openlicense_eng.asp"
        ),
    ),  # type: ignore
    "https://web.archive.org/web/20161209023955/http://www.paratype.ru/public/pt_openlicense_eng.asp": CreativeWork(
        identifier="ParaType-Free-Font-1.3",
        name="ParaType Free Font Licensing Agreement v1.3",
        url=AnyUrl(
            "https://web.archive.org/web/20161209023955/http://www.paratype.ru/public/pt_openlicense_eng.asp"
        ),
    ),  # type: ignore
    "Parity-6.0.0": CreativeWork(
        identifier="Parity-6.0.0",
        name="The Parity Public License 6.0.0",
        url=AnyUrl("https://paritylicense.com/versions/6.0.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Parity-6.0.0": CreativeWork(
        identifier="Parity-6.0.0",
        name="The Parity Public License 6.0.0",
        url=AnyUrl("https://paritylicense.com/versions/6.0.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Parity-6.0.0.html": CreativeWork(
        identifier="Parity-6.0.0",
        name="The Parity Public License 6.0.0",
        url=AnyUrl("https://paritylicense.com/versions/6.0.0.html"),
    ),  # type: ignore
    "https://paritylicense.com/versions/6.0.0.html": CreativeWork(
        identifier="Parity-6.0.0",
        name="The Parity Public License 6.0.0",
        url=AnyUrl("https://paritylicense.com/versions/6.0.0.html"),
    ),  # type: ignore
    "Parity-7.0.0": CreativeWork(
        identifier="Parity-7.0.0",
        name="The Parity Public License 7.0.0",
        url=AnyUrl("https://paritylicense.com/versions/7.0.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Parity-7.0.0": CreativeWork(
        identifier="Parity-7.0.0",
        name="The Parity Public License 7.0.0",
        url=AnyUrl("https://paritylicense.com/versions/7.0.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Parity-7.0.0.html": CreativeWork(
        identifier="Parity-7.0.0",
        name="The Parity Public License 7.0.0",
        url=AnyUrl("https://paritylicense.com/versions/7.0.0.html"),
    ),  # type: ignore
    "https://paritylicense.com/versions/7.0.0.html": CreativeWork(
        identifier="Parity-7.0.0",
        name="The Parity Public License 7.0.0",
        url=AnyUrl("https://paritylicense.com/versions/7.0.0.html"),
    ),  # type: ignore
    "PDDL-1.0": CreativeWork(
        identifier="PDDL-1.0",
        name="Open Data Commons Public Domain Dedication & License 1.0",
        url=AnyUrl("http://opendatacommons.org/licenses/pddl/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/PDDL-1.0": CreativeWork(
        identifier="PDDL-1.0",
        name="Open Data Commons Public Domain Dedication & License 1.0",
        url=AnyUrl("http://opendatacommons.org/licenses/pddl/1.0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/PDDL-1.0.html": CreativeWork(
        identifier="PDDL-1.0",
        name="Open Data Commons Public Domain Dedication & License 1.0",
        url=AnyUrl("http://opendatacommons.org/licenses/pddl/1.0/"),
    ),  # type: ignore
    "http://opendatacommons.org/licenses/pddl/1.0/": CreativeWork(
        identifier="PDDL-1.0",
        name="Open Data Commons Public Domain Dedication & License 1.0",
        url=AnyUrl("http://opendatacommons.org/licenses/pddl/1.0/"),
    ),  # type: ignore
    "PHP-3.0": CreativeWork(
        identifier="PHP-3.0",
        name="PHP License v3.0",
        url=AnyUrl("http://www.php.net/license/3_0.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/PHP-3.0": CreativeWork(
        identifier="PHP-3.0",
        name="PHP License v3.0",
        url=AnyUrl("http://www.php.net/license/3_0.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/PHP-3.0.html": CreativeWork(
        identifier="PHP-3.0",
        name="PHP License v3.0",
        url=AnyUrl("http://www.php.net/license/3_0.txt"),
    ),  # type: ignore
    "http://www.php.net/license/3_0.txt": CreativeWork(
        identifier="PHP-3.0",
        name="PHP License v3.0",
        url=AnyUrl("http://www.php.net/license/3_0.txt"),
    ),  # type: ignore
    "PHP-3.01": CreativeWork(
        identifier="PHP-3.01",
        name="PHP License v3.01",
        url=AnyUrl("http://www.php.net/license/3_01.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/PHP-3.01": CreativeWork(
        identifier="PHP-3.01",
        name="PHP License v3.01",
        url=AnyUrl("http://www.php.net/license/3_01.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/PHP-3.01.html": CreativeWork(
        identifier="PHP-3.01",
        name="PHP License v3.01",
        url=AnyUrl("http://www.php.net/license/3_01.txt"),
    ),  # type: ignore
    "http://www.php.net/license/3_01.txt": CreativeWork(
        identifier="PHP-3.01",
        name="PHP License v3.01",
        url=AnyUrl("http://www.php.net/license/3_01.txt"),
    ),  # type: ignore
    "Pixar": CreativeWork(
        identifier="Pixar",
        name="Pixar License",
        url=AnyUrl(
            "https://github.com/PixarAnimationStudios/OpenSubdiv/raw/v3_5_0/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Pixar": CreativeWork(
        identifier="Pixar",
        name="Pixar License",
        url=AnyUrl(
            "https://github.com/PixarAnimationStudios/OpenSubdiv/raw/v3_5_0/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Pixar.html": CreativeWork(
        identifier="Pixar",
        name="Pixar License",
        url=AnyUrl(
            "https://github.com/PixarAnimationStudios/OpenSubdiv/raw/v3_5_0/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://github.com/PixarAnimationStudios/OpenSubdiv/raw/v3_5_0/LICENSE.txt": CreativeWork(
        identifier="Pixar",
        name="Pixar License",
        url=AnyUrl(
            "https://github.com/PixarAnimationStudios/OpenSubdiv/raw/v3_5_0/LICENSE.txt"
        ),
    ),  # type: ignore
    "pkgconf": CreativeWork(
        identifier="pkgconf",
        name="pkgconf License",
        url=AnyUrl("https://github.com/pkgconf/pkgconf/blob/master/cli/main.c#L8"),
    ),  # type: ignore
    "https://spdx.org/licenses/pkgconf": CreativeWork(
        identifier="pkgconf",
        name="pkgconf License",
        url=AnyUrl("https://github.com/pkgconf/pkgconf/blob/master/cli/main.c#L8"),
    ),  # type: ignore
    "https://spdx.org/licenses/pkgconf.html": CreativeWork(
        identifier="pkgconf",
        name="pkgconf License",
        url=AnyUrl("https://github.com/pkgconf/pkgconf/blob/master/cli/main.c#L8"),
    ),  # type: ignore
    "https://github.com/pkgconf/pkgconf/blob/master/cli/main.c#L8": CreativeWork(
        identifier="pkgconf",
        name="pkgconf License",
        url=AnyUrl("https://github.com/pkgconf/pkgconf/blob/master/cli/main.c#L8"),
    ),  # type: ignore
    "Plexus": CreativeWork(
        identifier="Plexus",
        name="Plexus Classworlds License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Plexus_Classworlds_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Plexus": CreativeWork(
        identifier="Plexus",
        name="Plexus Classworlds License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Plexus_Classworlds_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Plexus.html": CreativeWork(
        identifier="Plexus",
        name="Plexus Classworlds License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Plexus_Classworlds_License"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Plexus_Classworlds_License": CreativeWork(
        identifier="Plexus",
        name="Plexus Classworlds License",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Plexus_Classworlds_License"
        ),
    ),  # type: ignore
    "pnmstitch": CreativeWork(
        identifier="pnmstitch",
        name="pnmstitch License",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/editor/pnmstitch.c#l2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/pnmstitch": CreativeWork(
        identifier="pnmstitch",
        name="pnmstitch License",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/editor/pnmstitch.c#l2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/pnmstitch.html": CreativeWork(
        identifier="pnmstitch",
        name="pnmstitch License",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/editor/pnmstitch.c#l2"
        ),
    ),  # type: ignore
    "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/editor/pnmstitch.c#l2": CreativeWork(
        identifier="pnmstitch",
        name="pnmstitch License",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/editor/pnmstitch.c#l2"
        ),
    ),  # type: ignore
    "PolyForm-Noncommercial-1.0.0": CreativeWork(
        identifier="PolyForm-Noncommercial-1.0.0",
        name="PolyForm Noncommercial License 1.0.0",
        url=AnyUrl("https://polyformproject.org/licenses/noncommercial/1.0.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/PolyForm-Noncommercial-1.0.0": CreativeWork(
        identifier="PolyForm-Noncommercial-1.0.0",
        name="PolyForm Noncommercial License 1.0.0",
        url=AnyUrl("https://polyformproject.org/licenses/noncommercial/1.0.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/PolyForm-Noncommercial-1.0.0.html": CreativeWork(
        identifier="PolyForm-Noncommercial-1.0.0",
        name="PolyForm Noncommercial License 1.0.0",
        url=AnyUrl("https://polyformproject.org/licenses/noncommercial/1.0.0"),
    ),  # type: ignore
    "https://polyformproject.org/licenses/noncommercial/1.0.0": CreativeWork(
        identifier="PolyForm-Noncommercial-1.0.0",
        name="PolyForm Noncommercial License 1.0.0",
        url=AnyUrl("https://polyformproject.org/licenses/noncommercial/1.0.0"),
    ),  # type: ignore
    "PolyForm-Small-Business-1.0.0": CreativeWork(
        identifier="PolyForm-Small-Business-1.0.0",
        name="PolyForm Small Business License 1.0.0",
        url=AnyUrl("https://polyformproject.org/licenses/small-business/1.0.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/PolyForm-Small-Business-1.0.0": CreativeWork(
        identifier="PolyForm-Small-Business-1.0.0",
        name="PolyForm Small Business License 1.0.0",
        url=AnyUrl("https://polyformproject.org/licenses/small-business/1.0.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/PolyForm-Small-Business-1.0.0.html": CreativeWork(
        identifier="PolyForm-Small-Business-1.0.0",
        name="PolyForm Small Business License 1.0.0",
        url=AnyUrl("https://polyformproject.org/licenses/small-business/1.0.0"),
    ),  # type: ignore
    "https://polyformproject.org/licenses/small-business/1.0.0": CreativeWork(
        identifier="PolyForm-Small-Business-1.0.0",
        name="PolyForm Small Business License 1.0.0",
        url=AnyUrl("https://polyformproject.org/licenses/small-business/1.0.0"),
    ),  # type: ignore
    "PostgreSQL": CreativeWork(
        identifier="PostgreSQL",
        name="PostgreSQL License",
        url=AnyUrl("http://www.postgresql.org/about/licence"),
    ),  # type: ignore
    "https://spdx.org/licenses/PostgreSQL": CreativeWork(
        identifier="PostgreSQL",
        name="PostgreSQL License",
        url=AnyUrl("http://www.postgresql.org/about/licence"),
    ),  # type: ignore
    "https://spdx.org/licenses/PostgreSQL.html": CreativeWork(
        identifier="PostgreSQL",
        name="PostgreSQL License",
        url=AnyUrl("http://www.postgresql.org/about/licence"),
    ),  # type: ignore
    "http://www.postgresql.org/about/licence": CreativeWork(
        identifier="PostgreSQL",
        name="PostgreSQL License",
        url=AnyUrl("http://www.postgresql.org/about/licence"),
    ),  # type: ignore
    "PPL": CreativeWork(
        identifier="PPL",
        name="Peer Production License",
        url=AnyUrl("https://wiki.p2pfoundation.net/Peer_Production_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/PPL": CreativeWork(
        identifier="PPL",
        name="Peer Production License",
        url=AnyUrl("https://wiki.p2pfoundation.net/Peer_Production_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/PPL.html": CreativeWork(
        identifier="PPL",
        name="Peer Production License",
        url=AnyUrl("https://wiki.p2pfoundation.net/Peer_Production_License"),
    ),  # type: ignore
    "https://wiki.p2pfoundation.net/Peer_Production_License": CreativeWork(
        identifier="PPL",
        name="Peer Production License",
        url=AnyUrl("https://wiki.p2pfoundation.net/Peer_Production_License"),
    ),  # type: ignore
    "PSF-2.0": CreativeWork(
        identifier="PSF-2.0",
        name="Python Software Foundation License 2.0",
        url=AnyUrl("https://opensource.org/licenses/Python-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/PSF-2.0": CreativeWork(
        identifier="PSF-2.0",
        name="Python Software Foundation License 2.0",
        url=AnyUrl("https://opensource.org/licenses/Python-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/PSF-2.0.html": CreativeWork(
        identifier="PSF-2.0",
        name="Python Software Foundation License 2.0",
        url=AnyUrl("https://opensource.org/licenses/Python-2.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/Python-2.0": CreativeWork(
        identifier="PSF-2.0",
        name="Python Software Foundation License 2.0",
        url=AnyUrl("https://opensource.org/licenses/Python-2.0"),
    ),  # type: ignore
    "psfrag": CreativeWork(
        identifier="psfrag",
        name="psfrag License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/psfrag"),
    ),  # type: ignore
    "https://spdx.org/licenses/psfrag": CreativeWork(
        identifier="psfrag",
        name="psfrag License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/psfrag"),
    ),  # type: ignore
    "https://spdx.org/licenses/psfrag.html": CreativeWork(
        identifier="psfrag",
        name="psfrag License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/psfrag"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/psfrag": CreativeWork(
        identifier="psfrag",
        name="psfrag License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/psfrag"),
    ),  # type: ignore
    "psutils": CreativeWork(
        identifier="psutils",
        name="psutils License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/psutils"),
    ),  # type: ignore
    "https://spdx.org/licenses/psutils": CreativeWork(
        identifier="psutils",
        name="psutils License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/psutils"),
    ),  # type: ignore
    "https://spdx.org/licenses/psutils.html": CreativeWork(
        identifier="psutils",
        name="psutils License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/psutils"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/psutils": CreativeWork(
        identifier="psutils",
        name="psutils License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/psutils"),
    ),  # type: ignore
    "Python-2.0": CreativeWork(
        identifier="Python-2.0",
        name="Python License 2.0",
        url=AnyUrl("https://opensource.org/licenses/Python-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Python-2.0": CreativeWork(
        identifier="Python-2.0",
        name="Python License 2.0",
        url=AnyUrl("https://opensource.org/licenses/Python-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Python-2.0.html": CreativeWork(
        identifier="Python-2.0",
        name="Python License 2.0",
        url=AnyUrl("https://opensource.org/licenses/Python-2.0"),
    ),  # type: ignore
    "Python-2.0.1": CreativeWork(
        identifier="Python-2.0.1",
        name="Python License 2.0.1",
        url=AnyUrl("https://www.python.org/download/releases/2.0.1/license/"),
    ),  # type: ignore
    "https://spdx.org/licenses/Python-2.0.1": CreativeWork(
        identifier="Python-2.0.1",
        name="Python License 2.0.1",
        url=AnyUrl("https://www.python.org/download/releases/2.0.1/license/"),
    ),  # type: ignore
    "https://spdx.org/licenses/Python-2.0.1.html": CreativeWork(
        identifier="Python-2.0.1",
        name="Python License 2.0.1",
        url=AnyUrl("https://www.python.org/download/releases/2.0.1/license/"),
    ),  # type: ignore
    "https://www.python.org/download/releases/2.0.1/license/": CreativeWork(
        identifier="Python-2.0.1",
        name="Python License 2.0.1",
        url=AnyUrl("https://www.python.org/download/releases/2.0.1/license/"),
    ),  # type: ignore
    "python-ldap": CreativeWork(
        identifier="python-ldap",
        name="Python ldap License",
        url=AnyUrl("https://github.com/python-ldap/python-ldap/blob/main/LICENCE"),
    ),  # type: ignore
    "https://spdx.org/licenses/python-ldap": CreativeWork(
        identifier="python-ldap",
        name="Python ldap License",
        url=AnyUrl("https://github.com/python-ldap/python-ldap/blob/main/LICENCE"),
    ),  # type: ignore
    "https://spdx.org/licenses/python-ldap.html": CreativeWork(
        identifier="python-ldap",
        name="Python ldap License",
        url=AnyUrl("https://github.com/python-ldap/python-ldap/blob/main/LICENCE"),
    ),  # type: ignore
    "https://github.com/python-ldap/python-ldap/blob/main/LICENCE": CreativeWork(
        identifier="python-ldap",
        name="Python ldap License",
        url=AnyUrl("https://github.com/python-ldap/python-ldap/blob/main/LICENCE"),
    ),  # type: ignore
    "Qhull": CreativeWork(
        identifier="Qhull",
        name="Qhull License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Qhull"),
    ),  # type: ignore
    "https://spdx.org/licenses/Qhull": CreativeWork(
        identifier="Qhull",
        name="Qhull License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Qhull"),
    ),  # type: ignore
    "https://spdx.org/licenses/Qhull.html": CreativeWork(
        identifier="Qhull",
        name="Qhull License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Qhull"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Qhull": CreativeWork(
        identifier="Qhull",
        name="Qhull License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Qhull"),
    ),  # type: ignore
    "QPL-1.0": CreativeWork(
        identifier="QPL-1.0",
        name="Q Public License 1.0",
        url=AnyUrl("http://doc.qt.nokia.com/3.3/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/QPL-1.0": CreativeWork(
        identifier="QPL-1.0",
        name="Q Public License 1.0",
        url=AnyUrl("http://doc.qt.nokia.com/3.3/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/QPL-1.0.html": CreativeWork(
        identifier="QPL-1.0",
        name="Q Public License 1.0",
        url=AnyUrl("http://doc.qt.nokia.com/3.3/license.html"),
    ),  # type: ignore
    "http://doc.qt.nokia.com/3.3/license.html": CreativeWork(
        identifier="QPL-1.0",
        name="Q Public License 1.0",
        url=AnyUrl("http://doc.qt.nokia.com/3.3/license.html"),
    ),  # type: ignore
    "QPL-1.0-INRIA-2004": CreativeWork(
        identifier="QPL-1.0-INRIA-2004",
        name="Q Public License 1.0 - INRIA 2004 variant",
        url=AnyUrl("https://github.com/maranget/hevea/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/QPL-1.0-INRIA-2004": CreativeWork(
        identifier="QPL-1.0-INRIA-2004",
        name="Q Public License 1.0 - INRIA 2004 variant",
        url=AnyUrl("https://github.com/maranget/hevea/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/QPL-1.0-INRIA-2004.html": CreativeWork(
        identifier="QPL-1.0-INRIA-2004",
        name="Q Public License 1.0 - INRIA 2004 variant",
        url=AnyUrl("https://github.com/maranget/hevea/blob/master/LICENSE"),
    ),  # type: ignore
    "https://github.com/maranget/hevea/blob/master/LICENSE": CreativeWork(
        identifier="QPL-1.0-INRIA-2004",
        name="Q Public License 1.0 - INRIA 2004 variant",
        url=AnyUrl("https://github.com/maranget/hevea/blob/master/LICENSE"),
    ),  # type: ignore
    "radvd": CreativeWork(
        identifier="radvd",
        name="radvd License",
        url=AnyUrl("https://github.com/radvd-project/radvd/blob/master/COPYRIGHT"),
    ),  # type: ignore
    "https://spdx.org/licenses/radvd": CreativeWork(
        identifier="radvd",
        name="radvd License",
        url=AnyUrl("https://github.com/radvd-project/radvd/blob/master/COPYRIGHT"),
    ),  # type: ignore
    "https://spdx.org/licenses/radvd.html": CreativeWork(
        identifier="radvd",
        name="radvd License",
        url=AnyUrl("https://github.com/radvd-project/radvd/blob/master/COPYRIGHT"),
    ),  # type: ignore
    "https://github.com/radvd-project/radvd/blob/master/COPYRIGHT": CreativeWork(
        identifier="radvd",
        name="radvd License",
        url=AnyUrl("https://github.com/radvd-project/radvd/blob/master/COPYRIGHT"),
    ),  # type: ignore
    "Rdisc": CreativeWork(
        identifier="Rdisc",
        name="Rdisc License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Rdisc_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/Rdisc": CreativeWork(
        identifier="Rdisc",
        name="Rdisc License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Rdisc_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/Rdisc.html": CreativeWork(
        identifier="Rdisc",
        name="Rdisc License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Rdisc_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Rdisc_License": CreativeWork(
        identifier="Rdisc",
        name="Rdisc License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Rdisc_License"),
    ),  # type: ignore
    "RHeCos-1.1": CreativeWork(
        identifier="RHeCos-1.1",
        name="Red Hat eCos Public License v1.1",
        url=AnyUrl("http://ecos.sourceware.org/old-license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/RHeCos-1.1": CreativeWork(
        identifier="RHeCos-1.1",
        name="Red Hat eCos Public License v1.1",
        url=AnyUrl("http://ecos.sourceware.org/old-license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/RHeCos-1.1.html": CreativeWork(
        identifier="RHeCos-1.1",
        name="Red Hat eCos Public License v1.1",
        url=AnyUrl("http://ecos.sourceware.org/old-license.html"),
    ),  # type: ignore
    "http://ecos.sourceware.org/old-license.html": CreativeWork(
        identifier="RHeCos-1.1",
        name="Red Hat eCos Public License v1.1",
        url=AnyUrl("http://ecos.sourceware.org/old-license.html"),
    ),  # type: ignore
    "RPL-1.1": CreativeWork(
        identifier="RPL-1.1",
        name="Reciprocal Public License 1.1",
        url=AnyUrl("https://opensource.org/licenses/RPL-1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/RPL-1.1": CreativeWork(
        identifier="RPL-1.1",
        name="Reciprocal Public License 1.1",
        url=AnyUrl("https://opensource.org/licenses/RPL-1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/RPL-1.1.html": CreativeWork(
        identifier="RPL-1.1",
        name="Reciprocal Public License 1.1",
        url=AnyUrl("https://opensource.org/licenses/RPL-1.1"),
    ),  # type: ignore
    "https://opensource.org/licenses/RPL-1.1": CreativeWork(
        identifier="RPL-1.1",
        name="Reciprocal Public License 1.1",
        url=AnyUrl("https://opensource.org/licenses/RPL-1.1"),
    ),  # type: ignore
    "RPL-1.5": CreativeWork(
        identifier="RPL-1.5",
        name="Reciprocal Public License 1.5",
        url=AnyUrl("https://opensource.org/licenses/RPL-1.5"),
    ),  # type: ignore
    "https://spdx.org/licenses/RPL-1.5": CreativeWork(
        identifier="RPL-1.5",
        name="Reciprocal Public License 1.5",
        url=AnyUrl("https://opensource.org/licenses/RPL-1.5"),
    ),  # type: ignore
    "https://spdx.org/licenses/RPL-1.5.html": CreativeWork(
        identifier="RPL-1.5",
        name="Reciprocal Public License 1.5",
        url=AnyUrl("https://opensource.org/licenses/RPL-1.5"),
    ),  # type: ignore
    "https://opensource.org/licenses/RPL-1.5": CreativeWork(
        identifier="RPL-1.5",
        name="Reciprocal Public License 1.5",
        url=AnyUrl("https://opensource.org/licenses/RPL-1.5"),
    ),  # type: ignore
    "RPSL-1.0": CreativeWork(
        identifier="RPSL-1.0",
        name="RealNetworks Public Source License v1.0",
        url=AnyUrl("https://helixcommunity.org/content/rpsl"),
    ),  # type: ignore
    "https://spdx.org/licenses/RPSL-1.0": CreativeWork(
        identifier="RPSL-1.0",
        name="RealNetworks Public Source License v1.0",
        url=AnyUrl("https://helixcommunity.org/content/rpsl"),
    ),  # type: ignore
    "https://spdx.org/licenses/RPSL-1.0.html": CreativeWork(
        identifier="RPSL-1.0",
        name="RealNetworks Public Source License v1.0",
        url=AnyUrl("https://helixcommunity.org/content/rpsl"),
    ),  # type: ignore
    "https://helixcommunity.org/content/rpsl": CreativeWork(
        identifier="RPSL-1.0",
        name="RealNetworks Public Source License v1.0",
        url=AnyUrl("https://helixcommunity.org/content/rpsl"),
    ),  # type: ignore
    "RSA-MD": CreativeWork(
        identifier="RSA-MD",
        name="RSA Message-Digest License",
        url=AnyUrl("http://www.faqs.org/rfcs/rfc1321.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/RSA-MD": CreativeWork(
        identifier="RSA-MD",
        name="RSA Message-Digest License",
        url=AnyUrl("http://www.faqs.org/rfcs/rfc1321.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/RSA-MD.html": CreativeWork(
        identifier="RSA-MD",
        name="RSA Message-Digest License",
        url=AnyUrl("http://www.faqs.org/rfcs/rfc1321.html"),
    ),  # type: ignore
    "http://www.faqs.org/rfcs/rfc1321.html": CreativeWork(
        identifier="RSA-MD",
        name="RSA Message-Digest License",
        url=AnyUrl("http://www.faqs.org/rfcs/rfc1321.html"),
    ),  # type: ignore
    "RSCPL": CreativeWork(
        identifier="RSCPL",
        name="Ricoh Source Code Public License",
        url=AnyUrl(
            "http://wayback.archive.org/web/20060715140826/http://www.risource.org/RPL/RPL-1.0A.shtml"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/RSCPL": CreativeWork(
        identifier="RSCPL",
        name="Ricoh Source Code Public License",
        url=AnyUrl(
            "http://wayback.archive.org/web/20060715140826/http://www.risource.org/RPL/RPL-1.0A.shtml"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/RSCPL.html": CreativeWork(
        identifier="RSCPL",
        name="Ricoh Source Code Public License",
        url=AnyUrl(
            "http://wayback.archive.org/web/20060715140826/http://www.risource.org/RPL/RPL-1.0A.shtml"
        ),
    ),  # type: ignore
    "http://wayback.archive.org/web/20060715140826/http://www.risource.org/RPL/RPL-1.0A.shtml": CreativeWork(
        identifier="RSCPL",
        name="Ricoh Source Code Public License",
        url=AnyUrl(
            "http://wayback.archive.org/web/20060715140826/http://www.risource.org/RPL/RPL-1.0A.shtml"
        ),
    ),  # type: ignore
    "Ruby": CreativeWork(
        identifier="Ruby",
        name="Ruby License",
        url=AnyUrl("https://www.ruby-lang.org/en/about/license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Ruby": CreativeWork(
        identifier="Ruby",
        name="Ruby License",
        url=AnyUrl("https://www.ruby-lang.org/en/about/license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Ruby.html": CreativeWork(
        identifier="Ruby",
        name="Ruby License",
        url=AnyUrl("https://www.ruby-lang.org/en/about/license.txt"),
    ),  # type: ignore
    "https://www.ruby-lang.org/en/about/license.txt": CreativeWork(
        identifier="Ruby",
        name="Ruby License",
        url=AnyUrl("https://www.ruby-lang.org/en/about/license.txt"),
    ),  # type: ignore
    "Ruby-pty": CreativeWork(
        identifier="Ruby-pty",
        name="Ruby pty extension license",
        url=AnyUrl(
            "https://github.com/ruby/ruby/blob/9f6deaa6888a423720b4b127b5314f0ad26cc2e6/ext/pty/pty.c#L775-L786"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Ruby-pty": CreativeWork(
        identifier="Ruby-pty",
        name="Ruby pty extension license",
        url=AnyUrl(
            "https://github.com/ruby/ruby/blob/9f6deaa6888a423720b4b127b5314f0ad26cc2e6/ext/pty/pty.c#L775-L786"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Ruby-pty.html": CreativeWork(
        identifier="Ruby-pty",
        name="Ruby pty extension license",
        url=AnyUrl(
            "https://github.com/ruby/ruby/blob/9f6deaa6888a423720b4b127b5314f0ad26cc2e6/ext/pty/pty.c#L775-L786"
        ),
    ),  # type: ignore
    "https://github.com/ruby/ruby/blob/9f6deaa6888a423720b4b127b5314f0ad26cc2e6/ext/pty/pty.c#L775-L786": CreativeWork(
        identifier="Ruby-pty",
        name="Ruby pty extension license",
        url=AnyUrl(
            "https://github.com/ruby/ruby/blob/9f6deaa6888a423720b4b127b5314f0ad26cc2e6/ext/pty/pty.c#L775-L786"
        ),
    ),  # type: ignore
    "SAX-PD": CreativeWork(
        identifier="SAX-PD",
        name="Sax Public Domain Notice",
        url=AnyUrl("http://www.saxproject.org/copying.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SAX-PD": CreativeWork(
        identifier="SAX-PD",
        name="Sax Public Domain Notice",
        url=AnyUrl("http://www.saxproject.org/copying.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SAX-PD.html": CreativeWork(
        identifier="SAX-PD",
        name="Sax Public Domain Notice",
        url=AnyUrl("http://www.saxproject.org/copying.html"),
    ),  # type: ignore
    "http://www.saxproject.org/copying.html": CreativeWork(
        identifier="SAX-PD",
        name="Sax Public Domain Notice",
        url=AnyUrl("http://www.saxproject.org/copying.html"),
    ),  # type: ignore
    "SAX-PD-2.0": CreativeWork(
        identifier="SAX-PD-2.0",
        name="Sax Public Domain Notice 2.0",
        url=AnyUrl("http://www.saxproject.org/copying.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SAX-PD-2.0": CreativeWork(
        identifier="SAX-PD-2.0",
        name="Sax Public Domain Notice 2.0",
        url=AnyUrl("http://www.saxproject.org/copying.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SAX-PD-2.0.html": CreativeWork(
        identifier="SAX-PD-2.0",
        name="Sax Public Domain Notice 2.0",
        url=AnyUrl("http://www.saxproject.org/copying.html"),
    ),  # type: ignore
    "Saxpath": CreativeWork(
        identifier="Saxpath",
        name="Saxpath License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Saxpath_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/Saxpath": CreativeWork(
        identifier="Saxpath",
        name="Saxpath License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Saxpath_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/Saxpath.html": CreativeWork(
        identifier="Saxpath",
        name="Saxpath License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Saxpath_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Saxpath_License": CreativeWork(
        identifier="Saxpath",
        name="Saxpath License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Saxpath_License"),
    ),  # type: ignore
    "SCEA": CreativeWork(
        identifier="SCEA",
        name="SCEA Shared Source License",
        url=AnyUrl("http://research.scea.com/scea_shared_source_license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SCEA": CreativeWork(
        identifier="SCEA",
        name="SCEA Shared Source License",
        url=AnyUrl("http://research.scea.com/scea_shared_source_license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SCEA.html": CreativeWork(
        identifier="SCEA",
        name="SCEA Shared Source License",
        url=AnyUrl("http://research.scea.com/scea_shared_source_license.html"),
    ),  # type: ignore
    "http://research.scea.com/scea_shared_source_license.html": CreativeWork(
        identifier="SCEA",
        name="SCEA Shared Source License",
        url=AnyUrl("http://research.scea.com/scea_shared_source_license.html"),
    ),  # type: ignore
    "SchemeReport": CreativeWork(
        identifier="SchemeReport",
        name="Scheme Language Report License",
        url=AnyUrl("https://spdx.org/licenses/SchemeReport.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SchemeReport": CreativeWork(
        identifier="SchemeReport",
        name="Scheme Language Report License",
        url=AnyUrl("https://spdx.org/licenses/SchemeReport.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SchemeReport.html": CreativeWork(
        identifier="SchemeReport",
        name="Scheme Language Report License",
        url=AnyUrl("https://spdx.org/licenses/SchemeReport.html"),
    ),  # type: ignore
    "Sendmail": CreativeWork(
        identifier="Sendmail",
        name="Sendmail License",
        url=AnyUrl("http://www.sendmail.com/pdfs/open_source/sendmail_license.pdf"),
    ),  # type: ignore
    "https://spdx.org/licenses/Sendmail": CreativeWork(
        identifier="Sendmail",
        name="Sendmail License",
        url=AnyUrl("http://www.sendmail.com/pdfs/open_source/sendmail_license.pdf"),
    ),  # type: ignore
    "https://spdx.org/licenses/Sendmail.html": CreativeWork(
        identifier="Sendmail",
        name="Sendmail License",
        url=AnyUrl("http://www.sendmail.com/pdfs/open_source/sendmail_license.pdf"),
    ),  # type: ignore
    "http://www.sendmail.com/pdfs/open_source/sendmail_license.pdf": CreativeWork(
        identifier="Sendmail",
        name="Sendmail License",
        url=AnyUrl("http://www.sendmail.com/pdfs/open_source/sendmail_license.pdf"),
    ),  # type: ignore
    "Sendmail-8.23": CreativeWork(
        identifier="Sendmail-8.23",
        name="Sendmail License 8.23",
        url=AnyUrl(
            "https://www.proofpoint.com/sites/default/files/sendmail-license.pdf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Sendmail-8.23": CreativeWork(
        identifier="Sendmail-8.23",
        name="Sendmail License 8.23",
        url=AnyUrl(
            "https://www.proofpoint.com/sites/default/files/sendmail-license.pdf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Sendmail-8.23.html": CreativeWork(
        identifier="Sendmail-8.23",
        name="Sendmail License 8.23",
        url=AnyUrl(
            "https://www.proofpoint.com/sites/default/files/sendmail-license.pdf"
        ),
    ),  # type: ignore
    "https://www.proofpoint.com/sites/default/files/sendmail-license.pdf": CreativeWork(
        identifier="Sendmail-8.23",
        name="Sendmail License 8.23",
        url=AnyUrl(
            "https://www.proofpoint.com/sites/default/files/sendmail-license.pdf"
        ),
    ),  # type: ignore
    "Sendmail-Open-Source-1.1": CreativeWork(
        identifier="Sendmail-Open-Source-1.1",
        name="Sendmail Open Source License v1.1",
        url=AnyUrl(
            "https://github.com/trusteddomainproject/OpenDMARC/blob/master/LICENSE.Sendmail"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Sendmail-Open-Source-1.1": CreativeWork(
        identifier="Sendmail-Open-Source-1.1",
        name="Sendmail Open Source License v1.1",
        url=AnyUrl(
            "https://github.com/trusteddomainproject/OpenDMARC/blob/master/LICENSE.Sendmail"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Sendmail-Open-Source-1.1.html": CreativeWork(
        identifier="Sendmail-Open-Source-1.1",
        name="Sendmail Open Source License v1.1",
        url=AnyUrl(
            "https://github.com/trusteddomainproject/OpenDMARC/blob/master/LICENSE.Sendmail"
        ),
    ),  # type: ignore
    "https://github.com/trusteddomainproject/OpenDMARC/blob/master/LICENSE.Sendmail": CreativeWork(
        identifier="Sendmail-Open-Source-1.1",
        name="Sendmail Open Source License v1.1",
        url=AnyUrl(
            "https://github.com/trusteddomainproject/OpenDMARC/blob/master/LICENSE.Sendmail"
        ),
    ),  # type: ignore
    "SGI-B-1.0": CreativeWork(
        identifier="SGI-B-1.0",
        name="SGI Free Software License B v1.0",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.1.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SGI-B-1.0": CreativeWork(
        identifier="SGI-B-1.0",
        name="SGI Free Software License B v1.0",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.1.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SGI-B-1.0.html": CreativeWork(
        identifier="SGI-B-1.0",
        name="SGI Free Software License B v1.0",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.1.0.html"),
    ),  # type: ignore
    "http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.1.0.html": CreativeWork(
        identifier="SGI-B-1.0",
        name="SGI Free Software License B v1.0",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.1.0.html"),
    ),  # type: ignore
    "SGI-B-1.1": CreativeWork(
        identifier="SGI-B-1.1",
        name="SGI Free Software License B v1.1",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/"),
    ),  # type: ignore
    "https://spdx.org/licenses/SGI-B-1.1": CreativeWork(
        identifier="SGI-B-1.1",
        name="SGI Free Software License B v1.1",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/"),
    ),  # type: ignore
    "https://spdx.org/licenses/SGI-B-1.1.html": CreativeWork(
        identifier="SGI-B-1.1",
        name="SGI Free Software License B v1.1",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/"),
    ),  # type: ignore
    "http://oss.sgi.com/projects/FreeB/": CreativeWork(
        identifier="SGI-B-1.1",
        name="SGI Free Software License B v1.1",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/"),
    ),  # type: ignore
    "SGI-B-2.0": CreativeWork(
        identifier="SGI-B-2.0",
        name="SGI Free Software License B v2.0",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.2.0.pdf"),
    ),  # type: ignore
    "https://spdx.org/licenses/SGI-B-2.0": CreativeWork(
        identifier="SGI-B-2.0",
        name="SGI Free Software License B v2.0",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.2.0.pdf"),
    ),  # type: ignore
    "https://spdx.org/licenses/SGI-B-2.0.html": CreativeWork(
        identifier="SGI-B-2.0",
        name="SGI Free Software License B v2.0",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.2.0.pdf"),
    ),  # type: ignore
    "http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.2.0.pdf": CreativeWork(
        identifier="SGI-B-2.0",
        name="SGI Free Software License B v2.0",
        url=AnyUrl("http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.2.0.pdf"),
    ),  # type: ignore
    "SGI-OpenGL": CreativeWork(
        identifier="SGI-OpenGL",
        name="SGI OpenGL License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/mesa/glw/-/blob/master/README?ref_type=heads"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SGI-OpenGL": CreativeWork(
        identifier="SGI-OpenGL",
        name="SGI OpenGL License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/mesa/glw/-/blob/master/README?ref_type=heads"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SGI-OpenGL.html": CreativeWork(
        identifier="SGI-OpenGL",
        name="SGI OpenGL License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/mesa/glw/-/blob/master/README?ref_type=heads"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/mesa/glw/-/blob/master/README?ref_type=heads": CreativeWork(
        identifier="SGI-OpenGL",
        name="SGI OpenGL License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/mesa/glw/-/blob/master/README?ref_type=heads"
        ),
    ),  # type: ignore
    "SGMLUG-PM": CreativeWork(
        identifier="SGMLUG-PM",
        name="SGMLUG Parser Materials License",
        url=AnyUrl(
            "https://gitweb.gentoo.org/repo/gentoo.git/tree/licenses/SGMLUG?id=7d999af4a47bf55e53e54713d98d145f935935c1"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SGMLUG-PM": CreativeWork(
        identifier="SGMLUG-PM",
        name="SGMLUG Parser Materials License",
        url=AnyUrl(
            "https://gitweb.gentoo.org/repo/gentoo.git/tree/licenses/SGMLUG?id=7d999af4a47bf55e53e54713d98d145f935935c1"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SGMLUG-PM.html": CreativeWork(
        identifier="SGMLUG-PM",
        name="SGMLUG Parser Materials License",
        url=AnyUrl(
            "https://gitweb.gentoo.org/repo/gentoo.git/tree/licenses/SGMLUG?id=7d999af4a47bf55e53e54713d98d145f935935c1"
        ),
    ),  # type: ignore
    "https://gitweb.gentoo.org/repo/gentoo.git/tree/licenses/SGMLUG?id=7d999af4a47bf55e53e54713d98d145f935935c1": CreativeWork(
        identifier="SGMLUG-PM",
        name="SGMLUG Parser Materials License",
        url=AnyUrl(
            "https://gitweb.gentoo.org/repo/gentoo.git/tree/licenses/SGMLUG?id=7d999af4a47bf55e53e54713d98d145f935935c1"
        ),
    ),  # type: ignore
    "SGP4": CreativeWork(
        identifier="SGP4",
        name="SGP4 Permission Notice",
        url=AnyUrl("https://celestrak.org/publications/AIAA/2006-6753/faq.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/SGP4": CreativeWork(
        identifier="SGP4",
        name="SGP4 Permission Notice",
        url=AnyUrl("https://celestrak.org/publications/AIAA/2006-6753/faq.php"),
    ),  # type: ignore
    "https://spdx.org/licenses/SGP4.html": CreativeWork(
        identifier="SGP4",
        name="SGP4 Permission Notice",
        url=AnyUrl("https://celestrak.org/publications/AIAA/2006-6753/faq.php"),
    ),  # type: ignore
    "https://celestrak.org/publications/AIAA/2006-6753/faq.php": CreativeWork(
        identifier="SGP4",
        name="SGP4 Permission Notice",
        url=AnyUrl("https://celestrak.org/publications/AIAA/2006-6753/faq.php"),
    ),  # type: ignore
    "SHL-0.5": CreativeWork(
        identifier="SHL-0.5",
        name="Solderpad Hardware License v0.5",
        url=AnyUrl("https://solderpad.org/licenses/SHL-0.5/"),
    ),  # type: ignore
    "https://spdx.org/licenses/SHL-0.5": CreativeWork(
        identifier="SHL-0.5",
        name="Solderpad Hardware License v0.5",
        url=AnyUrl("https://solderpad.org/licenses/SHL-0.5/"),
    ),  # type: ignore
    "https://spdx.org/licenses/SHL-0.5.html": CreativeWork(
        identifier="SHL-0.5",
        name="Solderpad Hardware License v0.5",
        url=AnyUrl("https://solderpad.org/licenses/SHL-0.5/"),
    ),  # type: ignore
    "https://solderpad.org/licenses/SHL-0.5/": CreativeWork(
        identifier="SHL-0.5",
        name="Solderpad Hardware License v0.5",
        url=AnyUrl("https://solderpad.org/licenses/SHL-0.5/"),
    ),  # type: ignore
    "SHL-0.51": CreativeWork(
        identifier="SHL-0.51",
        name="Solderpad Hardware License, Version 0.51",
        url=AnyUrl("https://solderpad.org/licenses/SHL-0.51/"),
    ),  # type: ignore
    "https://spdx.org/licenses/SHL-0.51": CreativeWork(
        identifier="SHL-0.51",
        name="Solderpad Hardware License, Version 0.51",
        url=AnyUrl("https://solderpad.org/licenses/SHL-0.51/"),
    ),  # type: ignore
    "https://spdx.org/licenses/SHL-0.51.html": CreativeWork(
        identifier="SHL-0.51",
        name="Solderpad Hardware License, Version 0.51",
        url=AnyUrl("https://solderpad.org/licenses/SHL-0.51/"),
    ),  # type: ignore
    "https://solderpad.org/licenses/SHL-0.51/": CreativeWork(
        identifier="SHL-0.51",
        name="Solderpad Hardware License, Version 0.51",
        url=AnyUrl("https://solderpad.org/licenses/SHL-0.51/"),
    ),  # type: ignore
    "SimPL-2.0": CreativeWork(
        identifier="SimPL-2.0",
        name="Simple Public License 2.0",
        url=AnyUrl("https://opensource.org/licenses/SimPL-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/SimPL-2.0": CreativeWork(
        identifier="SimPL-2.0",
        name="Simple Public License 2.0",
        url=AnyUrl("https://opensource.org/licenses/SimPL-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/SimPL-2.0.html": CreativeWork(
        identifier="SimPL-2.0",
        name="Simple Public License 2.0",
        url=AnyUrl("https://opensource.org/licenses/SimPL-2.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/SimPL-2.0": CreativeWork(
        identifier="SimPL-2.0",
        name="Simple Public License 2.0",
        url=AnyUrl("https://opensource.org/licenses/SimPL-2.0"),
    ),  # type: ignore
    "SISSL": CreativeWork(
        identifier="SISSL",
        name="Sun Industry Standards Source License v1.1",
        url=AnyUrl("http://www.openoffice.org/licenses/sissl_license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SISSL": CreativeWork(
        identifier="SISSL",
        name="Sun Industry Standards Source License v1.1",
        url=AnyUrl("http://www.openoffice.org/licenses/sissl_license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SISSL.html": CreativeWork(
        identifier="SISSL",
        name="Sun Industry Standards Source License v1.1",
        url=AnyUrl("http://www.openoffice.org/licenses/sissl_license.html"),
    ),  # type: ignore
    "http://www.openoffice.org/licenses/sissl_license.html": CreativeWork(
        identifier="SISSL",
        name="Sun Industry Standards Source License v1.1",
        url=AnyUrl("http://www.openoffice.org/licenses/sissl_license.html"),
    ),  # type: ignore
    "SISSL-1.2": CreativeWork(
        identifier="SISSL-1.2",
        name="Sun Industry Standards Source License v1.2",
        url=AnyUrl(
            "http://gridscheduler.sourceforge.net/Gridengine_SISSL_license.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SISSL-1.2": CreativeWork(
        identifier="SISSL-1.2",
        name="Sun Industry Standards Source License v1.2",
        url=AnyUrl(
            "http://gridscheduler.sourceforge.net/Gridengine_SISSL_license.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SISSL-1.2.html": CreativeWork(
        identifier="SISSL-1.2",
        name="Sun Industry Standards Source License v1.2",
        url=AnyUrl(
            "http://gridscheduler.sourceforge.net/Gridengine_SISSL_license.html"
        ),
    ),  # type: ignore
    "http://gridscheduler.sourceforge.net/Gridengine_SISSL_license.html": CreativeWork(
        identifier="SISSL-1.2",
        name="Sun Industry Standards Source License v1.2",
        url=AnyUrl(
            "http://gridscheduler.sourceforge.net/Gridengine_SISSL_license.html"
        ),
    ),  # type: ignore
    "SL": CreativeWork(
        identifier="SL",
        name="SL License",
        url=AnyUrl("https://github.com/mtoyoda/sl/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/SL": CreativeWork(
        identifier="SL",
        name="SL License",
        url=AnyUrl("https://github.com/mtoyoda/sl/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/SL.html": CreativeWork(
        identifier="SL",
        name="SL License",
        url=AnyUrl("https://github.com/mtoyoda/sl/blob/master/LICENSE"),
    ),  # type: ignore
    "https://github.com/mtoyoda/sl/blob/master/LICENSE": CreativeWork(
        identifier="SL",
        name="SL License",
        url=AnyUrl("https://github.com/mtoyoda/sl/blob/master/LICENSE"),
    ),  # type: ignore
    "Sleepycat": CreativeWork(
        identifier="Sleepycat",
        name="Sleepycat License",
        url=AnyUrl("https://opensource.org/licenses/Sleepycat"),
    ),  # type: ignore
    "https://spdx.org/licenses/Sleepycat": CreativeWork(
        identifier="Sleepycat",
        name="Sleepycat License",
        url=AnyUrl("https://opensource.org/licenses/Sleepycat"),
    ),  # type: ignore
    "https://spdx.org/licenses/Sleepycat.html": CreativeWork(
        identifier="Sleepycat",
        name="Sleepycat License",
        url=AnyUrl("https://opensource.org/licenses/Sleepycat"),
    ),  # type: ignore
    "https://opensource.org/licenses/Sleepycat": CreativeWork(
        identifier="Sleepycat",
        name="Sleepycat License",
        url=AnyUrl("https://opensource.org/licenses/Sleepycat"),
    ),  # type: ignore
    "SMAIL-GPL": CreativeWork(
        identifier="SMAIL-GPL",
        name="SMAIL General Public License",
        url=AnyUrl("https://sources.debian.org/copyright/license/debianutils/4.11.2/"),
    ),  # type: ignore
    "https://spdx.org/licenses/SMAIL-GPL": CreativeWork(
        identifier="SMAIL-GPL",
        name="SMAIL General Public License",
        url=AnyUrl("https://sources.debian.org/copyright/license/debianutils/4.11.2/"),
    ),  # type: ignore
    "https://spdx.org/licenses/SMAIL-GPL.html": CreativeWork(
        identifier="SMAIL-GPL",
        name="SMAIL General Public License",
        url=AnyUrl("https://sources.debian.org/copyright/license/debianutils/4.11.2/"),
    ),  # type: ignore
    "https://sources.debian.org/copyright/license/debianutils/4.11.2/": CreativeWork(
        identifier="SMAIL-GPL",
        name="SMAIL General Public License",
        url=AnyUrl("https://sources.debian.org/copyright/license/debianutils/4.11.2/"),
    ),  # type: ignore
    "SMLNJ": CreativeWork(
        identifier="SMLNJ",
        name="Standard ML of New Jersey License",
        url=AnyUrl("https://www.smlnj.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SMLNJ": CreativeWork(
        identifier="SMLNJ",
        name="Standard ML of New Jersey License",
        url=AnyUrl("https://www.smlnj.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SMLNJ.html": CreativeWork(
        identifier="SMLNJ",
        name="Standard ML of New Jersey License",
        url=AnyUrl("https://www.smlnj.org/license.html"),
    ),  # type: ignore
    "https://www.smlnj.org/license.html": CreativeWork(
        identifier="SMLNJ",
        name="Standard ML of New Jersey License",
        url=AnyUrl("https://www.smlnj.org/license.html"),
    ),  # type: ignore
    "SMPPL": CreativeWork(
        identifier="SMPPL",
        name="Secure Messaging Protocol Public License",
        url=AnyUrl(
            "https://github.com/dcblake/SMP/blob/master/Documentation/License.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SMPPL": CreativeWork(
        identifier="SMPPL",
        name="Secure Messaging Protocol Public License",
        url=AnyUrl(
            "https://github.com/dcblake/SMP/blob/master/Documentation/License.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SMPPL.html": CreativeWork(
        identifier="SMPPL",
        name="Secure Messaging Protocol Public License",
        url=AnyUrl(
            "https://github.com/dcblake/SMP/blob/master/Documentation/License.txt"
        ),
    ),  # type: ignore
    "https://github.com/dcblake/SMP/blob/master/Documentation/License.txt": CreativeWork(
        identifier="SMPPL",
        name="Secure Messaging Protocol Public License",
        url=AnyUrl(
            "https://github.com/dcblake/SMP/blob/master/Documentation/License.txt"
        ),
    ),  # type: ignore
    "SNIA": CreativeWork(
        identifier="SNIA",
        name="SNIA Public License 1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/SNIA_Public_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/SNIA": CreativeWork(
        identifier="SNIA",
        name="SNIA Public License 1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/SNIA_Public_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/SNIA.html": CreativeWork(
        identifier="SNIA",
        name="SNIA Public License 1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/SNIA_Public_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/SNIA_Public_License": CreativeWork(
        identifier="SNIA",
        name="SNIA Public License 1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/SNIA_Public_License"),
    ),  # type: ignore
    "snprintf": CreativeWork(
        identifier="snprintf",
        name="snprintf License",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/master/openbsd-compat/bsd-snprintf.c#L2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/snprintf": CreativeWork(
        identifier="snprintf",
        name="snprintf License",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/master/openbsd-compat/bsd-snprintf.c#L2"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/snprintf.html": CreativeWork(
        identifier="snprintf",
        name="snprintf License",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/master/openbsd-compat/bsd-snprintf.c#L2"
        ),
    ),  # type: ignore
    "https://github.com/openssh/openssh-portable/blob/master/openbsd-compat/bsd-snprintf.c#L2": CreativeWork(
        identifier="snprintf",
        name="snprintf License",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/master/openbsd-compat/bsd-snprintf.c#L2"
        ),
    ),  # type: ignore
    "SOFA": CreativeWork(
        identifier="SOFA",
        name="SOFA Software License",
        url=AnyUrl("http://www.iausofa.org/tandc.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SOFA": CreativeWork(
        identifier="SOFA",
        name="SOFA Software License",
        url=AnyUrl("http://www.iausofa.org/tandc.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/SOFA.html": CreativeWork(
        identifier="SOFA",
        name="SOFA Software License",
        url=AnyUrl("http://www.iausofa.org/tandc.html"),
    ),  # type: ignore
    "http://www.iausofa.org/tandc.html": CreativeWork(
        identifier="SOFA",
        name="SOFA Software License",
        url=AnyUrl("http://www.iausofa.org/tandc.html"),
    ),  # type: ignore
    "softSurfer": CreativeWork(
        identifier="softSurfer",
        name="softSurfer License",
        url=AnyUrl("https://github.com/mm2/Little-CMS/blob/master/src/cmssm.c#L207"),
    ),  # type: ignore
    "https://spdx.org/licenses/softSurfer": CreativeWork(
        identifier="softSurfer",
        name="softSurfer License",
        url=AnyUrl("https://github.com/mm2/Little-CMS/blob/master/src/cmssm.c#L207"),
    ),  # type: ignore
    "https://spdx.org/licenses/softSurfer.html": CreativeWork(
        identifier="softSurfer",
        name="softSurfer License",
        url=AnyUrl("https://github.com/mm2/Little-CMS/blob/master/src/cmssm.c#L207"),
    ),  # type: ignore
    "https://github.com/mm2/Little-CMS/blob/master/src/cmssm.c#L207": CreativeWork(
        identifier="softSurfer",
        name="softSurfer License",
        url=AnyUrl("https://github.com/mm2/Little-CMS/blob/master/src/cmssm.c#L207"),
    ),  # type: ignore
    "Soundex": CreativeWork(
        identifier="Soundex",
        name="Soundex License",
        url=AnyUrl(
            "https://metacpan.org/release/RJBS/Text-Soundex-3.05/source/Soundex.pm#L3-11"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Soundex": CreativeWork(
        identifier="Soundex",
        name="Soundex License",
        url=AnyUrl(
            "https://metacpan.org/release/RJBS/Text-Soundex-3.05/source/Soundex.pm#L3-11"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Soundex.html": CreativeWork(
        identifier="Soundex",
        name="Soundex License",
        url=AnyUrl(
            "https://metacpan.org/release/RJBS/Text-Soundex-3.05/source/Soundex.pm#L3-11"
        ),
    ),  # type: ignore
    "https://metacpan.org/release/RJBS/Text-Soundex-3.05/source/Soundex.pm#L3-11": CreativeWork(
        identifier="Soundex",
        name="Soundex License",
        url=AnyUrl(
            "https://metacpan.org/release/RJBS/Text-Soundex-3.05/source/Soundex.pm#L3-11"
        ),
    ),  # type: ignore
    "Spencer-86": CreativeWork(
        identifier="Spencer-86",
        name="Spencer License 86",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Spencer-86": CreativeWork(
        identifier="Spencer-86",
        name="Spencer License 86",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Spencer-86.html": CreativeWork(
        identifier="Spencer-86",
        name="Spencer License 86",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License"
        ),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License": CreativeWork(
        identifier="Spencer-86",
        name="Spencer License 86",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License"
        ),
    ),  # type: ignore
    "Spencer-94": CreativeWork(
        identifier="Spencer-94",
        name="Spencer License 94",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Spencer-94": CreativeWork(
        identifier="Spencer-94",
        name="Spencer License 94",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Spencer-94.html": CreativeWork(
        identifier="Spencer-94",
        name="Spencer License 94",
        url=AnyUrl(
            "https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License"
        ),
    ),  # type: ignore
    "Spencer-99": CreativeWork(
        identifier="Spencer-99",
        name="Spencer License 99",
        url=AnyUrl(
            "http://www.opensource.apple.com/source/tcl/tcl-5/tcl/generic/regfronts.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Spencer-99": CreativeWork(
        identifier="Spencer-99",
        name="Spencer License 99",
        url=AnyUrl(
            "http://www.opensource.apple.com/source/tcl/tcl-5/tcl/generic/regfronts.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Spencer-99.html": CreativeWork(
        identifier="Spencer-99",
        name="Spencer License 99",
        url=AnyUrl(
            "http://www.opensource.apple.com/source/tcl/tcl-5/tcl/generic/regfronts.c"
        ),
    ),  # type: ignore
    "http://www.opensource.apple.com/source/tcl/tcl-5/tcl/generic/regfronts.c": CreativeWork(
        identifier="Spencer-99",
        name="Spencer License 99",
        url=AnyUrl(
            "http://www.opensource.apple.com/source/tcl/tcl-5/tcl/generic/regfronts.c"
        ),
    ),  # type: ignore
    "SPL-1.0": CreativeWork(
        identifier="SPL-1.0",
        name="Sun Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/SPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/SPL-1.0": CreativeWork(
        identifier="SPL-1.0",
        name="Sun Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/SPL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/SPL-1.0.html": CreativeWork(
        identifier="SPL-1.0",
        name="Sun Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/SPL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/SPL-1.0": CreativeWork(
        identifier="SPL-1.0",
        name="Sun Public License v1.0",
        url=AnyUrl("https://opensource.org/licenses/SPL-1.0"),
    ),  # type: ignore
    "ssh-keyscan": CreativeWork(
        identifier="ssh-keyscan",
        name="ssh-keyscan License",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/master/LICENCE#L82"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ssh-keyscan": CreativeWork(
        identifier="ssh-keyscan",
        name="ssh-keyscan License",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/master/LICENCE#L82"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ssh-keyscan.html": CreativeWork(
        identifier="ssh-keyscan",
        name="ssh-keyscan License",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/master/LICENCE#L82"
        ),
    ),  # type: ignore
    "https://github.com/openssh/openssh-portable/blob/master/LICENCE#L82": CreativeWork(
        identifier="ssh-keyscan",
        name="ssh-keyscan License",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/master/LICENCE#L82"
        ),
    ),  # type: ignore
    "SSH-OpenSSH": CreativeWork(
        identifier="SSH-OpenSSH",
        name="SSH OpenSSH license",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/LICENCE#L10"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SSH-OpenSSH": CreativeWork(
        identifier="SSH-OpenSSH",
        name="SSH OpenSSH license",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/LICENCE#L10"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SSH-OpenSSH.html": CreativeWork(
        identifier="SSH-OpenSSH",
        name="SSH OpenSSH license",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/LICENCE#L10"
        ),
    ),  # type: ignore
    "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/LICENCE#L10": CreativeWork(
        identifier="SSH-OpenSSH",
        name="SSH OpenSSH license",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/LICENCE#L10"
        ),
    ),  # type: ignore
    "SSH-short": CreativeWork(
        identifier="SSH-short",
        name="SSH short notice",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/pathnames.h"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SSH-short": CreativeWork(
        identifier="SSH-short",
        name="SSH short notice",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/pathnames.h"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SSH-short.html": CreativeWork(
        identifier="SSH-short",
        name="SSH short notice",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/pathnames.h"
        ),
    ),  # type: ignore
    "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/pathnames.h": CreativeWork(
        identifier="SSH-short",
        name="SSH short notice",
        url=AnyUrl(
            "https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/pathnames.h"
        ),
    ),  # type: ignore
    "SSLeay-standalone": CreativeWork(
        identifier="SSLeay-standalone",
        name="SSLeay License - standalone",
        url=AnyUrl(
            "https://www.tq-group.com/filedownloads/files/software-license-conditions/OriginalSSLeay/OriginalSSLeay.pdf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SSLeay-standalone": CreativeWork(
        identifier="SSLeay-standalone",
        name="SSLeay License - standalone",
        url=AnyUrl(
            "https://www.tq-group.com/filedownloads/files/software-license-conditions/OriginalSSLeay/OriginalSSLeay.pdf"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SSLeay-standalone.html": CreativeWork(
        identifier="SSLeay-standalone",
        name="SSLeay License - standalone",
        url=AnyUrl(
            "https://www.tq-group.com/filedownloads/files/software-license-conditions/OriginalSSLeay/OriginalSSLeay.pdf"
        ),
    ),  # type: ignore
    "https://www.tq-group.com/filedownloads/files/software-license-conditions/OriginalSSLeay/OriginalSSLeay.pdf": CreativeWork(
        identifier="SSLeay-standalone",
        name="SSLeay License - standalone",
        url=AnyUrl(
            "https://www.tq-group.com/filedownloads/files/software-license-conditions/OriginalSSLeay/OriginalSSLeay.pdf"
        ),
    ),  # type: ignore
    "SSPL-1.0": CreativeWork(
        identifier="SSPL-1.0",
        name="Server Side Public License, v 1",
        url=AnyUrl("https://www.mongodb.com/licensing/server-side-public-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/SSPL-1.0": CreativeWork(
        identifier="SSPL-1.0",
        name="Server Side Public License, v 1",
        url=AnyUrl("https://www.mongodb.com/licensing/server-side-public-license"),
    ),  # type: ignore
    "https://spdx.org/licenses/SSPL-1.0.html": CreativeWork(
        identifier="SSPL-1.0",
        name="Server Side Public License, v 1",
        url=AnyUrl("https://www.mongodb.com/licensing/server-side-public-license"),
    ),  # type: ignore
    "https://www.mongodb.com/licensing/server-side-public-license": CreativeWork(
        identifier="SSPL-1.0",
        name="Server Side Public License, v 1",
        url=AnyUrl("https://www.mongodb.com/licensing/server-side-public-license"),
    ),  # type: ignore
    "StandardML-NJ": CreativeWork(
        identifier="StandardML-NJ",
        name="Standard ML of New Jersey License",
        url=AnyUrl("https://www.smlnj.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/StandardML-NJ": CreativeWork(
        identifier="StandardML-NJ",
        name="Standard ML of New Jersey License",
        url=AnyUrl("https://www.smlnj.org/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/StandardML-NJ.html": CreativeWork(
        identifier="StandardML-NJ",
        name="Standard ML of New Jersey License",
        url=AnyUrl("https://www.smlnj.org/license.html"),
    ),  # type: ignore
    "SugarCRM-1.1.3": CreativeWork(
        identifier="SugarCRM-1.1.3",
        name="SugarCRM Public License v1.1.3",
        url=AnyUrl("http://www.sugarcrm.com/crm/SPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/SugarCRM-1.1.3": CreativeWork(
        identifier="SugarCRM-1.1.3",
        name="SugarCRM Public License v1.1.3",
        url=AnyUrl("http://www.sugarcrm.com/crm/SPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/SugarCRM-1.1.3.html": CreativeWork(
        identifier="SugarCRM-1.1.3",
        name="SugarCRM Public License v1.1.3",
        url=AnyUrl("http://www.sugarcrm.com/crm/SPL"),
    ),  # type: ignore
    "http://www.sugarcrm.com/crm/SPL": CreativeWork(
        identifier="SugarCRM-1.1.3",
        name="SugarCRM Public License v1.1.3",
        url=AnyUrl("http://www.sugarcrm.com/crm/SPL"),
    ),  # type: ignore
    "SUL-1.0": CreativeWork(
        identifier="SUL-1.0",
        name="Sustainable Use License v1.0",
        url=AnyUrl("https://github.com/n8n-io/n8n/blob/master/LICENSE.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/SUL-1.0": CreativeWork(
        identifier="SUL-1.0",
        name="Sustainable Use License v1.0",
        url=AnyUrl("https://github.com/n8n-io/n8n/blob/master/LICENSE.md"),
    ),  # type: ignore
    "https://spdx.org/licenses/SUL-1.0.html": CreativeWork(
        identifier="SUL-1.0",
        name="Sustainable Use License v1.0",
        url=AnyUrl("https://github.com/n8n-io/n8n/blob/master/LICENSE.md"),
    ),  # type: ignore
    "https://github.com/n8n-io/n8n/blob/master/LICENSE.md": CreativeWork(
        identifier="SUL-1.0",
        name="Sustainable Use License v1.0",
        url=AnyUrl("https://github.com/n8n-io/n8n/blob/master/LICENSE.md"),
    ),  # type: ignore
    "Sun-PPP": CreativeWork(
        identifier="Sun-PPP",
        name="Sun PPP License",
        url=AnyUrl("https://github.com/ppp-project/ppp/blob/master/pppd/eap.c#L7-L16"),
    ),  # type: ignore
    "https://spdx.org/licenses/Sun-PPP": CreativeWork(
        identifier="Sun-PPP",
        name="Sun PPP License",
        url=AnyUrl("https://github.com/ppp-project/ppp/blob/master/pppd/eap.c#L7-L16"),
    ),  # type: ignore
    "https://spdx.org/licenses/Sun-PPP.html": CreativeWork(
        identifier="Sun-PPP",
        name="Sun PPP License",
        url=AnyUrl("https://github.com/ppp-project/ppp/blob/master/pppd/eap.c#L7-L16"),
    ),  # type: ignore
    "https://github.com/ppp-project/ppp/blob/master/pppd/eap.c#L7-L16": CreativeWork(
        identifier="Sun-PPP",
        name="Sun PPP License",
        url=AnyUrl("https://github.com/ppp-project/ppp/blob/master/pppd/eap.c#L7-L16"),
    ),  # type: ignore
    "Sun-PPP-2000": CreativeWork(
        identifier="Sun-PPP-2000",
        name="Sun PPP License (2000)",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/modules/ppp_ahdlc.c#L7-L19"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Sun-PPP-2000": CreativeWork(
        identifier="Sun-PPP-2000",
        name="Sun PPP License (2000)",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/modules/ppp_ahdlc.c#L7-L19"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Sun-PPP-2000.html": CreativeWork(
        identifier="Sun-PPP-2000",
        name="Sun PPP License (2000)",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/modules/ppp_ahdlc.c#L7-L19"
        ),
    ),  # type: ignore
    "https://github.com/ppp-project/ppp/blob/master/modules/ppp_ahdlc.c#L7-L19": CreativeWork(
        identifier="Sun-PPP-2000",
        name="Sun PPP License (2000)",
        url=AnyUrl(
            "https://github.com/ppp-project/ppp/blob/master/modules/ppp_ahdlc.c#L7-L19"
        ),
    ),  # type: ignore
    "SunPro": CreativeWork(
        identifier="SunPro",
        name="SunPro License",
        url=AnyUrl(
            "https://github.com/freebsd/freebsd-src/blob/main/lib/msun/src/e_acosh.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SunPro": CreativeWork(
        identifier="SunPro",
        name="SunPro License",
        url=AnyUrl(
            "https://github.com/freebsd/freebsd-src/blob/main/lib/msun/src/e_acosh.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/SunPro.html": CreativeWork(
        identifier="SunPro",
        name="SunPro License",
        url=AnyUrl(
            "https://github.com/freebsd/freebsd-src/blob/main/lib/msun/src/e_acosh.c"
        ),
    ),  # type: ignore
    "https://github.com/freebsd/freebsd-src/blob/main/lib/msun/src/e_acosh.c": CreativeWork(
        identifier="SunPro",
        name="SunPro License",
        url=AnyUrl(
            "https://github.com/freebsd/freebsd-src/blob/main/lib/msun/src/e_acosh.c"
        ),
    ),  # type: ignore
    "SWL": CreativeWork(
        identifier="SWL",
        name="Scheme Widget Library (SWL) Software License Agreement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/SWL"),
    ),  # type: ignore
    "https://spdx.org/licenses/SWL": CreativeWork(
        identifier="SWL",
        name="Scheme Widget Library (SWL) Software License Agreement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/SWL"),
    ),  # type: ignore
    "https://spdx.org/licenses/SWL.html": CreativeWork(
        identifier="SWL",
        name="Scheme Widget Library (SWL) Software License Agreement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/SWL"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/SWL": CreativeWork(
        identifier="SWL",
        name="Scheme Widget Library (SWL) Software License Agreement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/SWL"),
    ),  # type: ignore
    "swrule": CreativeWork(
        identifier="swrule",
        name="swrule License",
        url=AnyUrl(
            "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/misc/swrule.sty"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/swrule": CreativeWork(
        identifier="swrule",
        name="swrule License",
        url=AnyUrl(
            "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/misc/swrule.sty"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/swrule.html": CreativeWork(
        identifier="swrule",
        name="swrule License",
        url=AnyUrl(
            "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/misc/swrule.sty"
        ),
    ),  # type: ignore
    "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/misc/swrule.sty": CreativeWork(
        identifier="swrule",
        name="swrule License",
        url=AnyUrl(
            "https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/misc/swrule.sty"
        ),
    ),  # type: ignore
    "Symlinks": CreativeWork(
        identifier="Symlinks",
        name="Symlinks License",
        url=AnyUrl(
            "https://www.mail-archive.com/debian-bugs-rc@lists.debian.org/msg11494.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Symlinks": CreativeWork(
        identifier="Symlinks",
        name="Symlinks License",
        url=AnyUrl(
            "https://www.mail-archive.com/debian-bugs-rc@lists.debian.org/msg11494.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Symlinks.html": CreativeWork(
        identifier="Symlinks",
        name="Symlinks License",
        url=AnyUrl(
            "https://www.mail-archive.com/debian-bugs-rc@lists.debian.org/msg11494.html"
        ),
    ),  # type: ignore
    "https://www.mail-archive.com/debian-bugs-rc@lists.debian.org/msg11494.html": CreativeWork(
        identifier="Symlinks",
        name="Symlinks License",
        url=AnyUrl(
            "https://www.mail-archive.com/debian-bugs-rc@lists.debian.org/msg11494.html"
        ),
    ),  # type: ignore
    "TAPR-OHL-1.0": CreativeWork(
        identifier="TAPR-OHL-1.0",
        name="TAPR Open Hardware License v1.0",
        url=AnyUrl("https://www.tapr.org/OHL"),
    ),  # type: ignore
    "https://spdx.org/licenses/TAPR-OHL-1.0": CreativeWork(
        identifier="TAPR-OHL-1.0",
        name="TAPR Open Hardware License v1.0",
        url=AnyUrl("https://www.tapr.org/OHL"),
    ),  # type: ignore
    "https://spdx.org/licenses/TAPR-OHL-1.0.html": CreativeWork(
        identifier="TAPR-OHL-1.0",
        name="TAPR Open Hardware License v1.0",
        url=AnyUrl("https://www.tapr.org/OHL"),
    ),  # type: ignore
    "https://www.tapr.org/OHL": CreativeWork(
        identifier="TAPR-OHL-1.0",
        name="TAPR Open Hardware License v1.0",
        url=AnyUrl("https://www.tapr.org/OHL"),
    ),  # type: ignore
    "TCL": CreativeWork(
        identifier="TCL",
        name="TCL/TK License",
        url=AnyUrl("http://www.tcl.tk/software/tcltk/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/TCL": CreativeWork(
        identifier="TCL",
        name="TCL/TK License",
        url=AnyUrl("http://www.tcl.tk/software/tcltk/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/TCL.html": CreativeWork(
        identifier="TCL",
        name="TCL/TK License",
        url=AnyUrl("http://www.tcl.tk/software/tcltk/license.html"),
    ),  # type: ignore
    "http://www.tcl.tk/software/tcltk/license.html": CreativeWork(
        identifier="TCL",
        name="TCL/TK License",
        url=AnyUrl("http://www.tcl.tk/software/tcltk/license.html"),
    ),  # type: ignore
    "TCP-wrappers": CreativeWork(
        identifier="TCP-wrappers",
        name="TCP Wrappers License",
        url=AnyUrl("http://rc.quest.com/topics/openssh/license.php#tcpwrappers"),
    ),  # type: ignore
    "https://spdx.org/licenses/TCP-wrappers": CreativeWork(
        identifier="TCP-wrappers",
        name="TCP Wrappers License",
        url=AnyUrl("http://rc.quest.com/topics/openssh/license.php#tcpwrappers"),
    ),  # type: ignore
    "https://spdx.org/licenses/TCP-wrappers.html": CreativeWork(
        identifier="TCP-wrappers",
        name="TCP Wrappers License",
        url=AnyUrl("http://rc.quest.com/topics/openssh/license.php#tcpwrappers"),
    ),  # type: ignore
    "http://rc.quest.com/topics/openssh/license.php#tcpwrappers": CreativeWork(
        identifier="TCP-wrappers",
        name="TCP Wrappers License",
        url=AnyUrl("http://rc.quest.com/topics/openssh/license.php#tcpwrappers"),
    ),  # type: ignore
    "TekHVC": CreativeWork(
        identifier="TekHVC",
        name="TekHVC License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/COPYING?ref_type=heads#L138-171"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TekHVC": CreativeWork(
        identifier="TekHVC",
        name="TekHVC License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/COPYING?ref_type=heads#L138-171"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TekHVC.html": CreativeWork(
        identifier="TekHVC",
        name="TekHVC License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/COPYING?ref_type=heads#L138-171"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/COPYING?ref_type=heads#L138-171": CreativeWork(
        identifier="TekHVC",
        name="TekHVC License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/COPYING?ref_type=heads#L138-171"
        ),
    ),  # type: ignore
    "TermReadKey": CreativeWork(
        identifier="TermReadKey",
        name="TermReadKey License",
        url=AnyUrl(
            "https://github.com/jonathanstowe/TermReadKey/blob/master/README#L9-L10"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TermReadKey": CreativeWork(
        identifier="TermReadKey",
        name="TermReadKey License",
        url=AnyUrl(
            "https://github.com/jonathanstowe/TermReadKey/blob/master/README#L9-L10"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TermReadKey.html": CreativeWork(
        identifier="TermReadKey",
        name="TermReadKey License",
        url=AnyUrl(
            "https://github.com/jonathanstowe/TermReadKey/blob/master/README#L9-L10"
        ),
    ),  # type: ignore
    "https://github.com/jonathanstowe/TermReadKey/blob/master/README#L9-L10": CreativeWork(
        identifier="TermReadKey",
        name="TermReadKey License",
        url=AnyUrl(
            "https://github.com/jonathanstowe/TermReadKey/blob/master/README#L9-L10"
        ),
    ),  # type: ignore
    "TGPPL-1.0": CreativeWork(
        identifier="TGPPL-1.0",
        name="Transitive Grace Period Public Licence 1.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TGPPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/TGPPL-1.0": CreativeWork(
        identifier="TGPPL-1.0",
        name="Transitive Grace Period Public Licence 1.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TGPPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/TGPPL-1.0.html": CreativeWork(
        identifier="TGPPL-1.0",
        name="Transitive Grace Period Public Licence 1.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TGPPL"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/TGPPL": CreativeWork(
        identifier="TGPPL-1.0",
        name="Transitive Grace Period Public Licence 1.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TGPPL"),
    ),  # type: ignore
    "ThirdEye": CreativeWork(
        identifier="ThirdEye",
        name="ThirdEye License",
        url=AnyUrl(
            "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/symconst.h#n11"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ThirdEye": CreativeWork(
        identifier="ThirdEye",
        name="ThirdEye License",
        url=AnyUrl(
            "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/symconst.h#n11"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/ThirdEye.html": CreativeWork(
        identifier="ThirdEye",
        name="ThirdEye License",
        url=AnyUrl(
            "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/symconst.h#n11"
        ),
    ),  # type: ignore
    "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/symconst.h#n11": CreativeWork(
        identifier="ThirdEye",
        name="ThirdEye License",
        url=AnyUrl(
            "https://sourceware.org/cgit/binutils-gdb/tree/include/coff/symconst.h#n11"
        ),
    ),  # type: ignore
    "threeparttable": CreativeWork(
        identifier="threeparttable",
        name="threeparttable License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Threeparttable"),
    ),  # type: ignore
    "https://spdx.org/licenses/threeparttable": CreativeWork(
        identifier="threeparttable",
        name="threeparttable License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Threeparttable"),
    ),  # type: ignore
    "https://spdx.org/licenses/threeparttable.html": CreativeWork(
        identifier="threeparttable",
        name="threeparttable License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Threeparttable"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Threeparttable": CreativeWork(
        identifier="threeparttable",
        name="threeparttable License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Threeparttable"),
    ),  # type: ignore
    "TMate": CreativeWork(
        identifier="TMate",
        name="TMate Open Source License",
        url=AnyUrl("http://svnkit.com/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/TMate": CreativeWork(
        identifier="TMate",
        name="TMate Open Source License",
        url=AnyUrl("http://svnkit.com/license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/TMate.html": CreativeWork(
        identifier="TMate",
        name="TMate Open Source License",
        url=AnyUrl("http://svnkit.com/license.html"),
    ),  # type: ignore
    "http://svnkit.com/license.html": CreativeWork(
        identifier="TMate",
        name="TMate Open Source License",
        url=AnyUrl("http://svnkit.com/license.html"),
    ),  # type: ignore
    "TORQUE-1.1": CreativeWork(
        identifier="TORQUE-1.1",
        name="TORQUE v2.5+ Software License v1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TORQUEv1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/TORQUE-1.1": CreativeWork(
        identifier="TORQUE-1.1",
        name="TORQUE v2.5+ Software License v1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TORQUEv1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/TORQUE-1.1.html": CreativeWork(
        identifier="TORQUE-1.1",
        name="TORQUE v2.5+ Software License v1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TORQUEv1.1"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/TORQUEv1.1": CreativeWork(
        identifier="TORQUE-1.1",
        name="TORQUE v2.5+ Software License v1.1",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TORQUEv1.1"),
    ),  # type: ignore
    "TOSL": CreativeWork(
        identifier="TOSL",
        name="Trusster Open Source License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TOSL"),
    ),  # type: ignore
    "https://spdx.org/licenses/TOSL": CreativeWork(
        identifier="TOSL",
        name="Trusster Open Source License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TOSL"),
    ),  # type: ignore
    "https://spdx.org/licenses/TOSL.html": CreativeWork(
        identifier="TOSL",
        name="Trusster Open Source License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TOSL"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/TOSL": CreativeWork(
        identifier="TOSL",
        name="Trusster Open Source License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TOSL"),
    ),  # type: ignore
    "TPDL": CreativeWork(
        identifier="TPDL",
        name="Time::ParseDate License",
        url=AnyUrl("https://metacpan.org/pod/Time::ParseDate#LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/TPDL": CreativeWork(
        identifier="TPDL",
        name="Time::ParseDate License",
        url=AnyUrl("https://metacpan.org/pod/Time::ParseDate#LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/TPDL.html": CreativeWork(
        identifier="TPDL",
        name="Time::ParseDate License",
        url=AnyUrl("https://metacpan.org/pod/Time::ParseDate#LICENSE"),
    ),  # type: ignore
    "https://metacpan.org/pod/Time::ParseDate#LICENSE": CreativeWork(
        identifier="TPDL",
        name="Time::ParseDate License",
        url=AnyUrl("https://metacpan.org/pod/Time::ParseDate#LICENSE"),
    ),  # type: ignore
    "TPL-1.0": CreativeWork(
        identifier="TPL-1.0",
        name="THOR Public License 1.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:ThorPublicLicense"),
    ),  # type: ignore
    "https://spdx.org/licenses/TPL-1.0": CreativeWork(
        identifier="TPL-1.0",
        name="THOR Public License 1.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:ThorPublicLicense"),
    ),  # type: ignore
    "https://spdx.org/licenses/TPL-1.0.html": CreativeWork(
        identifier="TPL-1.0",
        name="THOR Public License 1.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:ThorPublicLicense"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing:ThorPublicLicense": CreativeWork(
        identifier="TPL-1.0",
        name="THOR Public License 1.0",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing:ThorPublicLicense"),
    ),  # type: ignore
    "TrustedQSL": CreativeWork(
        identifier="TrustedQSL",
        name="TrustedQSL License",
        url=AnyUrl(
            "https://sourceforge.net/p/trustedqsl/tqsl/ci/master/tree/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TrustedQSL": CreativeWork(
        identifier="TrustedQSL",
        name="TrustedQSL License",
        url=AnyUrl(
            "https://sourceforge.net/p/trustedqsl/tqsl/ci/master/tree/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TrustedQSL.html": CreativeWork(
        identifier="TrustedQSL",
        name="TrustedQSL License",
        url=AnyUrl(
            "https://sourceforge.net/p/trustedqsl/tqsl/ci/master/tree/LICENSE.txt"
        ),
    ),  # type: ignore
    "https://sourceforge.net/p/trustedqsl/tqsl/ci/master/tree/LICENSE.txt": CreativeWork(
        identifier="TrustedQSL",
        name="TrustedQSL License",
        url=AnyUrl(
            "https://sourceforge.net/p/trustedqsl/tqsl/ci/master/tree/LICENSE.txt"
        ),
    ),  # type: ignore
    "TTWL": CreativeWork(
        identifier="TTWL",
        name="Text-Tabs+Wrap License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TTWL"),
    ),  # type: ignore
    "https://spdx.org/licenses/TTWL": CreativeWork(
        identifier="TTWL",
        name="Text-Tabs+Wrap License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TTWL"),
    ),  # type: ignore
    "https://spdx.org/licenses/TTWL.html": CreativeWork(
        identifier="TTWL",
        name="Text-Tabs+Wrap License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TTWL"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/TTWL": CreativeWork(
        identifier="TTWL",
        name="Text-Tabs+Wrap License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/TTWL"),
    ),  # type: ignore
    "TTYP0": CreativeWork(
        identifier="TTYP0",
        name="TTYP0 License",
        url=AnyUrl("https://people.mpi-inf.mpg.de/~uwe/misc/uw-ttyp0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/TTYP0": CreativeWork(
        identifier="TTYP0",
        name="TTYP0 License",
        url=AnyUrl("https://people.mpi-inf.mpg.de/~uwe/misc/uw-ttyp0/"),
    ),  # type: ignore
    "https://spdx.org/licenses/TTYP0.html": CreativeWork(
        identifier="TTYP0",
        name="TTYP0 License",
        url=AnyUrl("https://people.mpi-inf.mpg.de/~uwe/misc/uw-ttyp0/"),
    ),  # type: ignore
    "https://people.mpi-inf.mpg.de/~uwe/misc/uw-ttyp0/": CreativeWork(
        identifier="TTYP0",
        name="TTYP0 License",
        url=AnyUrl("https://people.mpi-inf.mpg.de/~uwe/misc/uw-ttyp0/"),
    ),  # type: ignore
    "TU-Berlin-1.0": CreativeWork(
        identifier="TU-Berlin-1.0",
        name="Technische Universitaet Berlin License 1.0",
        url=AnyUrl(
            "https://github.com/swh/ladspa/blob/7bf6f3799fdba70fda297c2d8fd9f526803d9680/gsm/COPYRIGHT"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TU-Berlin-1.0": CreativeWork(
        identifier="TU-Berlin-1.0",
        name="Technische Universitaet Berlin License 1.0",
        url=AnyUrl(
            "https://github.com/swh/ladspa/blob/7bf6f3799fdba70fda297c2d8fd9f526803d9680/gsm/COPYRIGHT"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TU-Berlin-1.0.html": CreativeWork(
        identifier="TU-Berlin-1.0",
        name="Technische Universitaet Berlin License 1.0",
        url=AnyUrl(
            "https://github.com/swh/ladspa/blob/7bf6f3799fdba70fda297c2d8fd9f526803d9680/gsm/COPYRIGHT"
        ),
    ),  # type: ignore
    "https://github.com/swh/ladspa/blob/7bf6f3799fdba70fda297c2d8fd9f526803d9680/gsm/COPYRIGHT": CreativeWork(
        identifier="TU-Berlin-1.0",
        name="Technische Universitaet Berlin License 1.0",
        url=AnyUrl(
            "https://github.com/swh/ladspa/blob/7bf6f3799fdba70fda297c2d8fd9f526803d9680/gsm/COPYRIGHT"
        ),
    ),  # type: ignore
    "TU-Berlin-2.0": CreativeWork(
        identifier="TU-Berlin-2.0",
        name="Technische Universitaet Berlin License 2.0",
        url=AnyUrl(
            "https://github.com/CorsixTH/deps/blob/fd339a9f526d1d9c9f01ccf39e438a015da50035/licences/libgsm.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TU-Berlin-2.0": CreativeWork(
        identifier="TU-Berlin-2.0",
        name="Technische Universitaet Berlin License 2.0",
        url=AnyUrl(
            "https://github.com/CorsixTH/deps/blob/fd339a9f526d1d9c9f01ccf39e438a015da50035/licences/libgsm.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/TU-Berlin-2.0.html": CreativeWork(
        identifier="TU-Berlin-2.0",
        name="Technische Universitaet Berlin License 2.0",
        url=AnyUrl(
            "https://github.com/CorsixTH/deps/blob/fd339a9f526d1d9c9f01ccf39e438a015da50035/licences/libgsm.txt"
        ),
    ),  # type: ignore
    "https://github.com/CorsixTH/deps/blob/fd339a9f526d1d9c9f01ccf39e438a015da50035/licences/libgsm.txt": CreativeWork(
        identifier="TU-Berlin-2.0",
        name="Technische Universitaet Berlin License 2.0",
        url=AnyUrl(
            "https://github.com/CorsixTH/deps/blob/fd339a9f526d1d9c9f01ccf39e438a015da50035/licences/libgsm.txt"
        ),
    ),  # type: ignore
    "Ubuntu-font-1.0": CreativeWork(
        identifier="Ubuntu-font-1.0",
        name="Ubuntu Font Licence v1.0",
        url=AnyUrl("https://ubuntu.com/legal/font-licence"),
    ),  # type: ignore
    "https://spdx.org/licenses/Ubuntu-font-1.0": CreativeWork(
        identifier="Ubuntu-font-1.0",
        name="Ubuntu Font Licence v1.0",
        url=AnyUrl("https://ubuntu.com/legal/font-licence"),
    ),  # type: ignore
    "https://spdx.org/licenses/Ubuntu-font-1.0.html": CreativeWork(
        identifier="Ubuntu-font-1.0",
        name="Ubuntu Font Licence v1.0",
        url=AnyUrl("https://ubuntu.com/legal/font-licence"),
    ),  # type: ignore
    "https://ubuntu.com/legal/font-licence": CreativeWork(
        identifier="Ubuntu-font-1.0",
        name="Ubuntu Font Licence v1.0",
        url=AnyUrl("https://ubuntu.com/legal/font-licence"),
    ),  # type: ignore
    "UCAR": CreativeWork(
        identifier="UCAR",
        name="UCAR License",
        url=AnyUrl("https://github.com/Unidata/UDUNITS-2/blob/master/COPYRIGHT"),
    ),  # type: ignore
    "https://spdx.org/licenses/UCAR": CreativeWork(
        identifier="UCAR",
        name="UCAR License",
        url=AnyUrl("https://github.com/Unidata/UDUNITS-2/blob/master/COPYRIGHT"),
    ),  # type: ignore
    "https://spdx.org/licenses/UCAR.html": CreativeWork(
        identifier="UCAR",
        name="UCAR License",
        url=AnyUrl("https://github.com/Unidata/UDUNITS-2/blob/master/COPYRIGHT"),
    ),  # type: ignore
    "https://github.com/Unidata/UDUNITS-2/blob/master/COPYRIGHT": CreativeWork(
        identifier="UCAR",
        name="UCAR License",
        url=AnyUrl("https://github.com/Unidata/UDUNITS-2/blob/master/COPYRIGHT"),
    ),  # type: ignore
    "UCL-1.0": CreativeWork(
        identifier="UCL-1.0",
        name="Upstream Compatibility License v1.0",
        url=AnyUrl("https://opensource.org/licenses/UCL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/UCL-1.0": CreativeWork(
        identifier="UCL-1.0",
        name="Upstream Compatibility License v1.0",
        url=AnyUrl("https://opensource.org/licenses/UCL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/UCL-1.0.html": CreativeWork(
        identifier="UCL-1.0",
        name="Upstream Compatibility License v1.0",
        url=AnyUrl("https://opensource.org/licenses/UCL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/UCL-1.0": CreativeWork(
        identifier="UCL-1.0",
        name="Upstream Compatibility License v1.0",
        url=AnyUrl("https://opensource.org/licenses/UCL-1.0"),
    ),  # type: ignore
    "ulem": CreativeWork(
        identifier="ulem",
        name="ulem License",
        url=AnyUrl("https://mirrors.ctan.org/macros/latex/contrib/ulem/README"),
    ),  # type: ignore
    "https://spdx.org/licenses/ulem": CreativeWork(
        identifier="ulem",
        name="ulem License",
        url=AnyUrl("https://mirrors.ctan.org/macros/latex/contrib/ulem/README"),
    ),  # type: ignore
    "https://spdx.org/licenses/ulem.html": CreativeWork(
        identifier="ulem",
        name="ulem License",
        url=AnyUrl("https://mirrors.ctan.org/macros/latex/contrib/ulem/README"),
    ),  # type: ignore
    "https://mirrors.ctan.org/macros/latex/contrib/ulem/README": CreativeWork(
        identifier="ulem",
        name="ulem License",
        url=AnyUrl("https://mirrors.ctan.org/macros/latex/contrib/ulem/README"),
    ),  # type: ignore
    "UMich-Merit": CreativeWork(
        identifier="UMich-Merit",
        name="Michigan/Merit Networks License",
        url=AnyUrl("https://github.com/radcli/radcli/blob/master/COPYRIGHT#L64"),
    ),  # type: ignore
    "https://spdx.org/licenses/UMich-Merit": CreativeWork(
        identifier="UMich-Merit",
        name="Michigan/Merit Networks License",
        url=AnyUrl("https://github.com/radcli/radcli/blob/master/COPYRIGHT#L64"),
    ),  # type: ignore
    "https://spdx.org/licenses/UMich-Merit.html": CreativeWork(
        identifier="UMich-Merit",
        name="Michigan/Merit Networks License",
        url=AnyUrl("https://github.com/radcli/radcli/blob/master/COPYRIGHT#L64"),
    ),  # type: ignore
    "https://github.com/radcli/radcli/blob/master/COPYRIGHT#L64": CreativeWork(
        identifier="UMich-Merit",
        name="Michigan/Merit Networks License",
        url=AnyUrl("https://github.com/radcli/radcli/blob/master/COPYRIGHT#L64"),
    ),  # type: ignore
    "Unicode-3.0": CreativeWork(
        identifier="Unicode-3.0",
        name="Unicode License v3",
        url=AnyUrl("https://www.unicode.org/license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unicode-3.0": CreativeWork(
        identifier="Unicode-3.0",
        name="Unicode License v3",
        url=AnyUrl("https://www.unicode.org/license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unicode-3.0.html": CreativeWork(
        identifier="Unicode-3.0",
        name="Unicode License v3",
        url=AnyUrl("https://www.unicode.org/license.txt"),
    ),  # type: ignore
    "https://www.unicode.org/license.txt": CreativeWork(
        identifier="Unicode-3.0",
        name="Unicode License v3",
        url=AnyUrl("https://www.unicode.org/license.txt"),
    ),  # type: ignore
    "Unicode-DFS-2015": CreativeWork(
        identifier="Unicode-DFS-2015",
        name="Unicode License Agreement - Data Files and Software (2015)",
        url=AnyUrl(
            "https://web.archive.org/web/20151224134844/http://unicode.org/copyright.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Unicode-DFS-2015": CreativeWork(
        identifier="Unicode-DFS-2015",
        name="Unicode License Agreement - Data Files and Software (2015)",
        url=AnyUrl(
            "https://web.archive.org/web/20151224134844/http://unicode.org/copyright.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Unicode-DFS-2015.html": CreativeWork(
        identifier="Unicode-DFS-2015",
        name="Unicode License Agreement - Data Files and Software (2015)",
        url=AnyUrl(
            "https://web.archive.org/web/20151224134844/http://unicode.org/copyright.html"
        ),
    ),  # type: ignore
    "https://web.archive.org/web/20151224134844/http://unicode.org/copyright.html": CreativeWork(
        identifier="Unicode-DFS-2015",
        name="Unicode License Agreement - Data Files and Software (2015)",
        url=AnyUrl(
            "https://web.archive.org/web/20151224134844/http://unicode.org/copyright.html"
        ),
    ),  # type: ignore
    "Unicode-DFS-2016": CreativeWork(
        identifier="Unicode-DFS-2016",
        name="Unicode License Agreement - Data Files and Software (2016)",
        url=AnyUrl("https://www.unicode.org/license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unicode-DFS-2016": CreativeWork(
        identifier="Unicode-DFS-2016",
        name="Unicode License Agreement - Data Files and Software (2016)",
        url=AnyUrl("https://www.unicode.org/license.txt"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unicode-DFS-2016.html": CreativeWork(
        identifier="Unicode-DFS-2016",
        name="Unicode License Agreement - Data Files and Software (2016)",
        url=AnyUrl("https://www.unicode.org/license.txt"),
    ),  # type: ignore
    "Unicode-TOU": CreativeWork(
        identifier="Unicode-TOU",
        name="Unicode Terms of Use",
        url=AnyUrl(
            "http://web.archive.org/web/20140704074106/http://www.unicode.org/copyright.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Unicode-TOU": CreativeWork(
        identifier="Unicode-TOU",
        name="Unicode Terms of Use",
        url=AnyUrl(
            "http://web.archive.org/web/20140704074106/http://www.unicode.org/copyright.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Unicode-TOU.html": CreativeWork(
        identifier="Unicode-TOU",
        name="Unicode Terms of Use",
        url=AnyUrl(
            "http://web.archive.org/web/20140704074106/http://www.unicode.org/copyright.html"
        ),
    ),  # type: ignore
    "http://web.archive.org/web/20140704074106/http://www.unicode.org/copyright.html": CreativeWork(
        identifier="Unicode-TOU",
        name="Unicode Terms of Use",
        url=AnyUrl(
            "http://web.archive.org/web/20140704074106/http://www.unicode.org/copyright.html"
        ),
    ),  # type: ignore
    "UnixCrypt": CreativeWork(
        identifier="UnixCrypt",
        name="UnixCrypt License",
        url=AnyUrl(
            "https://foss.heptapod.net/python-libs/passlib/-/blob/branch/stable/LICENSE#L70"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/UnixCrypt": CreativeWork(
        identifier="UnixCrypt",
        name="UnixCrypt License",
        url=AnyUrl(
            "https://foss.heptapod.net/python-libs/passlib/-/blob/branch/stable/LICENSE#L70"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/UnixCrypt.html": CreativeWork(
        identifier="UnixCrypt",
        name="UnixCrypt License",
        url=AnyUrl(
            "https://foss.heptapod.net/python-libs/passlib/-/blob/branch/stable/LICENSE#L70"
        ),
    ),  # type: ignore
    "https://foss.heptapod.net/python-libs/passlib/-/blob/branch/stable/LICENSE#L70": CreativeWork(
        identifier="UnixCrypt",
        name="UnixCrypt License",
        url=AnyUrl(
            "https://foss.heptapod.net/python-libs/passlib/-/blob/branch/stable/LICENSE#L70"
        ),
    ),  # type: ignore
    "Unlicense": CreativeWork(
        identifier="Unlicense",
        name="The Unlicense",
        url=AnyUrl("https://unlicense.org/"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unlicense": CreativeWork(
        identifier="Unlicense",
        name="The Unlicense",
        url=AnyUrl("https://unlicense.org/"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unlicense.html": CreativeWork(
        identifier="Unlicense",
        name="The Unlicense",
        url=AnyUrl("https://unlicense.org/"),
    ),  # type: ignore
    "https://unlicense.org/": CreativeWork(
        identifier="Unlicense",
        name="The Unlicense",
        url=AnyUrl("https://unlicense.org/"),
    ),  # type: ignore
    "Unlicense-libtelnet": CreativeWork(
        identifier="Unlicense-libtelnet",
        name="Unlicense - libtelnet variant",
        url=AnyUrl("https://github.com/seanmiddleditch/libtelnet/blob/develop/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unlicense-libtelnet": CreativeWork(
        identifier="Unlicense-libtelnet",
        name="Unlicense - libtelnet variant",
        url=AnyUrl("https://github.com/seanmiddleditch/libtelnet/blob/develop/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unlicense-libtelnet.html": CreativeWork(
        identifier="Unlicense-libtelnet",
        name="Unlicense - libtelnet variant",
        url=AnyUrl("https://github.com/seanmiddleditch/libtelnet/blob/develop/COPYING"),
    ),  # type: ignore
    "https://github.com/seanmiddleditch/libtelnet/blob/develop/COPYING": CreativeWork(
        identifier="Unlicense-libtelnet",
        name="Unlicense - libtelnet variant",
        url=AnyUrl("https://github.com/seanmiddleditch/libtelnet/blob/develop/COPYING"),
    ),  # type: ignore
    "Unlicense-libwhirlpool": CreativeWork(
        identifier="Unlicense-libwhirlpool",
        name="Unlicense - libwhirlpool variant",
        url=AnyUrl("https://github.com/dfateyev/libwhirlpool/blob/master/README#L27"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unlicense-libwhirlpool": CreativeWork(
        identifier="Unlicense-libwhirlpool",
        name="Unlicense - libwhirlpool variant",
        url=AnyUrl("https://github.com/dfateyev/libwhirlpool/blob/master/README#L27"),
    ),  # type: ignore
    "https://spdx.org/licenses/Unlicense-libwhirlpool.html": CreativeWork(
        identifier="Unlicense-libwhirlpool",
        name="Unlicense - libwhirlpool variant",
        url=AnyUrl("https://github.com/dfateyev/libwhirlpool/blob/master/README#L27"),
    ),  # type: ignore
    "https://github.com/dfateyev/libwhirlpool/blob/master/README#L27": CreativeWork(
        identifier="Unlicense-libwhirlpool",
        name="Unlicense - libwhirlpool variant",
        url=AnyUrl("https://github.com/dfateyev/libwhirlpool/blob/master/README#L27"),
    ),  # type: ignore
    "UnRAR": CreativeWork(
        identifier="UnRAR",
        name="UnRAR License",
        url=AnyUrl(
            "https://public.dhe.ibm.com/aix/freeSoftware/aixtoolbox/LICENSES/unRAR.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/UnRAR": CreativeWork(
        identifier="UnRAR",
        name="UnRAR License",
        url=AnyUrl(
            "https://public.dhe.ibm.com/aix/freeSoftware/aixtoolbox/LICENSES/unRAR.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/UnRAR.html": CreativeWork(
        identifier="UnRAR",
        name="UnRAR License",
        url=AnyUrl(
            "https://public.dhe.ibm.com/aix/freeSoftware/aixtoolbox/LICENSES/unRAR.txt"
        ),
    ),  # type: ignore
    "https://public.dhe.ibm.com/aix/freeSoftware/aixtoolbox/LICENSES/unRAR.txt": CreativeWork(
        identifier="UnRAR",
        name="UnRAR License",
        url=AnyUrl(
            "https://public.dhe.ibm.com/aix/freeSoftware/aixtoolbox/LICENSES/unRAR.txt"
        ),
    ),  # type: ignore
    "UPL-1.0": CreativeWork(
        identifier="UPL-1.0",
        name="Universal Permissive License v1.0",
        url=AnyUrl("https://opensource.org/licenses/UPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/UPL-1.0": CreativeWork(
        identifier="UPL-1.0",
        name="Universal Permissive License v1.0",
        url=AnyUrl("https://opensource.org/licenses/UPL"),
    ),  # type: ignore
    "https://spdx.org/licenses/UPL-1.0.html": CreativeWork(
        identifier="UPL-1.0",
        name="Universal Permissive License v1.0",
        url=AnyUrl("https://opensource.org/licenses/UPL"),
    ),  # type: ignore
    "https://opensource.org/licenses/UPL": CreativeWork(
        identifier="UPL-1.0",
        name="Universal Permissive License v1.0",
        url=AnyUrl("https://opensource.org/licenses/UPL"),
    ),  # type: ignore
    "URT-RLE": CreativeWork(
        identifier="URT-RLE",
        name="Utah Raster Toolkit Run Length Encoded License",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/other/pnmtorle.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/URT-RLE": CreativeWork(
        identifier="URT-RLE",
        name="Utah Raster Toolkit Run Length Encoded License",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/other/pnmtorle.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/URT-RLE.html": CreativeWork(
        identifier="URT-RLE",
        name="Utah Raster Toolkit Run Length Encoded License",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/other/pnmtorle.c"
        ),
    ),  # type: ignore
    "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/other/pnmtorle.c": CreativeWork(
        identifier="URT-RLE",
        name="Utah Raster Toolkit Run Length Encoded License",
        url=AnyUrl(
            "https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/other/pnmtorle.c"
        ),
    ),  # type: ignore
    "Vim": CreativeWork(
        identifier="Vim",
        name="Vim License",
        url=AnyUrl("http://vimdoc.sourceforge.net/htmldoc/uganda.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Vim": CreativeWork(
        identifier="Vim",
        name="Vim License",
        url=AnyUrl("http://vimdoc.sourceforge.net/htmldoc/uganda.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Vim.html": CreativeWork(
        identifier="Vim",
        name="Vim License",
        url=AnyUrl("http://vimdoc.sourceforge.net/htmldoc/uganda.html"),
    ),  # type: ignore
    "http://vimdoc.sourceforge.net/htmldoc/uganda.html": CreativeWork(
        identifier="Vim",
        name="Vim License",
        url=AnyUrl("http://vimdoc.sourceforge.net/htmldoc/uganda.html"),
    ),  # type: ignore
    "Vixie-Cron": CreativeWork(
        identifier="Vixie-Cron",
        name="Vixie Cron License",
        url=AnyUrl(
            "https://github.com/vixie/cron/tree/545b3f5246824a9cda5905eeb7cf019c95e66995"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Vixie-Cron": CreativeWork(
        identifier="Vixie-Cron",
        name="Vixie Cron License",
        url=AnyUrl(
            "https://github.com/vixie/cron/tree/545b3f5246824a9cda5905eeb7cf019c95e66995"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Vixie-Cron.html": CreativeWork(
        identifier="Vixie-Cron",
        name="Vixie Cron License",
        url=AnyUrl(
            "https://github.com/vixie/cron/tree/545b3f5246824a9cda5905eeb7cf019c95e66995"
        ),
    ),  # type: ignore
    "https://github.com/vixie/cron/tree/545b3f5246824a9cda5905eeb7cf019c95e66995": CreativeWork(
        identifier="Vixie-Cron",
        name="Vixie Cron License",
        url=AnyUrl(
            "https://github.com/vixie/cron/tree/545b3f5246824a9cda5905eeb7cf019c95e66995"
        ),
    ),  # type: ignore
    "VOSTROM": CreativeWork(
        identifier="VOSTROM",
        name="VOSTROM Public License for Open Source",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/VOSTROM"),
    ),  # type: ignore
    "https://spdx.org/licenses/VOSTROM": CreativeWork(
        identifier="VOSTROM",
        name="VOSTROM Public License for Open Source",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/VOSTROM"),
    ),  # type: ignore
    "https://spdx.org/licenses/VOSTROM.html": CreativeWork(
        identifier="VOSTROM",
        name="VOSTROM Public License for Open Source",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/VOSTROM"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/VOSTROM": CreativeWork(
        identifier="VOSTROM",
        name="VOSTROM Public License for Open Source",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/VOSTROM"),
    ),  # type: ignore
    "VSL-1.0": CreativeWork(
        identifier="VSL-1.0",
        name="Vovida Software License v1.0",
        url=AnyUrl("https://opensource.org/licenses/VSL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/VSL-1.0": CreativeWork(
        identifier="VSL-1.0",
        name="Vovida Software License v1.0",
        url=AnyUrl("https://opensource.org/licenses/VSL-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/VSL-1.0.html": CreativeWork(
        identifier="VSL-1.0",
        name="Vovida Software License v1.0",
        url=AnyUrl("https://opensource.org/licenses/VSL-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/VSL-1.0": CreativeWork(
        identifier="VSL-1.0",
        name="Vovida Software License v1.0",
        url=AnyUrl("https://opensource.org/licenses/VSL-1.0"),
    ),  # type: ignore
    "W3C": CreativeWork(
        identifier="W3C",
        name="W3C Software Notice and License (2002-12-31)",
        url=AnyUrl(
            "http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/W3C": CreativeWork(
        identifier="W3C",
        name="W3C Software Notice and License (2002-12-31)",
        url=AnyUrl(
            "http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/W3C.html": CreativeWork(
        identifier="W3C",
        name="W3C Software Notice and License (2002-12-31)",
        url=AnyUrl(
            "http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231.html"
        ),
    ),  # type: ignore
    "http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231.html": CreativeWork(
        identifier="W3C",
        name="W3C Software Notice and License (2002-12-31)",
        url=AnyUrl(
            "http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231.html"
        ),
    ),  # type: ignore
    "W3C-19980720": CreativeWork(
        identifier="W3C-19980720",
        name="W3C Software Notice and License (1998-07-20)",
        url=AnyUrl(
            "http://www.w3.org/Consortium/Legal/copyright-software-19980720.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/W3C-19980720": CreativeWork(
        identifier="W3C-19980720",
        name="W3C Software Notice and License (1998-07-20)",
        url=AnyUrl(
            "http://www.w3.org/Consortium/Legal/copyright-software-19980720.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/W3C-19980720.html": CreativeWork(
        identifier="W3C-19980720",
        name="W3C Software Notice and License (1998-07-20)",
        url=AnyUrl(
            "http://www.w3.org/Consortium/Legal/copyright-software-19980720.html"
        ),
    ),  # type: ignore
    "http://www.w3.org/Consortium/Legal/copyright-software-19980720.html": CreativeWork(
        identifier="W3C-19980720",
        name="W3C Software Notice and License (1998-07-20)",
        url=AnyUrl(
            "http://www.w3.org/Consortium/Legal/copyright-software-19980720.html"
        ),
    ),  # type: ignore
    "W3C-20150513": CreativeWork(
        identifier="W3C-20150513",
        name="W3C Software Notice and Document License (2015-05-13)",
        url=AnyUrl(
            "https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/W3C-20150513": CreativeWork(
        identifier="W3C-20150513",
        name="W3C Software Notice and Document License (2015-05-13)",
        url=AnyUrl(
            "https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/W3C-20150513.html": CreativeWork(
        identifier="W3C-20150513",
        name="W3C Software Notice and Document License (2015-05-13)",
        url=AnyUrl(
            "https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document"
        ),
    ),  # type: ignore
    "https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document": CreativeWork(
        identifier="W3C-20150513",
        name="W3C Software Notice and Document License (2015-05-13)",
        url=AnyUrl(
            "https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document"
        ),
    ),  # type: ignore
    "w3m": CreativeWork(
        identifier="w3m",
        name="w3m License",
        url=AnyUrl("https://github.com/tats/w3m/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/w3m": CreativeWork(
        identifier="w3m",
        name="w3m License",
        url=AnyUrl("https://github.com/tats/w3m/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/w3m.html": CreativeWork(
        identifier="w3m",
        name="w3m License",
        url=AnyUrl("https://github.com/tats/w3m/blob/master/COPYING"),
    ),  # type: ignore
    "https://github.com/tats/w3m/blob/master/COPYING": CreativeWork(
        identifier="w3m",
        name="w3m License",
        url=AnyUrl("https://github.com/tats/w3m/blob/master/COPYING"),
    ),  # type: ignore
    "Watcom-1.0": CreativeWork(
        identifier="Watcom-1.0",
        name="Sybase Open Watcom Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Watcom-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Watcom-1.0": CreativeWork(
        identifier="Watcom-1.0",
        name="Sybase Open Watcom Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Watcom-1.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/Watcom-1.0.html": CreativeWork(
        identifier="Watcom-1.0",
        name="Sybase Open Watcom Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Watcom-1.0"),
    ),  # type: ignore
    "https://opensource.org/licenses/Watcom-1.0": CreativeWork(
        identifier="Watcom-1.0",
        name="Sybase Open Watcom Public License 1.0",
        url=AnyUrl("https://opensource.org/licenses/Watcom-1.0"),
    ),  # type: ignore
    "Widget-Workshop": CreativeWork(
        identifier="Widget-Workshop",
        name="Widget Workshop License",
        url=AnyUrl("https://github.com/novnc/noVNC/blob/master/core/crypto/des.js#L24"),
    ),  # type: ignore
    "https://spdx.org/licenses/Widget-Workshop": CreativeWork(
        identifier="Widget-Workshop",
        name="Widget Workshop License",
        url=AnyUrl("https://github.com/novnc/noVNC/blob/master/core/crypto/des.js#L24"),
    ),  # type: ignore
    "https://spdx.org/licenses/Widget-Workshop.html": CreativeWork(
        identifier="Widget-Workshop",
        name="Widget Workshop License",
        url=AnyUrl("https://github.com/novnc/noVNC/blob/master/core/crypto/des.js#L24"),
    ),  # type: ignore
    "https://github.com/novnc/noVNC/blob/master/core/crypto/des.js#L24": CreativeWork(
        identifier="Widget-Workshop",
        name="Widget Workshop License",
        url=AnyUrl("https://github.com/novnc/noVNC/blob/master/core/crypto/des.js#L24"),
    ),  # type: ignore
    "WordNet": CreativeWork(
        identifier="WordNet",
        name="WordNet License",
        url=AnyUrl("https://wordnet.princeton.edu/license-and-commercial-use"),
    ),  # type: ignore
    "https://spdx.org/licenses/WordNet": CreativeWork(
        identifier="WordNet",
        name="WordNet License",
        url=AnyUrl("https://wordnet.princeton.edu/license-and-commercial-use"),
    ),  # type: ignore
    "https://spdx.org/licenses/WordNet.html": CreativeWork(
        identifier="WordNet",
        name="WordNet License",
        url=AnyUrl("https://wordnet.princeton.edu/license-and-commercial-use"),
    ),  # type: ignore
    "https://wordnet.princeton.edu/license-and-commercial-use": CreativeWork(
        identifier="WordNet",
        name="WordNet License",
        url=AnyUrl("https://wordnet.princeton.edu/license-and-commercial-use"),
    ),  # type: ignore
    "Wsuipa": CreativeWork(
        identifier="Wsuipa",
        name="Wsuipa License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Wsuipa"),
    ),  # type: ignore
    "https://spdx.org/licenses/Wsuipa": CreativeWork(
        identifier="Wsuipa",
        name="Wsuipa License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Wsuipa"),
    ),  # type: ignore
    "https://spdx.org/licenses/Wsuipa.html": CreativeWork(
        identifier="Wsuipa",
        name="Wsuipa License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Wsuipa"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Wsuipa": CreativeWork(
        identifier="Wsuipa",
        name="Wsuipa License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Wsuipa"),
    ),  # type: ignore
    "WTFNMFPL": CreativeWork(
        identifier="WTFNMFPL",
        name="Do What The F*ck You Want To But It's Not My Fault Public License",
        url=AnyUrl(
            "https://github.com/adversary-org/wtfnmf/raw/refs/tags/1.0/COPYING.WTFNMFPL"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/WTFNMFPL": CreativeWork(
        identifier="WTFNMFPL",
        name="Do What The F*ck You Want To But It's Not My Fault Public License",
        url=AnyUrl(
            "https://github.com/adversary-org/wtfnmf/raw/refs/tags/1.0/COPYING.WTFNMFPL"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/WTFNMFPL.html": CreativeWork(
        identifier="WTFNMFPL",
        name="Do What The F*ck You Want To But It's Not My Fault Public License",
        url=AnyUrl(
            "https://github.com/adversary-org/wtfnmf/raw/refs/tags/1.0/COPYING.WTFNMFPL"
        ),
    ),  # type: ignore
    "https://github.com/adversary-org/wtfnmf/raw/refs/tags/1.0/COPYING.WTFNMFPL": CreativeWork(
        identifier="WTFNMFPL",
        name="Do What The F*ck You Want To But It's Not My Fault Public License",
        url=AnyUrl(
            "https://github.com/adversary-org/wtfnmf/raw/refs/tags/1.0/COPYING.WTFNMFPL"
        ),
    ),  # type: ignore
    "WTFPL": CreativeWork(
        identifier="WTFPL",
        name="Do What The F*ck You Want To Public License",
        url=AnyUrl("http://www.wtfpl.net/about/"),
    ),  # type: ignore
    "https://spdx.org/licenses/WTFPL": CreativeWork(
        identifier="WTFPL",
        name="Do What The F*ck You Want To Public License",
        url=AnyUrl("http://www.wtfpl.net/about/"),
    ),  # type: ignore
    "https://spdx.org/licenses/WTFPL.html": CreativeWork(
        identifier="WTFPL",
        name="Do What The F*ck You Want To Public License",
        url=AnyUrl("http://www.wtfpl.net/about/"),
    ),  # type: ignore
    "http://www.wtfpl.net/about/": CreativeWork(
        identifier="WTFPL",
        name="Do What The F*ck You Want To Public License",
        url=AnyUrl("http://www.wtfpl.net/about/"),
    ),  # type: ignore
    "wwl": CreativeWork(
        identifier="wwl",
        name="WWL License",
        url=AnyUrl("http://www.db.net/downloads/wwl+db-1.3.tgz"),
    ),  # type: ignore
    "https://spdx.org/licenses/wwl": CreativeWork(
        identifier="wwl",
        name="WWL License",
        url=AnyUrl("http://www.db.net/downloads/wwl+db-1.3.tgz"),
    ),  # type: ignore
    "https://spdx.org/licenses/wwl.html": CreativeWork(
        identifier="wwl",
        name="WWL License",
        url=AnyUrl("http://www.db.net/downloads/wwl+db-1.3.tgz"),
    ),  # type: ignore
    "http://www.db.net/downloads/wwl+db-1.3.tgz": CreativeWork(
        identifier="wwl",
        name="WWL License",
        url=AnyUrl("http://www.db.net/downloads/wwl+db-1.3.tgz"),
    ),  # type: ignore
    "wxWindows": CreativeWork(
        identifier="wxWindows",
        name="wxWindows Library License",
        url=AnyUrl("https://opensource.org/licenses/WXwindows"),
    ),  # type: ignore
    "https://spdx.org/licenses/wxWindows": CreativeWork(
        identifier="wxWindows",
        name="wxWindows Library License",
        url=AnyUrl("https://opensource.org/licenses/WXwindows"),
    ),  # type: ignore
    "https://spdx.org/licenses/wxWindows.html": CreativeWork(
        identifier="wxWindows",
        name="wxWindows Library License",
        url=AnyUrl("https://opensource.org/licenses/WXwindows"),
    ),  # type: ignore
    "https://opensource.org/licenses/WXwindows": CreativeWork(
        identifier="wxWindows",
        name="wxWindows Library License",
        url=AnyUrl("https://opensource.org/licenses/WXwindows"),
    ),  # type: ignore
    "X11": CreativeWork(
        identifier="X11",
        name="X11 License",
        url=AnyUrl("http://www.xfree86.org/3.3.6/COPYRIGHT2.html#3"),
    ),  # type: ignore
    "https://spdx.org/licenses/X11": CreativeWork(
        identifier="X11",
        name="X11 License",
        url=AnyUrl("http://www.xfree86.org/3.3.6/COPYRIGHT2.html#3"),
    ),  # type: ignore
    "https://spdx.org/licenses/X11.html": CreativeWork(
        identifier="X11",
        name="X11 License",
        url=AnyUrl("http://www.xfree86.org/3.3.6/COPYRIGHT2.html#3"),
    ),  # type: ignore
    "http://www.xfree86.org/3.3.6/COPYRIGHT2.html#3": CreativeWork(
        identifier="X11",
        name="X11 License",
        url=AnyUrl("http://www.xfree86.org/3.3.6/COPYRIGHT2.html#3"),
    ),  # type: ignore
    "X11-distribute-modifications-variant": CreativeWork(
        identifier="X11-distribute-modifications-variant",
        name="X11 License Distribution Modification Variant",
        url=AnyUrl("https://github.com/mirror/ncurses/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/X11-distribute-modifications-variant": CreativeWork(
        identifier="X11-distribute-modifications-variant",
        name="X11 License Distribution Modification Variant",
        url=AnyUrl("https://github.com/mirror/ncurses/blob/master/COPYING"),
    ),  # type: ignore
    "https://spdx.org/licenses/X11-distribute-modifications-variant.html": CreativeWork(
        identifier="X11-distribute-modifications-variant",
        name="X11 License Distribution Modification Variant",
        url=AnyUrl("https://github.com/mirror/ncurses/blob/master/COPYING"),
    ),  # type: ignore
    "https://github.com/mirror/ncurses/blob/master/COPYING": CreativeWork(
        identifier="X11-distribute-modifications-variant",
        name="X11 License Distribution Modification Variant",
        url=AnyUrl("https://github.com/mirror/ncurses/blob/master/COPYING"),
    ),  # type: ignore
    "X11-no-permit-persons": CreativeWork(
        identifier="X11-no-permit-persons",
        name="X11 no permit persons clause",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxinerama/-/blob/cc22c2f60c3862482562955116d5455263b443dc/COPYING#L44-66"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/X11-no-permit-persons": CreativeWork(
        identifier="X11-no-permit-persons",
        name="X11 no permit persons clause",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxinerama/-/blob/cc22c2f60c3862482562955116d5455263b443dc/COPYING#L44-66"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/X11-no-permit-persons.html": CreativeWork(
        identifier="X11-no-permit-persons",
        name="X11 no permit persons clause",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxinerama/-/blob/cc22c2f60c3862482562955116d5455263b443dc/COPYING#L44-66"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xorg/lib/libxinerama/-/blob/cc22c2f60c3862482562955116d5455263b443dc/COPYING#L44-66": CreativeWork(
        identifier="X11-no-permit-persons",
        name="X11 no permit persons clause",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xorg/lib/libxinerama/-/blob/cc22c2f60c3862482562955116d5455263b443dc/COPYING#L44-66"
        ),
    ),  # type: ignore
    "X11-swapped": CreativeWork(
        identifier="X11-swapped",
        name="X11 swapped final paragraphs",
        url=AnyUrl(
            "https://github.com/fedeinthemix/chez-srfi/blob/master/srfi/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/X11-swapped": CreativeWork(
        identifier="X11-swapped",
        name="X11 swapped final paragraphs",
        url=AnyUrl(
            "https://github.com/fedeinthemix/chez-srfi/blob/master/srfi/LICENSE"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/X11-swapped.html": CreativeWork(
        identifier="X11-swapped",
        name="X11 swapped final paragraphs",
        url=AnyUrl(
            "https://github.com/fedeinthemix/chez-srfi/blob/master/srfi/LICENSE"
        ),
    ),  # type: ignore
    "https://github.com/fedeinthemix/chez-srfi/blob/master/srfi/LICENSE": CreativeWork(
        identifier="X11-swapped",
        name="X11 swapped final paragraphs",
        url=AnyUrl(
            "https://github.com/fedeinthemix/chez-srfi/blob/master/srfi/LICENSE"
        ),
    ),  # type: ignore
    "Xdebug-1.03": CreativeWork(
        identifier="Xdebug-1.03",
        name="Xdebug License v 1.03",
        url=AnyUrl("https://github.com/xdebug/xdebug/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/Xdebug-1.03": CreativeWork(
        identifier="Xdebug-1.03",
        name="Xdebug License v 1.03",
        url=AnyUrl("https://github.com/xdebug/xdebug/blob/master/LICENSE"),
    ),  # type: ignore
    "https://spdx.org/licenses/Xdebug-1.03.html": CreativeWork(
        identifier="Xdebug-1.03",
        name="Xdebug License v 1.03",
        url=AnyUrl("https://github.com/xdebug/xdebug/blob/master/LICENSE"),
    ),  # type: ignore
    "https://github.com/xdebug/xdebug/blob/master/LICENSE": CreativeWork(
        identifier="Xdebug-1.03",
        name="Xdebug License v 1.03",
        url=AnyUrl("https://github.com/xdebug/xdebug/blob/master/LICENSE"),
    ),  # type: ignore
    "Xerox": CreativeWork(
        identifier="Xerox",
        name="Xerox License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Xerox"),
    ),  # type: ignore
    "https://spdx.org/licenses/Xerox": CreativeWork(
        identifier="Xerox",
        name="Xerox License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Xerox"),
    ),  # type: ignore
    "https://spdx.org/licenses/Xerox.html": CreativeWork(
        identifier="Xerox",
        name="Xerox License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Xerox"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Xerox": CreativeWork(
        identifier="Xerox",
        name="Xerox License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Xerox"),
    ),  # type: ignore
    "Xfig": CreativeWork(
        identifier="Xfig",
        name="Xfig License",
        url=AnyUrl(
            "https://github.com/Distrotech/transfig/blob/master/transfig/transfig.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Xfig": CreativeWork(
        identifier="Xfig",
        name="Xfig License",
        url=AnyUrl(
            "https://github.com/Distrotech/transfig/blob/master/transfig/transfig.c"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Xfig.html": CreativeWork(
        identifier="Xfig",
        name="Xfig License",
        url=AnyUrl(
            "https://github.com/Distrotech/transfig/blob/master/transfig/transfig.c"
        ),
    ),  # type: ignore
    "https://github.com/Distrotech/transfig/blob/master/transfig/transfig.c": CreativeWork(
        identifier="Xfig",
        name="Xfig License",
        url=AnyUrl(
            "https://github.com/Distrotech/transfig/blob/master/transfig/transfig.c"
        ),
    ),  # type: ignore
    "XFree86-1.1": CreativeWork(
        identifier="XFree86-1.1",
        name="XFree86 License 1.1",
        url=AnyUrl("http://www.xfree86.org/current/LICENSE4.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/XFree86-1.1": CreativeWork(
        identifier="XFree86-1.1",
        name="XFree86 License 1.1",
        url=AnyUrl("http://www.xfree86.org/current/LICENSE4.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/XFree86-1.1.html": CreativeWork(
        identifier="XFree86-1.1",
        name="XFree86 License 1.1",
        url=AnyUrl("http://www.xfree86.org/current/LICENSE4.html"),
    ),  # type: ignore
    "http://www.xfree86.org/current/LICENSE4.html": CreativeWork(
        identifier="XFree86-1.1",
        name="XFree86 License 1.1",
        url=AnyUrl("http://www.xfree86.org/current/LICENSE4.html"),
    ),  # type: ignore
    "xinetd": CreativeWork(
        identifier="xinetd",
        name="xinetd License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Xinetd_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/xinetd": CreativeWork(
        identifier="xinetd",
        name="xinetd License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Xinetd_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/xinetd.html": CreativeWork(
        identifier="xinetd",
        name="xinetd License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Xinetd_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Xinetd_License": CreativeWork(
        identifier="xinetd",
        name="xinetd License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Xinetd_License"),
    ),  # type: ignore
    "xkeyboard-config-Zinoviev": CreativeWork(
        identifier="xkeyboard-config-Zinoviev",
        name="xkeyboard-config Zinoviev License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/blob/master/COPYING?ref_type=heads#L178"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/xkeyboard-config-Zinoviev": CreativeWork(
        identifier="xkeyboard-config-Zinoviev",
        name="xkeyboard-config Zinoviev License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/blob/master/COPYING?ref_type=heads#L178"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/xkeyboard-config-Zinoviev.html": CreativeWork(
        identifier="xkeyboard-config-Zinoviev",
        name="xkeyboard-config Zinoviev License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/blob/master/COPYING?ref_type=heads#L178"
        ),
    ),  # type: ignore
    "https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/blob/master/COPYING?ref_type=heads#L178": CreativeWork(
        identifier="xkeyboard-config-Zinoviev",
        name="xkeyboard-config Zinoviev License",
        url=AnyUrl(
            "https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/blob/master/COPYING?ref_type=heads#L178"
        ),
    ),  # type: ignore
    "xlock": CreativeWork(
        identifier="xlock",
        name="xlock License",
        url=AnyUrl("https://fossies.org/linux/tiff/contrib/ras/ras2tif.c"),
    ),  # type: ignore
    "https://spdx.org/licenses/xlock": CreativeWork(
        identifier="xlock",
        name="xlock License",
        url=AnyUrl("https://fossies.org/linux/tiff/contrib/ras/ras2tif.c"),
    ),  # type: ignore
    "https://spdx.org/licenses/xlock.html": CreativeWork(
        identifier="xlock",
        name="xlock License",
        url=AnyUrl("https://fossies.org/linux/tiff/contrib/ras/ras2tif.c"),
    ),  # type: ignore
    "https://fossies.org/linux/tiff/contrib/ras/ras2tif.c": CreativeWork(
        identifier="xlock",
        name="xlock License",
        url=AnyUrl("https://fossies.org/linux/tiff/contrib/ras/ras2tif.c"),
    ),  # type: ignore
    "Xnet": CreativeWork(
        identifier="Xnet",
        name="X.Net License",
        url=AnyUrl("https://opensource.org/licenses/Xnet"),
    ),  # type: ignore
    "https://spdx.org/licenses/Xnet": CreativeWork(
        identifier="Xnet",
        name="X.Net License",
        url=AnyUrl("https://opensource.org/licenses/Xnet"),
    ),  # type: ignore
    "https://spdx.org/licenses/Xnet.html": CreativeWork(
        identifier="Xnet",
        name="X.Net License",
        url=AnyUrl("https://opensource.org/licenses/Xnet"),
    ),  # type: ignore
    "https://opensource.org/licenses/Xnet": CreativeWork(
        identifier="Xnet",
        name="X.Net License",
        url=AnyUrl("https://opensource.org/licenses/Xnet"),
    ),  # type: ignore
    "xpp": CreativeWork(
        identifier="xpp",
        name="XPP License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/xpp"),
    ),  # type: ignore
    "https://spdx.org/licenses/xpp": CreativeWork(
        identifier="xpp",
        name="XPP License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/xpp"),
    ),  # type: ignore
    "https://spdx.org/licenses/xpp.html": CreativeWork(
        identifier="xpp",
        name="XPP License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/xpp"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/xpp": CreativeWork(
        identifier="xpp",
        name="XPP License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/xpp"),
    ),  # type: ignore
    "XSkat": CreativeWork(
        identifier="XSkat",
        name="XSkat License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/XSkat_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/XSkat": CreativeWork(
        identifier="XSkat",
        name="XSkat License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/XSkat_License"),
    ),  # type: ignore
    "https://spdx.org/licenses/XSkat.html": CreativeWork(
        identifier="XSkat",
        name="XSkat License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/XSkat_License"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/XSkat_License": CreativeWork(
        identifier="XSkat",
        name="XSkat License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/XSkat_License"),
    ),  # type: ignore
    "xzoom": CreativeWork(
        identifier="xzoom",
        name="xzoom License",
        url=AnyUrl(
            "https://metadata.ftp-master.debian.org/changelogs//main/x/xzoom/xzoom_0.3-27_copyright"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/xzoom": CreativeWork(
        identifier="xzoom",
        name="xzoom License",
        url=AnyUrl(
            "https://metadata.ftp-master.debian.org/changelogs//main/x/xzoom/xzoom_0.3-27_copyright"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/xzoom.html": CreativeWork(
        identifier="xzoom",
        name="xzoom License",
        url=AnyUrl(
            "https://metadata.ftp-master.debian.org/changelogs//main/x/xzoom/xzoom_0.3-27_copyright"
        ),
    ),  # type: ignore
    "https://metadata.ftp-master.debian.org/changelogs//main/x/xzoom/xzoom_0.3-27_copyright": CreativeWork(
        identifier="xzoom",
        name="xzoom License",
        url=AnyUrl(
            "https://metadata.ftp-master.debian.org/changelogs//main/x/xzoom/xzoom_0.3-27_copyright"
        ),
    ),  # type: ignore
    "YPL-1.0": CreativeWork(
        identifier="YPL-1.0",
        name="Yahoo! Public License v1.0",
        url=AnyUrl("http://www.zimbra.com/license/yahoo_public_license_1.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/YPL-1.0": CreativeWork(
        identifier="YPL-1.0",
        name="Yahoo! Public License v1.0",
        url=AnyUrl("http://www.zimbra.com/license/yahoo_public_license_1.0.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/YPL-1.0.html": CreativeWork(
        identifier="YPL-1.0",
        name="Yahoo! Public License v1.0",
        url=AnyUrl("http://www.zimbra.com/license/yahoo_public_license_1.0.html"),
    ),  # type: ignore
    "http://www.zimbra.com/license/yahoo_public_license_1.0.html": CreativeWork(
        identifier="YPL-1.0",
        name="Yahoo! Public License v1.0",
        url=AnyUrl("http://www.zimbra.com/license/yahoo_public_license_1.0.html"),
    ),  # type: ignore
    "YPL-1.1": CreativeWork(
        identifier="YPL-1.1",
        name="Yahoo! Public License v1.1",
        url=AnyUrl("http://www.zimbra.com/license/yahoo_public_license_1.1.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/YPL-1.1": CreativeWork(
        identifier="YPL-1.1",
        name="Yahoo! Public License v1.1",
        url=AnyUrl("http://www.zimbra.com/license/yahoo_public_license_1.1.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/YPL-1.1.html": CreativeWork(
        identifier="YPL-1.1",
        name="Yahoo! Public License v1.1",
        url=AnyUrl("http://www.zimbra.com/license/yahoo_public_license_1.1.html"),
    ),  # type: ignore
    "http://www.zimbra.com/license/yahoo_public_license_1.1.html": CreativeWork(
        identifier="YPL-1.1",
        name="Yahoo! Public License v1.1",
        url=AnyUrl("http://www.zimbra.com/license/yahoo_public_license_1.1.html"),
    ),  # type: ignore
    "Zed": CreativeWork(
        identifier="Zed",
        name="Zed License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Zed"),
    ),  # type: ignore
    "https://spdx.org/licenses/Zed": CreativeWork(
        identifier="Zed",
        name="Zed License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Zed"),
    ),  # type: ignore
    "https://spdx.org/licenses/Zed.html": CreativeWork(
        identifier="Zed",
        name="Zed License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Zed"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/Zed": CreativeWork(
        identifier="Zed",
        name="Zed License",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/Zed"),
    ),  # type: ignore
    "Zeeff": CreativeWork(
        identifier="Zeeff",
        name="Zeeff License",
        url=AnyUrl("ftp://ftp.tin.org/pub/news/utils/newsx/newsx-1.6.tar.gz"),
    ),  # type: ignore
    "https://spdx.org/licenses/Zeeff": CreativeWork(
        identifier="Zeeff",
        name="Zeeff License",
        url=AnyUrl("ftp://ftp.tin.org/pub/news/utils/newsx/newsx-1.6.tar.gz"),
    ),  # type: ignore
    "https://spdx.org/licenses/Zeeff.html": CreativeWork(
        identifier="Zeeff",
        name="Zeeff License",
        url=AnyUrl("ftp://ftp.tin.org/pub/news/utils/newsx/newsx-1.6.tar.gz"),
    ),  # type: ignore
    "ftp://ftp.tin.org/pub/news/utils/newsx/newsx-1.6.tar.gz": CreativeWork(
        identifier="Zeeff",
        name="Zeeff License",
        url=AnyUrl("ftp://ftp.tin.org/pub/news/utils/newsx/newsx-1.6.tar.gz"),
    ),  # type: ignore
    "Zend-2.0": CreativeWork(
        identifier="Zend-2.0",
        name="Zend License v2.0",
        url=AnyUrl(
            "https://web.archive.org/web/20130517195954/http://www.zend.com/license/2_00.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Zend-2.0": CreativeWork(
        identifier="Zend-2.0",
        name="Zend License v2.0",
        url=AnyUrl(
            "https://web.archive.org/web/20130517195954/http://www.zend.com/license/2_00.txt"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Zend-2.0.html": CreativeWork(
        identifier="Zend-2.0",
        name="Zend License v2.0",
        url=AnyUrl(
            "https://web.archive.org/web/20130517195954/http://www.zend.com/license/2_00.txt"
        ),
    ),  # type: ignore
    "https://web.archive.org/web/20130517195954/http://www.zend.com/license/2_00.txt": CreativeWork(
        identifier="Zend-2.0",
        name="Zend License v2.0",
        url=AnyUrl(
            "https://web.archive.org/web/20130517195954/http://www.zend.com/license/2_00.txt"
        ),
    ),  # type: ignore
    "Zimbra-1.3": CreativeWork(
        identifier="Zimbra-1.3",
        name="Zimbra Public License v1.3",
        url=AnyUrl(
            "http://web.archive.org/web/20100302225219/http://www.zimbra.com/license/zimbra-public-license-1-3.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Zimbra-1.3": CreativeWork(
        identifier="Zimbra-1.3",
        name="Zimbra Public License v1.3",
        url=AnyUrl(
            "http://web.archive.org/web/20100302225219/http://www.zimbra.com/license/zimbra-public-license-1-3.html"
        ),
    ),  # type: ignore
    "https://spdx.org/licenses/Zimbra-1.3.html": CreativeWork(
        identifier="Zimbra-1.3",
        name="Zimbra Public License v1.3",
        url=AnyUrl(
            "http://web.archive.org/web/20100302225219/http://www.zimbra.com/license/zimbra-public-license-1-3.html"
        ),
    ),  # type: ignore
    "http://web.archive.org/web/20100302225219/http://www.zimbra.com/license/zimbra-public-license-1-3.html": CreativeWork(
        identifier="Zimbra-1.3",
        name="Zimbra Public License v1.3",
        url=AnyUrl(
            "http://web.archive.org/web/20100302225219/http://www.zimbra.com/license/zimbra-public-license-1-3.html"
        ),
    ),  # type: ignore
    "Zimbra-1.4": CreativeWork(
        identifier="Zimbra-1.4",
        name="Zimbra Public License v1.4",
        url=AnyUrl("http://www.zimbra.com/legal/zimbra-public-license-1-4"),
    ),  # type: ignore
    "https://spdx.org/licenses/Zimbra-1.4": CreativeWork(
        identifier="Zimbra-1.4",
        name="Zimbra Public License v1.4",
        url=AnyUrl("http://www.zimbra.com/legal/zimbra-public-license-1-4"),
    ),  # type: ignore
    "https://spdx.org/licenses/Zimbra-1.4.html": CreativeWork(
        identifier="Zimbra-1.4",
        name="Zimbra Public License v1.4",
        url=AnyUrl("http://www.zimbra.com/legal/zimbra-public-license-1-4"),
    ),  # type: ignore
    "http://www.zimbra.com/legal/zimbra-public-license-1-4": CreativeWork(
        identifier="Zimbra-1.4",
        name="Zimbra Public License v1.4",
        url=AnyUrl("http://www.zimbra.com/legal/zimbra-public-license-1-4"),
    ),  # type: ignore
    "Zlib": CreativeWork(
        identifier="Zlib",
        name="zlib License",
        url=AnyUrl("http://www.zlib.net/zlib_license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Zlib": CreativeWork(
        identifier="Zlib",
        name="zlib License",
        url=AnyUrl("http://www.zlib.net/zlib_license.html"),
    ),  # type: ignore
    "https://spdx.org/licenses/Zlib.html": CreativeWork(
        identifier="Zlib",
        name="zlib License",
        url=AnyUrl("http://www.zlib.net/zlib_license.html"),
    ),  # type: ignore
    "http://www.zlib.net/zlib_license.html": CreativeWork(
        identifier="Zlib",
        name="zlib License",
        url=AnyUrl("http://www.zlib.net/zlib_license.html"),
    ),  # type: ignore
    "zlib-acknowledgement": CreativeWork(
        identifier="zlib-acknowledgement",
        name="zlib/libpng License with Acknowledgement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/ZlibWithAcknowledgement"),
    ),  # type: ignore
    "https://spdx.org/licenses/zlib-acknowledgement": CreativeWork(
        identifier="zlib-acknowledgement",
        name="zlib/libpng License with Acknowledgement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/ZlibWithAcknowledgement"),
    ),  # type: ignore
    "https://spdx.org/licenses/zlib-acknowledgement.html": CreativeWork(
        identifier="zlib-acknowledgement",
        name="zlib/libpng License with Acknowledgement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/ZlibWithAcknowledgement"),
    ),  # type: ignore
    "https://fedoraproject.org/wiki/Licensing/ZlibWithAcknowledgement": CreativeWork(
        identifier="zlib-acknowledgement",
        name="zlib/libpng License with Acknowledgement",
        url=AnyUrl("https://fedoraproject.org/wiki/Licensing/ZlibWithAcknowledgement"),
    ),  # type: ignore
    "ZPL-1.1": CreativeWork(
        identifier="ZPL-1.1",
        name="Zope Public License 1.1",
        url=AnyUrl("http://old.zope.org/Resources/License/ZPL-1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/ZPL-1.1": CreativeWork(
        identifier="ZPL-1.1",
        name="Zope Public License 1.1",
        url=AnyUrl("http://old.zope.org/Resources/License/ZPL-1.1"),
    ),  # type: ignore
    "https://spdx.org/licenses/ZPL-1.1.html": CreativeWork(
        identifier="ZPL-1.1",
        name="Zope Public License 1.1",
        url=AnyUrl("http://old.zope.org/Resources/License/ZPL-1.1"),
    ),  # type: ignore
    "http://old.zope.org/Resources/License/ZPL-1.1": CreativeWork(
        identifier="ZPL-1.1",
        name="Zope Public License 1.1",
        url=AnyUrl("http://old.zope.org/Resources/License/ZPL-1.1"),
    ),  # type: ignore
    "ZPL-2.0": CreativeWork(
        identifier="ZPL-2.0",
        name="Zope Public License 2.0",
        url=AnyUrl("http://old.zope.org/Resources/License/ZPL-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/ZPL-2.0": CreativeWork(
        identifier="ZPL-2.0",
        name="Zope Public License 2.0",
        url=AnyUrl("http://old.zope.org/Resources/License/ZPL-2.0"),
    ),  # type: ignore
    "https://spdx.org/licenses/ZPL-2.0.html": CreativeWork(
        identifier="ZPL-2.0",
        name="Zope Public License 2.0",
        url=AnyUrl("http://old.zope.org/Resources/License/ZPL-2.0"),
    ),  # type: ignore
    "http://old.zope.org/Resources/License/ZPL-2.0": CreativeWork(
        identifier="ZPL-2.0",
        name="Zope Public License 2.0",
        url=AnyUrl("http://old.zope.org/Resources/License/ZPL-2.0"),
    ),  # type: ignore
    "ZPL-2.1": CreativeWork(
        identifier="ZPL-2.1",
        name="Zope Public License 2.1",
        url=AnyUrl("http://old.zope.org/Resources/ZPL/"),
    ),  # type: ignore
    "https://spdx.org/licenses/ZPL-2.1": CreativeWork(
        identifier="ZPL-2.1",
        name="Zope Public License 2.1",
        url=AnyUrl("http://old.zope.org/Resources/ZPL/"),
    ),  # type: ignore
    "https://spdx.org/licenses/ZPL-2.1.html": CreativeWork(
        identifier="ZPL-2.1",
        name="Zope Public License 2.1",
        url=AnyUrl("http://old.zope.org/Resources/ZPL/"),
    ),  # type: ignore
    "http://old.zope.org/Resources/ZPL/": CreativeWork(
        identifier="ZPL-2.1",
        name="Zope Public License 2.1",
        url=AnyUrl("http://old.zope.org/Resources/ZPL/"),
    ),  # type: ignore
}
