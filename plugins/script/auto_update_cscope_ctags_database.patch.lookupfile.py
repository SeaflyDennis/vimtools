#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : plugins/script/auto_update_cscope_ctags_database.patch.lookupfile.py
# Author            : SeaflyGithub <seafly0616@qq.com>
# Date              : 2017.10.25 21时48分09秒
# Last Modified Date: 2017.10.25 21时48分17秒
# Last Modified By  : SeaflyGithub <seafly0616@qq.com>
# https://github.com/haolongzhangm/auto_update_cscope_ctags_database

        #ctags_cmd = "ctags -R --fields=+lafikmnsztS --extra=+fq -L tags.files"
        ctags_cmd = "ctags -R --file-scope=yes --langmap=c:+.h --links=yes --c-kinds=+p --c++-kinds=+p --fields=+iaS --extra=+q ."
        ctags_cmd = ctags_cmd + " 2>/dev/null 1>/dev/null"

        if not os.path.exists("systags"):
            ctags_cmd = ctags_cmd + " ; mv tags mytags"
            ctags_cmd = ctags_cmd + " ; ctags -R --file-scope=yes --langmap=c:+.h --links=yes"
            ctags_cmd = ctags_cmd + " --c-kinds=+p --c++-kinds=+p --fields=+iaS --extra=+q"
            ctags_cmd = ctags_cmd + " -I __THROW -I __attribute_pure__ -I __nonnull -I __attribute__"
            ctags_cmd = ctags_cmd + " /usr/include/* ."

        ctags_cmd = ctags_cmd + " ; mv tags systags"
        ctags_cmd = ctags_cmd + " ; cat systags >> mytags"
        ctags_cmd = ctags_cmd + " ; mv mytags tags"
        ctags_cmd = ctags_cmd + ' ; echo -e "!_TAG_FILE_SORTED\t2\t/2=foldcase" > ./filenametags'
        ctags_cmd = ctags_cmd + ' ; find ./ -type f -printf "%f\t%p\t1\n" | sort -f >> ./filenametags'

#:补丁插入位置开始:补丁插入位置结尾:补丁文件匹配字串:(用来判断该插件是否已经打了该补丁)
#:400:438:auto_update_cscope_ctags_database_patch_lookupfile_py
