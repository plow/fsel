import hashdeep
import obfuscate
import package

hashdeep_out_file = "file_hashes.out"

hashdeep.hashdeep(hashdeep_out_file)
obfuscate.obfuscate(hashdeep_out_file)
package.package()

