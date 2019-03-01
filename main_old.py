import sys, os


class HashCode:
	def write_file(self, file_path, file_content):
		with open(file_path, 'w', encoding='utf-8') as file_handle:
			file_handle.write(file_content)

	def read_file(self, file_path):
		with open(file_path, 'rb') as file_data:
			return file_data.read()

	def create_slide(self, raw_data):
		whole_data = raw_data.decode().split("\n")
		whole_data.pop(0)
		whole_data.pop(-1)
		slide_array = []
		for idx, val in enumerate(whole_data, start=1):
			obj = {idx: val}
			slide_array.append(obj)

		h_arrays = []
		v_arrays = []
		total_num_of_slide = 0

		for idx, val in enumerate(slide_array, start=1):
			if val[idx][0] == 'H':
				h_arrays.append(val)
			else:
				v_arrays.append(val)

		total_num_of_slide += len(h_arrays)
		v_array_modulus = len(v_arrays) % 2
		usable_v_arrays = len(v_arrays) - v_array_modulus
		total_num_of_slide += int(usable_v_arrays/2)

		del v_arrays[usable_v_arrays:]

		file_content = str(total_num_of_slide)
		file_content += '\n'
		for h_array in h_arrays:
			for key, value in h_array.items():
				file_content += str(key - 1)
				file_content += '\n'
		sub_v_arrays = [v_arrays[n:n + 2] for n in range(0, len(v_arrays), 2)]
		for single_sub_v_array in sub_v_arrays:
			s_sub_v_array = []
			for single_s_v_obj in single_sub_v_array:
				s_sub_v_array.append(int(list(single_s_v_obj.keys())[0]))

			file_content += "{} {}".format(s_sub_v_array[0] - 1, s_sub_v_array[1] - 1)
			file_content += '\n'
		return file_content


if __name__ == '__main__':
	args = sys.argv
	file_name = args[1]
	if file_name:
		test_file_path = "./{}".format(os.path.join(file_name))
		slide_show_maker = HashCode()
		raw_data = slide_show_maker.read_file(test_file_path)
		file_content = slide_show_maker.create_slide(raw_data)
		result_file_path = "./result_{}".format(file_name)
		slide_show_maker.write_file(result_file_path, file_content)
	else:
		print('No file name')
