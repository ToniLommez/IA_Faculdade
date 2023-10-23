def findDecision(obj): #obj[0]: Historia do credito, obj[1]: Divida, obj[2]: Garantias, obj[3]: Renda Anual
	# {"feature": "Renda Anual", "instances": 11, "metric_value": 1.4949, "depth": 1}
	if obj[3] == '>35000':
		# {"feature": "Historia do credito", "instances": 6, "metric_value": 1.2516, "depth": 2}
		if obj[0] == 'Desconhecida':
			# {"feature": "Garantias", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2] == 'Nenhuma':
				# {"feature": "Divida", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'Baixa':
					return 'Alto'
				else: return 'Alto'
			elif obj[2] == 'Adequada':
				return 'Baixo'
			else: return 'Baixo'
		elif obj[0] == 'Boa':
			return 'Baixo'
		elif obj[0] == 'Ruim':
			return 'Moderado'
		else: return 'Moderado'
	elif obj[3] == '<15000':
		return 'Alto'
	elif obj[3] == '>=15000 a <=35000':
		# {"feature": "Divida", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == 'Alta':
			return 'Alto'
		elif obj[1] == 'Baixa':
			return 'Moderado'
		else: return 'Moderado'
	else: return 'Alto'
