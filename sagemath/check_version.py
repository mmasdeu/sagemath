from pkg_resources import parse_version

# Here we test that the version is the correct one
def check_version(version):
    try:
        import sage.all
    except ImportError:
        raise ValueError("Sage does not seem to be installed in this system. Please visit www.sagemath.org to fix this!")
    installed_version = sage.all.version().replace(',','').split()[2]
    if version.find('==') != -1:
        version = version.replace('==','')
        if parse_version(version) != parse_version(installed_version):
            raise ValueError("""\n******************************************************************\n
Sage version (= %s) is different from required one (= %s)\n
******************************************************************"""%(installed_version,version))
    elif version.find('>=') != -1:
        version = version.replace('>=','')
        if parse_version(version) > parse_version(installed_version):
            raise ValueError("""\n******************************************************************\n
Sage version (= %s) is older than the required one (= %s)\n
******************************************************************"""%(installed_version,version))
    elif version == '':
        pass
    else:
        raise ValueError("version argument (=%s) not understood"%version)
    return


